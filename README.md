# 🛡️ AI SOC Dashboard

An AI-powered **Security Operations Center (SOC) Dashboard** that detects anomalies in network traffic using Machine Learning, applies rule-based analysis, and generates **AI-driven threat explanations and mitigation strategies**.

---

## 🚀 Overview

Modern cybersecurity systems generate massive logs that are difficult to analyze manually.

**AI SOC Dashboard** simulates a real-world SOC system by:

- Detecting anomalous behavior using ML
- Applying rule-based threat detection
- Assigning severity levels
- Generating AI explanations using LLMs
- Visualizing alerts in a dashboard

👉 Built fully with **free and local technologies**

---

## 🧠 Architecture
```
Logs (CSV / Generated Data)
↓
Preprocessing Layer
↓
ML Detection (Isolation Forest)
↓
Rule Engine (Custom Logic)
↓
Severity Scoring Engine
↓
AI Explanation (Ollama LLM)
↓
Streamlit Dashboard
```
---

## 🧩 Tech Stack

- **Backend** → FastAPI  
- **Frontend** → Streamlit  
- **ML Model** → Isolation Forest (scikit-learn)  
- **AI (LLM)** → Ollama (Mistral)  
- **Data Processing** → Pandas  

---

## ✨ Features

### 🧠 Hybrid Threat Detection
- ML-based anomaly detection  
- Rule-based attack detection  

### 🚨 Severity Scoring
- Combines ML output + rules  
- Categorizes alerts into:
  - Low
  - Medium
  - High
  - Critical  

### 🤖 AI Threat Explanation
- Explains why traffic is suspicious  
- Suggests mitigation steps  

### 📊 SOC Dashboard
- Severity metrics  
- Alert visualization  
- Filterable alerts  
- Critical alert panel  

### 🔄 Real-Time Simulation
- Auto-refresh dashboard  
- Simulated streaming behavior  

---

## 📂 Project Structure
```
ai-soc-dashboard/
│
├── backend/
│ ├── main.py
│ ├── detection.py
│ ├── preprocessing.py
│ ├── rules.py
│ ├── severity.py
│ ├── agents.py
│ ├── llm.py
│ └── train.py
│
├── frontend/
│ └── app.py
│
├── data/
│ ├── logs.csv
│ └── generate_logs.py
│
├── models/
│ └── model.pkl (ignored in git)
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository


- git clone https://github.com/your-username/ai-soc-dashboard.git

- cd ai-soc-dashboard


---

### 2. Install Dependencies


- pip install -r requirements.txt


---

### 3. Generate Dataset (Optional)


- python data/generate_logs.py


---

### 4. Train Model


- python backend/train.py


---

### 5. Start Backend


- uvicorn backend.main:app --reload


---

### 6. Start Frontend


- streamlit run frontend/app.py


---

## 🚀 Future Improvements

- IP-based attack correlation  
- Time-series anomaly detection  
- Real-time streaming logs  
- Advanced multi-agent reasoning  
- Graph-based attack visualization  

---

## 👤 Author

Khushi Sharma

---

## ⭐ If You Like This Project

Give it a star ⭐ on GitHub
