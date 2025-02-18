import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime, date
import plotly.express as px # type: ignore

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
    "What is the total expenses?": """
        SELECT
            SUM(Amount) AS Total_Expense
        FROM
            Expense_tb;
    """,
    "What is the total number of transactions?": """
        SELECT
        	COUNT(*) AS Total_transactions
        FROM
	        Expense_tb;
    """,
    "What are the first and last transaction dates?": """
        SELECT
	        MIN(Date) AS First_transaction,
            MAX(Date) AS Last_transaction
        FROM 
	        Expense_tb;
    """,
    "What are the total, average, minimum, and maximum spending by category?": """
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
    "What is the count of transactions by category?": """
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
    "What are the monthly expenses?": """
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
    "What are the daily expenses?": """
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
    "What are the expenses for January?": """
        SELECT * FROM Expense_tb
        WHERE
	        strftime('%Y-%m', Date) = '2024-01'
        LIMIT 200;
    """,
    "What is the total cashback received per month?": """
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
    "What is the total cashback received per day?": """
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
    "What are the total, average, minimum, and maximum spending by payment mode?": """
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
    "What is the count of transactions by payment mode?": """
        SELECT
	        Payment_Mode, COUNT(*) AS Transaction_count
        FROM
	        Expense_tb
        GROUP BY
	        Payment_Mode
        ORDER BY
	        transaction_count DESC;
    """,
    "What is the total cashback received?": """
        SELECT
	        SUM(Cashback) AS Total_cashback
        FROM
	        Expense_tb;
    """,
    "What are the average, maximum, and minimum cashback amounts received in each transaction?": """
        SELECT
	        AVG(Cashback) AS Avg_cashback,
            MAX(Cashback) AS Max_cashback,
            MIN(Cashback) AS Min_cashback
        FROM
	        Expense_tb;
    """,
    "What is the total cashback received by payment mode?": """
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
    "What is the total spending after cashback?": """
        SELECT
        	SUM(Amount - Cashback) AS Total_spent_after_cashback
        FROM
	        Expense_tb;
    """,
    "What is the total spending after cashback for each category?": """
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
    "What is the total cashback received for each category?": """
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
    "What is the month-wise count of transactions for each category?": """
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
    "What is the count of transactions by description?": """
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
    "What is the category-wise highest spending per month?": """
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
    """,
    "What is the total amount spent in each category?": """
        Select
	        Category, sum(Amount) As Total_spent
        From
	        expense_tb
        Group by
	        Category
        Order by
	        Total_spent;""",
    "What is the total amount spent using each payment mode?": """
        Select
	        Payment_Mode, sum(Amount) As Total_spent
        From
	        expense_tb
        Group by
	        Payment_Mode
        Order by
	        Total_spent;""",

    "What is the total cashback received across all transactions?": """
        Select
	        sum(Cashback) As Total_cashback
        From
	        expense_tb;""",

    "Which are the top 5 most expensive categories in terms of spending?": """
        Select
	        Category, sum(Amount) As Total_spent
        From
	        expense_tb
        Group by
	        Category
        Order by
	        Total_spent Desc
        Limit 5;""",

    "How much was spent on transportation using different payment modes?": """
        Select
	        Payment_mode, SUM(Amount) AS Total_Spent_Transport
        From
	        expense_tb
        Where
	        Category = 'Transportation'
        Group By
	        Payment_Mode
        Order by
	        Total_Spent_Transport desc;""",

    "Which transactions resulted in cashback?": """
        Select
	        Category, Payment_mode, Description, Amount, Cashback
        From
	        expense_tb
        Where Cashback > 0;""",

    "What is the total spending in each month of the year?": """
        Select
            strftime('%Y-%m', Date) As Year_of_Month,
            SUM(Amount) As Total_Spent
        From
            expense_tb
        Group by 
            Year_of_Month;""",
    "Which months have the highest spending in categories like 'Travel,' 'Entertainment,' or 'Gifts'?": """
        Select 
            strftime('%Y-%m', Date) AS YearMonth,
            Category,
            SUM(Amount) AS Total_Spent
        From 
            expense_tb
        Where 
            Category IN ('Shopping', 'Entertainment', 'Transportation')
        Group by 
            YearMonth, Category
        Order by 
            YearMonth, Total_Spent DESC;""",
    "How much cashback or rewards were earned in each month?": """
        Select
	        strftime('%Y-%m', Date) AS Month,
            SUM(Cashback) AS Total_cashback
        From
	        expense_tb
        Group by
	        Month
        Order by
	        Month;""",
    "How has your overall spending changed over time (e.g., increasing, decreasing, remaining stable)?": """
        Select
            strftime('%Y-%m', Date) AS Year_of_Month,
            SUM(Amount) AS Total_Spent
        From
            expense_tb
        Group by
            Year_of_Month
        Order by
            Year_of_Month;""",
    "Define High and Low Priority Categories":"""
        Select
	        Category,
            SUM(Amount) AS Total_Spent,
            Case
                When Category In ('Groceries', 'Transportation', 'Medical Health', 'Investment') Then 'High'
                When Category In ('Entertainment', 'Food', 'Shopping') Then 'Low'
                else 'Medium'
            End AS Priority
        From
            expense_tb
        Group by
            Category
        Order by
            Priority, Total_Spent Desc;""",
    "Which category contributes the highest percentage of the total spending?": """
        Select
            Category,
            SUM(Amount) AS Total_Spent,
            (SUM(Amount) * 100.0 / (SELECT SUM(Amount) FROM expense_tb)) AS Percentage_of_Total
        From
            expense_tb
        Group by
            Category
        Order by 
            Percentage_of_Total Desc
        Limit 1;"""
}

