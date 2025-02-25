
# Analyzing Personal Expenses 💸

## Project Overview
This project simulates an expense tracker for individuals using Python, SQL, and Streamlit. It generates realistic monthly expense data through the Faker library, processes it, and stores it in a SQL database. The insights derived from SQL queries are then visualized through an interactive Streamlit application, helping users track their spending patterns across categories like bills, groceries, subscriptions, and personal spending.

## Domain 🌐
- **Personal Finance** and **Expense Tracking**

## Problem Statement
The goal of this project is to create a tool for tracking and analyzing personal expenses over the course of a year. By simulating a realistic dataset using the Faker library, the project:
- Generates monthly transaction data,
- Stores it in a SQL database,
- Uses SQL queries to uncover spending insights, and
- Displays the results through an easy-to-use Streamlit app.

The project provides an overview of monthly spending trends and helps individuals (or businesses) understand their financial habits, making it easier to optimize their spending and identify potential savings opportunities.

## Business Use Cases 💼
- **Automating Expense Tracking**: Streamline the process of tracking personal or business expenses, especially for e-commerce platforms.
- **Analyzing Spending Habits**: Categorize spending and offer actionable insights to help users create savings plans.
- **Financial Dashboards**: Build custom dashboards for visualizing income and expenses trends.
- **Business Insights**: Help businesses track procurement and inventory spending patterns.

## Data Set Explanation 📊
The dataset simulates an individual’s expenses with the following attributes:

| Field          | Description                                                |
|----------------|------------------------------------------------------------|
| **Date**       | Transaction date                                           |
| **Category**   | Type of expense (e.g., Food, Transportation, Bills)        |
| **Payment Mode** | Cash or Online transaction                                |
| **Description** | Details about the expense (e.g., "Grocery shopping")       |
| **Amount Paid** | Total amount spent in the transaction                     |
| **Cashback**   | Cashback or rewards received, if any                      |

### Key Preprocessing Steps:
- **Realistic Date Ranges**: Ensure transactions span across different months of the year.
- **Accurate Categorization**: Properly assign expenses to the correct categories (e.g., bills, transportation, groceries).
- **Structured Data**: Format data for seamless querying and visualization.

## Approach 🛠️
1. **Data Simulation**: Use the Faker library to generate realistic data for each month of the year, creating 12 different tables (one for each month).
2. **Database Creation**: Set up a SQL database schema and load the simulated data for querying.
3. **Exploratory Data Analysis (EDA)**: Analyze the dataset using Python libraries (e.g., Pandas, Matplotlib) to derive insights.
4. **Streamlit App**: Build a user-friendly web app to showcase visualizations and SQL query outputs.
5. **Insights & Recommendations**: Offer actionable insights based on the analysis of spending patterns.

## Key Questions to Answer 🤔
The project answers 15 core questions related to spending habits, and encouraged to create my own set of 10-15 additional queries.

## Results and Deliverables 🏆
- **Streamlit App**: A fully functional app showcasing visualizations and the outputs of the 20+ SQL queries.
- **Insights**: Clear identification of spending trends and actionable takeaways for optimizing expenses.
- **Data-driven Recommendations**: Tips for improving financial habits based on simulated data analysis.

## Technical Tags 🔧
- Python
- SQL
- Streamlit
- EDA (Exploratory Data Analysis)
- Financial Analysis
- Data Visualization
- Expense Tracking

## Project Deliverables 📂
- **Source Code**: Python scripts for data cleaning, SQL queries, and Streamlit app development.
- **SQL Scripts**: All 20 queries (including 15 essential ones and my own additional queries).
- **Documentation**: A detailed explanation of the methodology, analysis, and insights derived from the data.
- **Streamlit App Screenshots**: Visual proof of the app with key visualizations and outputs.
- **Streamlit App Link**: https://expenses-tracker-app-project.streamlit.app/

## Skills Gained 🎓
- **Python**: Data manipulation, analysis, and simulation.
- **SQL**: Data storage, querying, and insights extraction.
- **Streamlit**: Building interactive dashboards for visualizations.

---

By completing this project, you'll gain hands-on experience with a real-world use case in personal finance tracking, and learn how to combine data simulation, database management, and web development to build an insightful financial dashboard. 🚀
