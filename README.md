# 🏢 Internal Operations RAG Assistant  
### *AI-Powered Retrieval-Augmented Application for HR, IT, Finance & ERP Operational Scenarios*

This project is a **Retrieval-Augmented Generation (RAG) AI Assistant** designed to answer questions related to **HR policies, IT Support, Finance, Employee Onboarding, and ERP Operations** using the organization's internal PDF knowledgebase.

It ensures:  
✔ Accurate answers  
✔ Zero hallucinations  
✔ Explanations strictly based on the PDF  
✔ Clear step-by-step resolutions  

---

## 📌 Project Overview
Enterprise operations involve repetitive queries that usually require manually searching large documents.  
This AI assistant automates that process using:

- **LangChain RAG Pipeline**
- **HuggingFace Embeddings**
- **Chroma Vector Database**
- **Gemini 2.5 Flash LLM**
- **Streamlit UI**
- **Enterprise Knowledgebase PDF**

---

## 🎯 Objective
To build an internal AI assistant that:

- Retrieves accurate information from the enterprise PDF  
- Provides complete and rewritten resolutions  
- Avoids hallucinations or inventing policies  
- Gives step-by-step actions wherever applicable  

---

## 🧠 Key Features
### 🔍 Intelligent RAG Search
- Splits PDF into optimized chunks  
- Retrieves the **4 most relevant** sections  
- Ensures answers are grounded in the document  

### 🤖 LLM Reasoning (Gemini Flash)
- Controlled output using strict system prompts  
- Prevents hallucinations  
- Rewrites answers clearly  

### 📘 Includes Enterprise Knowledgebase  
The PDF contains scenarios related to:
- HR Leave Management  
- IT Troubleshooting  
- Finance Reimbursements  
- Employee Onboarding  
- ERP Workflows  

### 🎨 Streamlit UI
- Clean layout  
- Simple input  
- Instant AI responses  

---

## 📁 Project Structure
```
Internal-RAG-Assistant/
│── app.py
│── enterprise_rag_scenarios_only_clean.pdf
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repo
```
git clone https://github.com/SaiPraneethMarripelli/internal-rag-assistant.git
cd internal-rag-assistant
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Add Your Google API Key
Set inside **app.py**:
```python
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
```

### 4️⃣ Launch Streamlit
```
streamlit run app.py
```

---

## 📈 Example Queries
- “Employee applied for medical leave without a certificate. What is the rule?”
- “Laptop not available on DOJ—what to do?”
- “VPN disconnecting repeatedly—resolution?”
- “Reimbursement without invoice—what happens?”
- “PO exceeds department budget—workflow?”

---

## 🚫 Hallucination Prevention
The assistant follows strict rules:
- Use only PDF content  
- No assumptions  
- No referencing case numbers  
- If answer not found →  
  **“The document does not contain information related to this query.”**

---

## 🚀 Future Enhancements
- Multi-PDF support  
- Add chat history  
- Deploy to cloud platforms  
- Role-based access  
- Evaluation metrics  

---

## 👤 Author
**Sai Praneeth Marripelli**  
📧 Email: saipraneethmarripelli@gmail.com  
🔗 LinkedIn: www.linkedin.com/in/saipraneeth-marripelli-2003sai  

---

## ⭐ Support  
If this project helped you, give it a ⭐ on GitHub!