# Sidebar for query selection
st.sidebar.markdown("""---""")
st.sidebar.header("MySQL Query 🔍")
query_options = ["Select a query"] + list(queries.keys())
selected_query = st.sidebar.selectbox("Select a query to display:", options=query_options)

# Displaying Query Results
if selected_query != "Select a query":
    query = queries[selected_query]
    df_query = pd.read_sql(query, conn)
    st.subheader(f"Query: {selected_query}")
    st.dataframe(df_query)

# Sidebar for chart selection
st.sidebar.markdown("---")
st.sidebar.header("Visualization 📊")
chart_options = [
    "What are the total, average, minimum, and maximum spending by category?",
    "What is the count of transactions by category?",
    "What are the monthly expenses?",
    "What are the daily expenses?",
    "What is the total cashback received per month?",
    "What is the total cashback received per day?",
    "What are the total, average, minimum, and maximum spending by payment mode?",
    "What is the total spending after cashback for each category?",
    "What is the total cashback received for each category?",
    "What is the month-wise count of transactions for each category?",
    "What is the category-wise highest spending per month?",
    "What is the total amount spent in each category?",
    "What is the total amount spent using each payment mode?",
    #"Q3. What is the total cashback received across all transactions?",
    "Which are the top 5 most expensive categories in terms of spending?",
    "How much was spent on transportation using different payment modes?",
    "Which transactions resulted in cashback?",
    "What is the total spending in each month of the year?",
    "Which months have the highest spending in categories like 'Travel,' 'Entertainment,' or 'Gifts'?",
    "How much cashback or rewards were earned in each month?",
    "How has your overall spending changed over time (e.g., increasing, decreasing, remaining stable)?",
    "Define High and Low Priority Categories",
    #"Q12. Which category contributes the highest percentage of the total spending?"
]
selected_charts = st.sidebar.multiselect("Select a query to display charts:", options=chart_options)

# Displaying Charts based on selected headers
for chart in selected_charts:
    query = queries[chart]
    df = pd.read_sql(query, conn)
    
