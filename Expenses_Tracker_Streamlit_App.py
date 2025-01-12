import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime, date
import plotly.express as px

# Page Title
st.set_page_config(page_title="Expense Tracker",
                   page_icon="💰",
                   layout="wide",
                   initial_sidebar_state="expanded")

# Connecting to MySQL database
conn = sqlite3.connect("expenses_db.db")

# Streamlit App Title
st.title("Analyzing Expenses Tracker")

# Sidebar for date input
current_year = datetime.now().year
default_start_date = date(2024, 1, 1)
st.sidebar.header("2024 Year Expenses Data 🗓️")
st.sidebar.markdown("""Choose a date to view the transaction details for that specific day""")
selected_date = st.sidebar.date_input("Select a Date:", value=default_start_date)

# Fetching entire data from MySQL database
def fetch_data(selected_date):
    query = f"SELECT DISTINCT Date, Category, Payment_mode, Description, Amount, Cashback FROM expense_tb WHERE Date = '{selected_date}';"
    df = pd.read_sql(query, conn)
    return df

# Displaying selected data for date
filtered_data = fetch_data(selected_date)
if not filtered_data.empty:
    st.write("Data for the chosen date:", selected_date)
    st.write(filtered_data)
else:
    st.warning("No data available for the selected date.")

# Defining all queries
queries = {
    "Total Expenses": """
        SELECT
            SUM(Amount) AS Total_Expense
        FROM
            Expense_tb;
    """,
    "Total number of transactions": """
        SELECT
        	COUNT(*) AS Total_transactions
        FROM
	        Expense_tb;
    """,
    "First and last transaction date": """
        SELECT
	        MIN(Date) AS First_transaction,
            MAX(Date) AS Last_transaction
        FROM 
	        Expense_tb;
    """,
    "Total, Avg, Min, Max Spending by Category": """
        SELECT
	        Category,
            SUM(Amount) AS Total_spent,
            Avg(Amount) AS Avg_spent,
            MAX(amount) AS Max_spent,
            MIN(amount) AS Min_spent
        FROM
	        Expense_tb
        GROUP BY
	        Category
        ORDER BY
	        Total_spent, Avg_spent, Max_spent, Min_spent;
    """,
    "Transactions Count by Category": """
        SELECT
            Category,
            COUNT(*) AS Total_trans
        FROM
	        Expense_tb
        GROUP BY
	        Category
        ORDER BY
	        Total_trans DESC;
    """,
    "Monthly Expenses": """
        SELECT
	        strftime('%Y-%m', Date) AS Month,
            SUM(Amount) AS Total_spent
        FROM
	        Expense_tb
        GROUP BY
	        strftime('%Y-%m', Date)
        ORDER BY
	        Month;
    """,
    "Daily Expenses": """
        SELECT
	        DATE(date) AS Day,
            SUM(amount) AS Total_expenses
        FROM
	        Expense_tb
        GROUP BY
	        DATE(date)
        ORDER BY
	        Day;
    """,
    "January month Expenses": """
        SELECT * FROM Expense_tb
        WHERE
	        strftime('%Y-%m', Date) = '2024-01'
        LIMIT 200;
    """,
    "Total cashback receive per month": """
        SELECT
	        strftime('%Y-%m', Date) AS Month,
            SUM(Cashback) AS Total_cashback
        FROM
	        Expense_tb
        GROUP BY
	        Month
        ORDER BY
	        Month;
    """,
    "Total cashback receive per day": """
        SELECT
	        Date,
            SUM(Cashback) AS Total_cashback
        FROM
	        Expense_tb
        GROUP BY
	        Date
        ORDER BY
	        Date;
    """,
    "Total, Avg, Min, Max spending by payment mode": """
        SELECT
            Payment_Mode,
	        SUM(Amount) AS Total_spent,
            Avg(Amount) AS Avg_spent,
            MAX(amount) AS Max_spent,
            MIN(amount) AS Min_spent
        FROM
	        Expense_tb
        GROUP BY
	        Payment_Mode
        ORDER BY
	        Total_spent, Avg_spent, Max_spent, Min_spent;
    """,
    "Count of transactions by payment mode": """
        SELECT
	        Payment_Mode, COUNT(*) AS Transaction_count
        FROM
	        Expense_tb
        GROUP BY
	        Payment_Mode
        ORDER BY
	        transaction_count DESC;
    """,
    "Total cashback receive": """
        SELECT
	        SUM(Cashback) AS Total_cashback
        FROM
	        Expense_tb;
    """,
    "Avg, Max, Min cashback receive in each transaction": """
        SELECT
	        AVG(Cashback) AS Avg_cashback,
            MAX(Cashback) AS Max_cashback,
            MIN(Cashback) AS Min_cashback
        FROM
	        Expense_tb;
    """,
    "Total cashback by payment mode": """
        SELECT
	        Payment_Mode,
	        SUM(Cashback) AS Total_cashback
        FROM
	        Expense_tb
        GROUP BY
	        Payment_Mode
        ORDER BY
	        total_cashback;
    """,
    "Total spending after cashback": """
        SELECT
        	SUM(Amount - Cashback) AS Total_spent_after_cashback
        FROM
	        Expense_tb;
    """,
    "Total spending after cashback for Each Category": """
        SELECT
	        Category,
	        SUM(Amount - Cashback) AS Total_spent_after_cashback
        FROM
	        Expense_tb
        GROUP BY
	        Category
        ORDER BY
	        Total_spent_after_cashback DESC;
    """,
    "Total cashback receive for each category": """
        SELECT
        	Category,
	        SUM(Cashback) AS Total_cashback
        FROM
	        Expense_tb
        GROUP BY
	        Category
        ORDER BY
        	total_cashback DESC;
    """,
    "Month-Wise Count of Transactions for Each Category": """
        SELECT 
            strftime('%Y-%m', Date) AS Month,
            Category,
            COUNT(*) AS Transaction_count
        FROM
	        Expense_tb
        GROUP BY
            Month, Category
        ORDER BY
	        Month,
            Transaction_count DESC;
    """,
    "Count of transactions by Description": """
        SELECT
        	Description,
            COUNT(*) AS Count
        FROM
            Expense_tb
        GROUP BY
	        Description
        ORDER BY
	        count DESC;
    """,
    "Category wise highest spending in each month": """
        SELECT 
            strftime('%Y-%m', Date) AS Month,
            Category,
            SUM(Amount) AS Total_spent
        FROM
	        Expense_tb
        GROUP BY
	        Month, Category
        ORDER BY
        	Month, Total_spent DESC;
    """
}

