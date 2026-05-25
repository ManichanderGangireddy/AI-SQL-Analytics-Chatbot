# AI-Powered Enterprise SQL Analytics Chatbot 🤖

## Project Overview

This project is an AI-powered SQL analytics chatbot developed using Python, LangChain, Gemini AI, SQLite, and Streamlit.

The chatbot allows users to ask business-related questions in natural language, and the system automatically converts them into SQL queries to retrieve insights from the database.

---

## Features

- Natural Language to SQL Query Conversion
- AI-Powered Business Analytics
- Enterprise Sales Database
- LangChain SQL Agent Integration
- Gemini AI Integration
- Streamlit Web Interface
- Semantic Layer (RAG-based Prompting)

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| SQLite | Database |
| LangChain | AI Agent Framework |
| Gemini AI | Large Language Model |
| Streamlit | Web Application UI |
| Pandas | Data Processing |
| SQLAlchemy | Database Connection |

---

## Project Structure

```text
AI-SQL-Analytics-Chatbot/
│
├── app.py
├── database_setup.py
├── enterprise_sales.db
├── requirements.txt
└── README.md
```

---

## Database Tables

### Customers Table
- customer_id
- company_name
- region

### Sales Table
- order_id
- customer_id
- product
- revenue
- status

### Products Table
- product_name
- cost_to_build

---

## How to Run the Project

### Step 1: Install Libraries

```bash
pip install -r requirements.txt
```

### Step 2: Create Database

```bash
python database_setup.py
```

### Step 3: Run Chatbot

```bash
streamlit run app.py
```

---

## Sample Questions

- Show all customers
- Calculate total revenue
- Show completed orders
- Which company generated highest revenue?
- Calculate total profit for completed orders

---

## AI Workflow

```text
User Question
      ↓
Gemini AI
      ↓
LangChain SQL Agent
      ↓
SQL Query Generation
      ↓
SQLite Database
      ↓
Business Insight Response
```

---

## Future Improvements

- Chat History
- Dashboard Visualization
- CSV Upload Support
- Authentication System
- Voice Assistant
- Graphical Analytics

---

## Project Demo

(Add chatbot screenshot here later)

Example:

```markdown
![Chatbot Demo](chatbot_demo.png)
```


## GitHub Repository

GitHub Link:
https://github.com/ManichanderGangireddy/AI-SQL-Analytics-Chatbot

---

## Author

Manichander Gangireddy