# Displaying Charts 
    if chart == "What are the total, average, minimum, and maximum spending by category?":
        st.subheader("Total, Avg, Max, Min Spending by Category")
        fig = px.bar(df, x='Category', y=['Total_spent', 'Avg_spent', 'Max_spent', 'Min_spent'],          
             labels={'value': 'Amount', 'variable': 'Metric'}, 
             barmode='stack')
        st.plotly_chart(fig)  
    
    if chart == "What is the count of transactions by category?":
        st.subheader("Transactions Count by Category")
        fig = px.pie(df, 
             names='Category', 
             values='Total_trans',
             color='Category')
        st.plotly_chart(fig)
    
    if chart == "What are the monthly expenses?":
        st.subheader("Monthly Expenses")
        line_chart = px.line(df, x='Month', y='Total_spent', markers=True)
        st.plotly_chart(line_chart)
    
    if chart == "What are the daily expenses?":
        st.subheader("Daily Expenses")
        bar_chart = px.bar(df, x='Day', y='Total_expenses')
        st.plotly_chart(bar_chart)
    
    if chart == "What is the total cashback received per month?":
        st.subheader("Total cashback receive per month")
        fig = px.bar(df, x='Month', y='Total_cashback', 
             labels={'Total_cashback': 'Total Cashback', 'Month': 'Month'})
        st.plotly_chart(fig)
    
    if chart == "What is the total cashback received per day?":
        st.subheader("Total cashback receive per day")
        fig = px.area(df, x='Date', y='Total_cashback', 
             labels={'Total_cashback': 'Total Cashback', 'Date': 'Date'})
        st.plotly_chart(fig)
    
    if chart == "What are the total, average, minimum, and maximum spending by payment mode?":
        st.subheader("Total, Average, Minimum, and Maximum Spending by payment mode")
        fig = px.bar(df, x='Payment_Mode', y=['Total_spent', 'Avg_spent', 'Max_spent', 'Min_spent'],          
             labels={'Total_spent': 'Total Spent', 'Avg_spent': 'Average Spending',
                     'Max_spent': 'Maximum Spending', 'Min_spent': 'Minimum Spending'},
             barmode='stack')
        st.plotly_chart(fig)
    
    if chart == "What is the total spending after cashback for each category?":
        st.subheader("Total spending after cashback for Each Category")
        fig = px.pie(df, names='Category', values='Total_spent_after_cashback')
        st.plotly_chart(fig)
    
    if chart == "What is the total cashback received for each category?":
        st.subheader("Total cashback receive for each category")
        fig = px.bar(df, 
             x='Category', 
             y='Total_cashback', 
             color='Total_cashback', 
             color_continuous_scale='Viridis',
             labels={'Total_cashback': 'Cashback Amount'})
        st.plotly_chart(fig)
    
    if chart == "What is the month-wise count of transactions for each category?":
        st.subheader("Month-Wise Count of Transactions for Each Category")
        fig = px.bar(df, 
              x='Month', 
              y='Transaction_count', 
              color='Category',
              labels={'Transaction_count': 'Transaction Count', 'Month': 'Month'},
              barmode='group')
        st.plotly_chart(fig)
    
    if chart == "What is the category-wise highest spending per month?":
        st.subheader("Category wise highest spending in each month")
        fig = px.bar(df, 
              x='Month', 
              y='Total_spent', 
              color='Category',
              labels={'Total_spent': 'Total_spending', 'Month': 'Month'},
              barmode='stack')
        st.plotly_chart(fig)

    if chart == "What is the total amount spent in each category?":
        st.subheader("Total Amount Spent in Each Category")
        fig = px.bar(df, x='Category', y='Total_spent',
                 labels={'value': 'Amount', 'Category': 'Category'})
        st.plotly_chart(fig)

    if chart == "What is the total amount spent using each payment mode?":
        st.subheader("Total Amount Spent by Payment Mode")
        fig = px.pie(df,
                 names='Payment_Mode',
                 values='Total_spent',
                 color='Payment_Mode')
        st.plotly_chart(fig)

    if chart == "Which are the top 5 most expensive categories in terms of spending?":
        st.subheader("Top 5 Most Expensive Categories")
        fig = px.bar(df, x='Total_spent', y='Category',
                 orientation='h',
                 labels={'Total_spent': 'Total Spending', 'Category': 'Category'})
        st.plotly_chart(fig)

    if chart == "How much was spent on transportation using different payment modes?":
        st.subheader("Spending on Transportation by Payment Mode")
        fig = px.bar(df, x='Payment_Mode', y='Total_Spent_Transport',
                 labels={'Total_Spent_Transport': 'Amount Spent', 'Payment_Mode': 'Payment Mode'})
        st.plotly_chart(fig)

    if chart == "Which transactions resulted in cashback?":
        st.subheader("Transactions resulted in Cashback")
        fig = px.density_heatmap(df, x='Category', y='Payment_Mode', z='Cashback',
                             color_continuous_scale='Viridis', 
                             labels={'Category': 'Category', 'Payment_mode': 'Payment Mode', 'Cashback': 'Cashback Amount'})
        st.plotly_chart(fig)

    if chart == "What is the total spending in each month of the year?":
        st.subheader("Monthly Spending")
        fig = px.line(df, x='Year_of_Month', y='Total_Spent',
                  labels={'Year_of_Month': 'Month', 'Total_Spent': 'Spending'},
                  markers=True)
        st.plotly_chart(fig)

    if chart == "Which months have the highest spending in categories like 'Travel,' 'Entertainment,' or 'Gifts'?":
        st.subheader("Highest Spending in Categories like 'Entertainment', 'Shopping', 'Transportation'")
        fig = px.bar(df, x='YearMonth', y='Total_Spent',
                 color='Category',
                 barmode='group',
                 labels={'YearMonth': 'Month', 'Total_Spent': 'Spending', 'Category': 'Category'})
        st.plotly_chart(fig)

    if chart == "How much cashback or rewards were earned in each month?":
        st.subheader("Monthly Cashback/Rewards")
        fig = px.line(df, x='Month', y='Total_cashback',
                  labels={'Month': 'Month', 'Total_cashback': 'Cashback'},
                  markers=True)
        st.plotly_chart(fig)

    if chart == "How has your overall spending changed over time (e.g., increasing, decreasing, remaining stable)?":
        st.subheader("Overall Spending Trend")
        fig = px.line(df, x='Year_of_Month', y='Total_Spent',
                  labels={'Year_of_Month': 'Month', 'Total_Spent': 'Spending'},
                  markers=True)
        st.plotly_chart(fig)

    if chart == "Define High and Low Priority Categories":
        st.subheader("Spending by Priority Categories")
        fig = px.bar(df, x='Category', y='Total_Spent',
                 color='Priority',
                 labels={'Total_Spent': 'Spending', 'Category': 'Category', 'Priority': 'Priority'})
        st.plotly_chart(fig)
