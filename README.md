# 🛒 E-Commerce Sales Data Pipeline

## 📌 Project Overview
An end-to-end ETL pipeline built using real Brazilian E-Commerce data from Kaggle (Olist Dataset). This project simulates how real companies like Amazon process thousands of orders every day.

## 🏗️ Architecture
CSV Files → Azure Data Lake → Azure Data Factory → Google Colab (PySpark) → SQL Server → SQL Reports

## 🛠️ Tools & Technologies
| Tool | Purpose |
|---|---|
| Azure Data Lake | Raw data storage |
| Azure Data Factory | Data pipeline orchestration |
| Google Colab + PySpark | Data transformation |
| SQL Server | Data warehouse |
| Python + Pandas | Data loading |
| GitHub | Version control |

## 📊 Dataset
- **Source:** Brazilian E-Commerce Dataset by Olist
- **Size:** 118,434 records
- **Tables Used:** Orders, Customers, Products, Payments, Reviews, Order Items

## 📁 Project Structure
ecommerce-data-pipeline/
├── data/
│   └── ecommerce_final_clean.csv
├── databricks/
│   └── ecommerce_transformation.ipynb
├── sql_reports/
│   └── business_queries.sql
├── adf_pipelines/
├── load_data.py
└── README.md

## 🔄 Pipeline Steps

### Step 1: Data Ingestion
- Downloaded raw CSV files from Kaggle
- Uploaded to Azure Data Lake Storage
- Built ADF pipeline to move data automatically

### Step 2: Data Transformation
- Cleaned data using PySpark in Google Colab
- Removed null values and duplicates
- Joined 6 tables into single dataframe

### Step 3: Data Loading
- Loaded 118,434 clean records into SQL Server
- Created ecommerce_db database

### Step 4: Business Reports
- Written 10 SQL queries for business insights

## 📈 Business Intelligence Queries
1. Top 10 Selling Products
2. Monthly Revenue Trend
3. Customer City Wise Order Count
4. Average Delivery Time by State
5. Revenue by Payment Type
6. Order Status Distribution
7. Top 10 Sellers by Revenue
8. Average Order Value by State
9. Peak Order Hours
10. Product Category Revenue

## 💡 Key Learnings
- Building end-to-end ETL pipelines
- Working with Azure cloud services
- Data transformation using PySpark
- SQL Server database management
- Business intelligence reporting

## 👨‍💻 Author
**Rishitha Kadali**
- GitHub: [@RISHITHAKADALI](https://github.com/RISHITHAKADALI)