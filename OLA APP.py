st.title("🚀 TEST UPDATE CHECK")
#Import required packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# ---------------------------------------------------------
# FUNCTION TO CONNECT DATABASE
# ---------------------------------------------------------

def get_data(query, params=None):

    conn = sqlite3.connect("olaride_db.sqlite")

    if params:
        df = pd.read_sql_query(query, conn, params=params)

    else:
        df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# CSS HERE (TOP OF FILE)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fb;
    }

    section[data-testid="stSidebar"] {
        background-color: #e9eef7;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# STREAMLIT PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="OLA Ride Analytics Dashboard",
    page_icon="🚖",
    layout="wide"
)

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Project Introduction",
        "OLA Ride Data Visualization",
        "SQL Queries",
        "Creator Info"
    ]
)

# =========================================================
# PAGE 1 : PROJECT INTRODUCTION
# =========================================================

if page == "Project Introduction":

    st.title("🚖 OLA Ride Analytics Dashboard")

    st.image("OLA LOGO.png", width=250)

    st.subheader(
        "Ride Booking Analysis using Python, SQL, Data Visualization and Streamlit"
    )

    st.write("""
    This project analyzes OLA ride booking data.

    Features:

    ✅ Ride Booking Analysis

    ✅ Vehicle Type Performance

    ✅ Cancellation Analysis

    ✅ Customer & Driver Ratings

    ✅ Payment Method Insights

    ✅ SQL Query-Based Business Insights

    Tools Used:

    - Python
    - Pandas
    - SQLite3
    - SQL
    - Streamlit
    - Plotly
    """)

# =========================================================
# PAGE 2 : DATA VISUALIZATION
# =========================================================