# Sidebar for query selection
st.sidebar.markdown("""---""")
st.sidebar.header("MySQL Query 🔍")
query_options = ["Select a query"] + list(queries.keys())
selected_query = st.sidebar.selectbox("Select a query to display:", options=query_options)

# Sidebar for chart selection
st.sidebar.markdown("---")
st.sidebar.header("Visualization 📊")
chart_options = [
    "Total, Avg, Min, Max Spending by Category",
    "Transactions Count by Category",
    "Monthly Expenses",
    "Daily Expenses",
    "Total cashback receive per month",
    "Total cashback receive per day",
    "Total, Avg, Min, Max spending by payment mode",
    "Total spending after cashback for Each Category",
    "Total cashback receive for each category",
    "Month-Wise Count of Transactions for Each Category",
    "Category wise highest spending in each month"
]
selected_charts = st.sidebar.multiselect("Select a query to display the corresponding chart:", options=chart_options)

# Displaying Query Results
if selected_query != "Select a query":
    query = queries[selected_query]
    df_query = pd.read_sql(query, conn)
    st.subheader(f"{selected_query}")
    st.dataframe(df_query)

# Displaying Charts
if "Total, Avg, Min, Max Spending by Category" in selected_charts:
    query = queries["Total, Avg, Min, Max Spending by Category"]
    df = pd.read_sql(query, conn)
    st.subheader("Spending by Category")
    fig = px.bar(df, x='Category', y=['Total_spent', 'Avg_spent', 'Max_spent', 'Min_spent'],          
             labels={'value': 'Amount', 'variable': 'Metric'}, 
             barmode='stack')
    st.plotly_chart(fig)

