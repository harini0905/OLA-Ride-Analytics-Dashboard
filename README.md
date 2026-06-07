# Ola Ride Insights

## Project Description

OLA Ride Insights is a data analytics project developed to analyze ride-booking data and generate actionable business insights. The project uses SQLite, SQL, Python and Streamlit to perform data analysis, visualization, and interactive reporting.


The system helps identify:

- Ride booking trends
- Revenue performance
- Customer behavior patterns
- Vehicle type performance
- Ride cancellation reasons
- Customer and driver rating trends
- Payment method preferences


### 🔴 Live Streamlit Dashboard
Explore the deployed dashboard here:  
👉 https://ola-ride-analytics-dashboard.streamlit.app/

---

# Features

- Ride Volume Trend Analysis
- Revenue Analysis Dashboard
- Booking Status Analysis
- Vehicle Type Performance Analysis
- Customer and Driver Rating Analysis
- Ride Cancellation Analysis
- Interactive Streamlit Dashboard
- SQL Query Insights

---

## Business Objectives

- Analyze ride booking trends and peak demand periods.
- Understand customer and driver behavior.
- Identify cancellation patterns and their causes.
- Evaluate revenue generation across payment methods.
- Monitor customer and driver ratings.
- Generate actionable insights for business improvement.

---
## Data Cleaning & Preprocessing

The dataset underwent preprocessing before analysis to ensure data quality, consistency, and reliability.

The following steps were performed:

- Identified and handled missing values using appropriate statistical techniques such as Mean, Median, and Mode imputation.
- Standardized column names.
- Dropped two columns V_TAT, C_TAT.
- Validated booking status, payment methods, ratings, and vehicle type values.
- Checked for duplicate records and data inconsistencies.
- Verified numerical columns such as booking value, ride distance, customer ratings, and driver ratings.
- Ensured proper data types for analytical processing.
- Performed exploratory data analysis (EDA) to understand data distribution and identify anomalies.
- Prepared a cleaned dataset for SQL analysis and Streamlit dashboard development.

The cleaned dataset was stored in SQLite for efficient querying and analysis.


## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Data Analysis |
| SQL | Data Querying |
| SQLite | Database |
| Streamlit | Dashboard Development |
| Pandas | Data Manipulation |
| Matplotlib | Visualization |
| Seaborn | Statistical Visualization |
| Git & GitHub | Version Control |

---

## Project Structure

```text
OLA RIDE PROJECT/
│
├── OLA APP.py
├── requirements.txt
├── README.md
├── .gitignore   
├── OLA LOGO.png
│
├── Report/
│   └── OLA_Ride_Insights_Report.pdf
│
├── Streamlit Screenshots/
│   ├── Dashboard_Home.png
│   ├── Revenue_By_Vehicle_Type.png
│   ├── Booking_Status_Distribution.png
│   ├── Customer_Rating_Analysis.png
│   ├── Payment_Method_Distribution.png
│   ├── Outlier_Analysis.png
│   ├── SQL_Query_Results.png
    
```



## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/OLA-Ride-Insights.git
```

### Step 2: Open the Project Folder

```bash
cd OLA-Ride-Insights
```


### Step 3: Run the Streamlit Application

```bash
streamlit run OLA APP.py
```

### Step 4: Open in Browser

After running the command, Streamlit will automatically open in your default browser.

---

# Dashboard Screenshots

## Dashboard Home
![Dashboard Home](Streamlit_Screenshots/Dashboard_Home.png)

## Revenue By Vehicle Type
![Revenue By Vehicle Type](Streamlit_Screenshots/Revenue_By_Vehicle_Type.png)

## Booking Status Distribution
![Booking Status Distribution](Streamlit_Screenshots/Booking_Status_Distribution.png)

## Customer Rating Analysis
![Customer Rating Analysis](Streamlit_Screenshots/Customer_Rating_Analysis.png)

## Payment Method Distribution
![Payment Method Distribution](Streamlit_Screenshots/Payment_Method_Distribution.png)

## Outlier Analysis
![Outlier Analysis](Streamlit_Screenshots/Outlier_Analysis.png)

## Outlier Summary
![Outlier Summary](Streamlit_Screenshots/Outlier_Summary.png)

## SQL Query Results
![SQL Query Results](Streamlit_Screenshots/SQL_Query_Results.png)


---

## Data Source

The Streamlit application uses a SQLite database (`olaride_db.sqlite`) as its primary data source.

---

### Note
The original raw dataset and intermediate Excel files were used during the data cleaning and preprocessing phase but are not required for running the application. The final processed data is stored in the SQLite database used by the Streamlit dashboard.

---

# SQL Queries Implemented 

1. Retrieve all successful bookings
2. Average ride distance for each vehicle type
3. Total number of rides cancelled by customers
4. Top 5 customers by number of rides
5. Driver cancellations due to personal and car-related issues
6. Maximum and minimum driver ratings for Prime Sedan bookings
7. Total rides paid using UPI
8. Average customer rating per vehicle type
9. Total booking value of successful rides
10. Incomplete rides and their reasons

---

# Business Insights Generated

- Identified peak booking periods and ride demand trends
- Analyzed revenue contribution by payment method
- Identified vehicle categories with the highest ride distance
- Evaluated customer satisfaction using rating analysis
- Examined ride cancellation patterns and root causes
- Identified high-value customers based on booking value
- Assessed driver performance through ratings analysis

---

# Future Enhancements

- Ride Demand Forecasting using Machine Learning
- Driver Allocation Optimization
- Real-time Ride Monitoring Dashboard
- Geographic Ride Heatmaps
- Customer Churn Prediction
- Cloud Database Integration

---

# Author

## A. Harini

### Skills

- Python
- SQL
- SQLite
- Streamlit
- EDA
- Data Analysis
- Data Visualization
- Pandas