elif page == "OLA Ride Data Visualization":

    st.title("🚖 OLA Ride Dashboard")

    # ---------------------------------------------------------
    # VEHICLE FILTER
    # ---------------------------------------------------------

    vehicles = get_data("""
    SELECT DISTINCT Vehicle_Type
    FROM ride_data
    """)["Vehicle_Type"].tolist()

    selected_vehicle = st.selectbox(
        "Select Vehicle Type",
        vehicles
    )

    # ---------------------------------------------------------
    # REVENUE BY VEHICLE TYPE
    # ---------------------------------------------------------

    st.subheader("🚗 Revenue by Vehicle Type")
    st.write("This section shows the total revenue generated based on booking values across different vehicle types.")

    revenue = get_data("""
    SELECT
        Vehicle_Type,
        SUM(Booking_Value) AS Revenue
    FROM ride_data
    WHERE Booking_Value IS NOT NULL
    GROUP BY Vehicle_Type
    ORDER BY Revenue DESC
    """)

    revenue = revenue.dropna()

    st.bar_chart(revenue.set_index("Vehicle_Type"))


    # ---------------------------------------------------------
    # BOOKING STATUS DISTRIBUTION
    # ---------------------------------------------------------
    st.subheader("📊 Booking Status Distribution")
    st.write("Shows the count of rides by booking status such as Success, Cancelled, Driver Not Found, and Incomplete.")
    status = get_data("""
    SELECT
        Booking_Status,
        COUNT(*) AS Total
    FROM ride_data
    GROUP BY Booking_Status
    """)

    st.dataframe(status)

    # =========================================================
    # CUSTOMER RATING ANALYSIS
    # =========================================================
    st.subheader("⭐ Customer Rating Analysis")
    st.write("This analysis provides insights into customer satisfaction by studying rating patterns across rides, helping identify service quality trends and improvement areas.")

    rating = get_data("""
    SELECT
        Vehicle_Type,
        ROUND(
            AVG(Customer_Rating),
            2
        ) AS Rating
    FROM ride_data
    GROUP BY Vehicle_Type
    """)

    st.bar_chart(
        rating.set_index("Vehicle_Type")
    )

    # ---------------------------------------------------------
    # PAYMENT METHOD DISTRIBUTION
    # ---------------------------------------------------------

    st.subheader(" 💳 Payment Method Distribution")
    st.write("This analysis shows the distribution of payment methods used by customers across rides, helping to understand customer preferences such as cash, digital wallets, or card payments. It provides insights into transaction behavior and supports decisions for improving payment options and digital adoption strategies.")
    # STEP 1: Get data from SQL
    payment = get_data("""
    SELECT
        Payment_Method,
        COUNT(*) AS Total
    FROM ride_data
    GROUP BY Payment_Method
    ORDER BY Total DESC
    """)

    # STEP 2: Show table 

    # STEP 3: Pie chart
    fig, ax = plt.subplots(figsize=(3, 3))

    ax.pie(
        payment["Total"],
        labels=payment["Payment_Method"],
        autopct="%1.1f%%",
        startangle=140,
        textprops={'fontsize': 8}
    )

    ax.axis("equal")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.pyplot(fig)

    # =========================================================
    # OUTLIER ANALYSIS
    # =========================================================

    st.subheader("📦 Outlier Analysis")
    st.write("This analysis identifies unusual or extreme values in ride data such as fare amount, distance, or ride duration. Detecting outliers helps highlight potential data errors, fraud cases, or rare high-value trips, and supports improving data quality and operational decision-making.")
    numeric_columns = [
        "Booking_Value",
        "Ride_Distance",
        "Driver_Ratings",
        "Customer_Rating"
    ]

    selected_column = st.selectbox(
        "Select Numeric Column",
        numeric_columns
    )

    # Fetch required column
    outlier_df = get_data(f"""
    SELECT {selected_column}
    FROM ride_data
    WHERE {selected_column} IS NOT NULL
    """)

    # Box Plot
    fig, ax = plt.subplots(figsize=(8, 3))

    sns.boxplot(
        x=outlier_df[selected_column],
        ax=ax
    )

    ax.set_title(f"Outlier Detection - {selected_column}")

    st.pyplot(fig)

    # IQR Method
    Q1 = outlier_df[selected_column].quantile(0.25)
    Q3 = outlier_df[selected_column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    outliers = outlier_df[
        (outlier_df[selected_column] < lower_bound)
        |
        (outlier_df[selected_column] > upper_bound)
    ]

    st.metric(
        "Number of Outliers",
        len(outliers)
    )

    st.write("Sample Outlier Records")

    st.dataframe(outliers.head(20))

    # =========================================================
    # OUTLIER SUMMARY
    # =========================================================

    st.subheader("📊 Outlier Summary")

    summary = pd.DataFrame({
        "Column": [
            "Booking_Value",
            "Ride_Distance",
            "Driver_Ratings",
            "Customer_Rating"
        ],
        "Outliers": [
            8468,
            0,
            9469,
            9636
        ]
    })

    st.dataframe(summary)

        

# =========================================================
# PAGE 3 : SQL QUERIES
# =========================================================

elif page == "SQL Queries":

    st.title("📋 OLA RIDE INSIGHTS SQL Query Results")

    queries = {

        "1. Retrieve all successful bookings":
        """
        SELECT Booking_ID,Booking_Status
        FROM ride_data
        WHERE Booking_Status = 'Success'
        """
    ,

        "2. Average ride distance for each vehicle type":
        """
        SELECT
            Vehicle_Type,
            ROUND(AVG(Ride_Distance), 2) AS Avg_Ride_Distance
        FROM ride_data
        GROUP BY Vehicle_Type
        ORDER BY Avg_Ride_Distance DESC
        """
    ,

        "3. Total number of rides cancelled by customers":
        """
        SELECT
            Booking_Status,
            COUNT(*) AS Total_Cancelled_Rides
        FROM ride_data
        WHERE Booking_Status = 'Canceled by Customer'
        GROUP BY Booking_Status
        """
    ,

        "4. Top 5 customers by number of rides":
        """
        WITH customer_rides AS (
            SELECT
                Customer_ID,
                COUNT(*) AS Total_Rides,
                ROW_NUMBER() OVER (
                    ORDER BY COUNT(*) DESC
                ) AS rn
            FROM ride_data
            GROUP BY Customer_ID
        )

        SELECT *
        FROM customer_rides
        WHERE rn <= 5
        """
    ,

        "5. Driver cancellations due to personal and car-related issues":
        """
        SELECT
            COUNT(*) AS Driver_Cancelled_Rides
        FROM ride_data
        WHERE Canceled_Rides_by_Driver =
        'Personal & Car related issue'
        """
    ,

        "6. Maximum and minimum driver ratings for Prime Sedan":
        """
        SELECT
            MAX(Driver_Ratings) AS Max_Driver_Rating,
            MIN(Driver_Ratings) AS Min_Driver_Rating
        FROM ride_data
        WHERE Vehicle_Type = 'Prime Sedan'
        """
    ,

        "7. Total rides paid using UPI":
        """
        SELECT
            COUNT(*) AS Total_UPI_Rides
        FROM ride_data
        WHERE Payment_Method = 'UPI'
        """
    ,

        "8. Average customer rating per vehicle type":
        """
        SELECT
            Vehicle_Type,
            ROUND(
                AVG(Customer_Rating),
                2
            ) AS Avg_Customer_Rating
        FROM ride_data
        GROUP BY Vehicle_Type
        ORDER BY Avg_Customer_Rating DESC
        """
    ,

        "9. Total booking value of successful rides":
        """
        SELECT
            SUM(Booking_Value)
            AS Total_Booking_Value
        FROM ride_data
        WHERE Booking_Status = 'Success'
        """
    ,

        "10. Incomplete rides and their reasons":
        """
        SELECT
            Incomplete_Rides_Reason,
            COUNT(*) AS Total_Rides
        FROM ride_data
        WHERE Incomplete_Rides = 'Yes'
        GROUP BY Incomplete_Rides_Reason
        ORDER BY Total_Rides DESC
        """
    }
    

    # Query selection
    selected_query = st.selectbox(
        "Choose a Query",
        list(queries.keys())
    )

    # Execute query
    query_result = get_data(
        queries[selected_query]
    )

    # Display result
    st.write("### Query Result")

    st.dataframe(query_result)

    # Show insight
    
    if selected_query == "1. Retrieve all successful bookings":
        st.info("Business Insight: This analysis helps understand total completed ride volume and overall platform performance efficiency.")

    elif selected_query == "2. Average ride distance for each vehicle type":
        st.info("Business Insight: This helps identify usage patterns across vehicle types and supports fleet optimization and pricing strategy decisions.")

    elif selected_query == "3. Total number of rides cancelled by customers":
        st.info("Business Insight: This highlights customer cancellation behavior and helps identify issues such as pricing, waiting time, or service experience.")

    elif selected_query == "4. Top 5 customers by number of rides":
        st.info("Business Insight: This identifies high-value customers who can be targeted for loyalty programs and personalized offers.")

    elif selected_query == "5. Driver cancellations due to personal and car-related issues":
        st.info("Business Insight: This helps detect operational issues related to driver availability and vehicle condition, improving service reliability.")

    elif selected_query == "6. Maximum and minimum driver ratings for Prime Sedan":
        st.info("Business Insight: This helps evaluate driver performance quality and identify service consistency within the Prime Sedan category.")

    elif selected_query == "7. Total rides paid using UPI":
        st.info("Business Insight: This shows digital payment adoption trends and customer preference for cashless transactions.")

    elif selected_query == "8. Average customer rating per vehicle type":
        st.info("Business Insight: This helps compare customer satisfaction across vehicle types and identify best-performing categories.")

    elif selected_query == "9. Total booking value of successful rides":
        st.info("Business Insight: This provides insights into total revenue generated from completed rides and overall business performance.")

    elif selected_query == "10. Incomplete rides and their reasons":
        st.info("Business Insight: This helps identify failure points in the booking journey and supports improving ride completion rates and service quality.")


# =========================================================
# PAGE 4 : CREATOR INFO
# =========================================================

elif page == "Creator Info":

    st.title("👩‍💻 Creator of this Project")

    st.write("""
    **Developed by:** A Harini

    **Skills:** Python, SQL, Data Analysis,Data Visualization, Pandas, EDA, Matplotlib, Streamlit
    """)