if "Transactions Count by Category" in selected_charts:
    query = queries["Transactions Count by Category"]
    df = pd.read_sql(query, conn)
    st.subheader("Transactions Count by Category")
    fig = px.pie(df, 
             names='Category', 
             values='Total_trans',
             color='Category')
    st.plotly_chart(fig)

if "Monthly Expenses" in selected_charts:
    query = queries["Monthly Expenses"]
    df = pd.read_sql(query, conn)
    st.subheader("Monthly Expenses")
    line_chart = px.line(df, x='Month', y='Total_spent', markers=True)
    st.plotly_chart(line_chart)

if "Daily Expenses" in selected_charts:
    query = queries["Daily Expenses"]
    df = pd.read_sql(query, conn)
    st.subheader("Daily Expenses")
    bar_chart = px.bar(df, x='Day', y='Total_expenses')
    st.plotly_chart(bar_chart)

if "Total cashback receive per month" in selected_charts:
    query = queries["Total cashback receive per month"]
    df = pd.read_sql(query, conn)
    st.subheader("Total cashback receive per month")
    fig = px.bar(df, x='Month', y='Total_cashback', 
             labels={'Total_cashback': 'Total Cashback', 'Month': 'Month'})
    st.plotly_chart(fig)

if "Total cashback receive per day" in selected_charts:
    query = queries["Total cashback receive per day"]
    df = pd.read_sql(query, conn)
    st.subheader("Total cashback receive per day")
    fig = px.area(df, x='Date', y='Total_cashback', 
             labels={'Total_cashback': 'Total Cashback', 'Date': 'Date'})
    st.plotly_chart(fig)

if "Total, Avg, Min, Max spending by payment mode" in selected_charts:
    query = queries["Total, Avg, Min, Max spending by payment mode"]
    df = pd.read_sql(query, conn)
    st.subheader("Spending by payment mode")
    fig = px.bar(df, x='Payment_Mode', y=['Total_spent', 'Avg_spent', 'Max_spent', 'Min_spent'],          
             labels={'Total_spent': 'Total Spent', 'Avg_spent': 'Average Spending',
                     'Max_spent': 'Maximum Spending', 'Min_spent': 'Minimum Spending'},
             barmode='stack')
    st.plotly_chart(fig)

if "Total spending after cashback for Each Category" in selected_charts:
    query = queries["Total spending after cashback for Each Category"]
    df = pd.read_sql(query, conn)
    st.subheader("Total spending after cashback for Each Category")
    fig = px.pie(df, names='Category', values='Total_spent_after_cashback')
    st.plotly_chart(fig)

if "Total cashback receive for each category" in selected_charts:
    query = queries["Total cashback receive for each category"]
    df = pd.read_sql(query, conn)
    st.subheader("Total cashback receive for each category")
    fig = px.bar(df, 
             x='Category', 
             y='Total_cashback', 
             color='Total_cashback', 
             color_continuous_scale='Viridis',
             labels={'Total_cashback': 'Cashback Amount'})
    st.plotly_chart(fig)

if "Month-Wise Count of Transactions for Each Category" in selected_charts:
    query = queries["Month-Wise Count of Transactions for Each Category"]
    df = pd.read_sql(query, conn)
    st.subheader("Month-Wise Count of Transactions for Each Category")
    fig = px.bar(df, 
              x='Month', 
              y='Transaction_count', 
              color='Category',
              labels={'Transaction_count': 'Transaction Count', 'Month': 'Month'},
              barmode='group')
    st.plotly_chart(fig)

if "Category wise highest spending in each month" in selected_charts:
    query = queries["Category wise highest spending in each month"]
    df = pd.read_sql(query, conn)
    st.subheader("Category wise highest spending in each month")
    fig = px.bar(df, 
              x='Month', 
              y='Total_spent', 
              color='Category',
              labels={'Total_spent': 'Total_spending', 'Month': 'Month'},
              barmode='stack')
    st.plotly_chart(fig)
