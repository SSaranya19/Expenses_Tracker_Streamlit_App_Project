SELECT * FROM expenses_db.expense_tb;
USE expenses_db;
SELECT * FROM expense_tb LIMIT 2400;

-- What is the total amount spent in each category?
Select
	Category, sum(Amount) As Total_spent
From
	expense_tb
Group by
	Category
Order by
	Total_spent;

-- What is the total amount spent using each payment mode?
Select
	Payment_Mode, sum(Amount) As Total_spent
From
	expense_tb
Group by
	Payment_Mode
Order by
	Total_spent;

-- What is the total cashback received across all transactions?
Select
	sum(Cashback) As Total_cashback
From
	expense_tb;

-- Which are the top 5 most expensive categories in terms of spending?
Select
	Category, sum(Amount) As Total_spent
From
	expense_tb
Group by
	Category
Order by
	Total_spent Desc
Limit 5;

-- How much was spent on transportation using different payment modes?
Select
	Payment_mode, SUM(Amount) AS Total_Spent_Transport
From
	expense_tb
Where
	Category = 'Transportation'
Group By
	Payment_Mode
Order by
	Total_Spent_Transport desc;

-- Which transactions resulted in cashback?
Select
	Category, Payment_mode, Description, Amount, Cashback
From
	expense_tb
Where Cashback > 0;

-- What is the total spending in each month of the year?
Select
    DATE_FORMAT(Date, '%Y-%m') As Year_of_Month,
    SUM(Amount) As Total_Spent
From
    expense_tb
Group by 
    Year_of_Month;

-- Which months have the highest spending in categories like "Travel," "Entertainment," or "Gifts"?
Select 
    DATE_FORMAT(Date, '%Y-%m') AS YearMonth,
    Category,
    SUM(Amount) AS Total_Spent
From 
    expense_tb
Where 
    Category IN ('Shopping', 'Entertainment', 'Transportation')
Group by 
    YearMonth, Category
Order by 
    YearMonth, Total_Spent DESC;

-- How much cashback or rewards were earned in each month?
Select
	DATE_FORMAT(Date, '%Y-%m') AS Month,
    SUM(Cashback) AS Total_cashback
From
	expense_tb
Group by
	Month
Order by
	Month;

-- How has your overall spending changed over time (e.g., increasing, decreasing, remaining stable)?
Select
    DATE_FORMAT(Date, '%Y-%m') AS Year_of_Month,
    SUM(Amount) AS Total_Spent
From
    expense_tb
Group by
    Year_of_Month
Order by
    Year_of_Month;
    
-- Are there any patterns in grocery spending (e.g., higher spending on weekends, increased spending during specific seasons)?

-- Monthly Breakdown in grocery spending
Select
    DATE_FORMAT(Date, '%m') AS Month,
    SUM(Amount) AS Total_Spent
From
    expense_tb
Where Category = 'Groceries'
Group by
    Month
Order by
    Total_Spent desc;
    
-- Days of the week and any specific seasons variation.
Select
    DATE_FORMAT(Date, '%w') AS Day_of_Week,
    DATE_FORMAT(Date, '%m') AS Month,
    SUM(Amount) AS Total_Spent
From
    expense_tb
Where Category = 'Groceries' AND DATE_FORMAT(Date, '%m') IN ('06', '07', '08')
Group by
    Day_of_Week, Month
Order by
    Day_of_Week, Month, Total_Spent desc;

-- Define High and Low Priority Categories
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
    Priority, Total_Spent Desc;

-- Which category contributes the highest percentage of the total spending?
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
Limit 1;