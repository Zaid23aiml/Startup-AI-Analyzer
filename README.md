# 🚀 AI Startup Idea Analyzer (Multi-Agent System)

## 📌 Overview
AI Startup Idea Analyzer is a multi-agent AI system designed to evaluate startup ideas using structured analysis instead of simple text generation.

Unlike traditional chatbot-based systems, this project demonstrates how to build an **AI decision-support pipeline** using:
- Multi-agent architecture
- Workflow orchestration
- Tool-based reasoning
- Structured output generation

---

## 🎯 Problem Statement
Evaluating startup ideas manually requires:
- Market research
- Competitor analysis
- Risk assessment
- Cost estimation

This process is time-consuming and unstructured.

---

## 💡 Solution
This system automates startup evaluation using **AI agents** that perform:
- Market research
- Risk analysis
- Structured reporting
- Context-aware Q&A

---

## 🧠 Key Features

### 🔹 Multi-Agent Architecture
- Research Agent → collects market insights
- Risk Agent → evaluates startup risks
- Chatbot Agent → answers follow-up questions

### 🔹 Workflow Orchestration
- Built using LangGraph
- Sequential agent execution pipeline

### 🔹 Real-Time Research
- Uses web search API to gather up-to-date data

### 🔹 Context-Aware Chatbot
- Answers queries based on analyzed startup idea

### 🔹 Structured Output
- Generates organized reports instead of raw text

---

## 🏗️ System Architecture

User Input  
↓  
Research Agent  
↓  
Risk Analysis Agent  
↓  
Structured Startup Report  
↓  
Interactive Chatbot  

---

## 🛠️ Tech Stack

- Python
- Streamlit (UI)
- LangChain + LangGraph (AI workflow)
- Groq API (LLM)
- Tavily API (web search)
- dotenv

---

## ⚙️ How It Works

1. User enters startup idea
2. Research agent gathers market data
3. Risk agent evaluates feasibility
4. System generates structured report
5. Chatbot allows interactive exploration

---

## 🚀 Running the Project

### 1. Clone Repository
```bash
git clone <your-repo-link>
cd startup-ai-analyzer
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables
Create `.env` file:

```
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

### 5. Run Application
```bash
streamlit run app.py
```

---

## ⚠️ Limitations
- Depends on external APIs (Groq, Tavily)
- Response time may vary due to multi-agent pipeline
- Current version uses a fixed workflow (future: dynamic agent routing)

---

## 🔮 Future Improvements
- Dynamic query routing (intent-based agents)
- Startup scoring system
- Cost estimation engine
- Offline model support (Ollama)
- Visual analytics dashboard

---

## 📌 Key Learning Outcomes
- Multi-agent system design
- LLM integration with tools
- Workflow orchestration using LangGraph
- Building end-to-end AI applications

---

## 📢 Disclaimer
This tool is for educational purposes and does not provide financial or legal advice.
