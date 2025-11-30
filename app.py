import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI


# ============================================
# PUT YOUR GOOGLE API KEY HERE
# ============================================
api_key = "AIzaSyA-Z-21As1dCSr76m7kgw2t1-O3KQ54mTQ"
os.environ["GOOGLE_API_KEY"] = api_key


# ============================================
# Streamlit UI
# ============================================
st.set_page_config(page_title="Internal Operations RAG Assistant", layout="wide")

st.title("🏢 Internal Associative Operations RAG Assistant")
st.write("""
This assistant answers Internal Operational Scenarios using the enterprise PDF of the company.
It gives **complete explanations**, **resolutions**, and avoids **hallucinations**.
""")


# ============================================
# PDF PATH (you already have locally)
# ============================================
PDF_PATH = r"enterprise_rag_scenarios_only_clean.pdf"

if not os.path.exists(PDF_PATH):
    st.error(f"❌ PDF not found at: {PDF_PATH}")
    st.stop()


# ============================================
# LOAD PDF
# ============================================
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()


# ============================================
# TEXT SPLITTING
# ============================================
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=80
)
splits = text_splitter.split_documents(docs)


# ============================================
# HUGGING FACE EMBEDDINGS (CPU SAFE)
# ============================================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)


# ============================================
# VECTORDB (IN-MEMORY)
# ============================================
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})


# ============================================
# LLM - GEMINI 2.5 FLASH
# ============================================
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.1
)


# ============================================
# SYSTEM INSTRUCTIONS FOR BETTER OUTPUT
# ============================================
system_prompt = """
You are an Internal Operations AI Assistant.

Your ONLY knowledge comes from the PDF.

RULES:
1. Read the retrieved context carefully.
2. Give a **full resolution**, not short answers.
3. DO NOT mention or guess any case numbers.
4. Rewrite the resolution clearly even if PDF says "Case 40".
5. Provide step-by-step actions and explanation when possible.
6. If the PDF does NOT contain the answer, say:
   "The document does not contain information related to this query."
7. Do NOT invent new policies or assumptions.
"""


# ============================================
# RAG CHAIN FUNCTION
# ============================================
def rag_answer(query):
    docs = retriever.invoke(query)
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
Context from PDF:
{context}

User Query:
{query}

Write a complete resolution based ONLY on the above context.
Do NOT mention case numbers.
Rewrite the answer in full sentences.
"""

    messages = [
        ("system", system_prompt),
        ("human", prompt)
    ]

    response = llm.invoke(messages)
    return response.content


# ============================================
# STREAMLIT INPUT
# ============================================
user_query = st.text_input("Ask your internal operations question:")

if st.button("Get Answer"):
    if user_query.strip():
        st.subheader("📘 Answer:")
        answer = rag_answer(user_query)
        st.write(answer)
    else:
        st.warning("Please enter a question.")
