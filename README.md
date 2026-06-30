# 📈 Real-Time Market Analytics Platform

A modular ETL pipeline that extracts real-time stock market data from Yahoo Finance, transforms and validates it using Python, stores it in SQL Server, and visualizes business insights using Power BI.

---

## 🚀 Project Overview

This project demonstrates an end-to-end data analytics workflow similar to those used in industry.

The pipeline:

- Extracts historical stock market data from Yahoo Finance
- Cleans and validates the data
- Calculates financial metrics such as daily returns and volatility
- Loads processed data into SQL Server
- Creates SQL views for reporting
- Builds interactive Power BI dashboards

---

## 🏗️ Project Architecture

```
Yahoo Finance API
        │
        ▼
Extract (Python)
        │
        ▼
Transform & Validation
        │
        ▼
Business Analytics
        │
        ▼
SQL Server Database
        │
        ▼
SQL Views
        │
        ▼
Power BI Dashboard
```

---

## 🛠️ Tech Stack

- Python
- Pandas
- yfinance
- SQL Server
- SQLAlchemy
- pyodbc
- Power BI
- Git & GitHub

---

## 📂 Project Structure

```
Market-Analysis/
│
├── analytics.py
├── config.py
├── extract.py
├── transform.py
├── validation.py
├── load.py
├── logger.py
├── main.py
│
├── sql/
│   ├── create_tables.sql
│   └── views.sql
│
├── powerbi/
│   └── Market_PowerBI.pbix
│
├── screenshots/
│
├── output/
│
├── data/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Features

- Modular ETL Pipeline
- Data Validation
- Incremental SQL Loading
- Logging
- SQL Views
- Power BI Dashboard
- Performance Ranking
- Volatility Analysis
- Trading Volume Analysis
- Risk vs Return Analysis

---

## 📈 Business Metrics

The project calculates:

- Daily Return
- Average Return
- Average Trading Volume
- Highest Price
- Lowest Price
- Volatility
- Top Gainer
- Top Loser

---

## 📊 Power BI Dashboards

### Executive Dashboard

- KPI Cards
- Performance Ranking
- Trading Volume
- Volatility Comparison

### Stock Trend Analysis

- Daily Closing Price
- Daily Return Trend
- Trading Volume Trend

### Stock Insights

- Risk vs Return Analysis
- Trading Volume Distribution
- Highest Price Reached
- Lowest Price Reached

---

## 🗄️ SQL Views

- vw_Daily_Stock_Data
- vw_Stock_Performance
- vw_Monthly_Trend
- vw_Stock_Ranking

---

## ▶️ How to Run

### Clone the repository

```bash
git clone <repository-url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure SQL Server

Update the SQL Server details in:

```
config.py
```

### Run the ETL Pipeline

```bash
python main.py
```

---

## 📸 Dashboard Screenshots


<img width="1078" height="611" alt="dashboard_page1 png" src="https://github.com/user-attachments/assets/1abaf4ae-f861-42c4-8f2a-41506ddaa5c9" />
<img width="1052" height="607" alt="dashboard_page2 png" src="https://github.com/user-attachments/assets/4b3942ce-6791-4cb9-9aa4-ca4482e03f9d" />
<img width="1078" height="593" alt="dashboard_page3 png" src="https://github.com/user-attachments/assets/5c2a0ea2-a339-4415-9f62-728070187203" />

---

## 🔮 Future Improvements

- Scheduled ETL execution
- Email reporting
- Live streaming market data
- Portfolio analytics
- Machine Learning based price prediction

---

## 👨‍💻 Author

**Gayatri Apotikar**

Electronics & Telecommunication Engineering  
Minor in Artificial Intelligence & Machine Learning
