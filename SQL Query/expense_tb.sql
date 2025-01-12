SELECT * FROM expenses_db.expense_tb;
USE expenses_db;
SELECT * FROM expense_tb LIMIT 2400;

-- 1. Total Expenses
SELECT
	SUM(Amount) AS Total_Expense
FROM
	expense_tb;

-- 2. Total number of transactions:
SELECT
	COUNT(*) AS Total_transactions
FROM
	expense_tb;

-- 3. First and last transaction date:
SELECT
	MIN(Date) AS First_transaction,
    MAX(Date) AS Last_transaction
FROM 
	expense_tb;

-- 4. Total, Avg, Min, Max Spending by Category:
SELECT
	Category,
    SUM(Amount) AS Total_spent,
    Avg(Amount) AS Avg_spent,
    MAX(amount) AS Max_spent,
    MIN(amount) AS Min_spent
FROM
	expense_tb
GROUP BY
	Category
ORDER BY
	Total_spent, Avg_spent, Max_spent, Min_spent;

-- 5. Transactions Count by Category:
SELECT
	Category,
    COUNT(*) AS Total_trans
FROM
	expense_tb
GROUP BY
	Category
ORDER BY
	total_trans DESC;

-- 6. Monthly Expenses:
SELECT
	DATE_FORMAT(Date, '%Y-%m') AS month,
    SUM(Amount) AS Total_spent
FROM
	expense_tb
GROUP BY
	DATE_FORMAT(Date, '%Y-%m')
ORDER BY
	month;

-- 7. Daily Expenses:
SELECT
	DATE(date) AS Day,
    SUM(amount) AS Total_expenses
FROM
	expense_tb
GROUP BY
	DATE(date)
ORDER BY
	day;

-- 8. January month Expenses:
SELECT * FROM expense_tb
WHERE
	DATE_FORMAT(Date, '%Y-%m') = '2024-01'
LIMIT 200;

-- 9. Total cashback receive per month:
SELECT
	DATE_FORMAT(Date, '%Y-%m') AS Month,
    SUM(Cashback) AS Total_cashback
FROM
	expense_tb
GROUP BY
	Month
ORDER BY
	Month;

-- 10. Total cashback receive per day:
SELECT
	Date,
    SUM(Cashback) AS Total_cashback
FROM
	expense_tb
GROUP BY
	Date
ORDER BY
	Date;

-- 11. Total, Avg, Min, Max spending by payment mode:
SELECT
	Payment_Mode,
	SUM(Amount) AS Total_spent,
    Avg(Amount) AS Avg_spent,
    MAX(amount) AS Max_spent,
    MIN(amount) AS Min_spent
FROM
	expense_tb
GROUP BY
	Payment_Mode
ORDER BY
	Total_spent, Avg_spent, Max_spent, Min_spent;

-- 12. Count of transactions by payment mode:
SELECT
	Payment_Mode, COUNT(*) AS Transaction_count
FROM
	expense_tb
GROUP BY
	Payment_Mode
ORDER BY
	transaction_count DESC;

-- 13. Total cashback receive:
SELECT
	SUM(Cashback) AS total_cashback
FROM
	expense_tb;

-- 14. Avg, Max, Min cashback receive in each transaction:
SELECT
	AVG(Cashback) AS Avg_cashback,
    MAX(Cashback) AS Max_cashback,
    MIN(Cashback) AS Min_cashback
FROM
	expense_tb;

-- 15. Total cashback by payment mode:
SELECT
	Payment_Mode,
	SUM(Cashback) AS Total_cashback
FROM
	expense_tb
GROUP BY
	Payment_Mode
ORDER BY
	total_cashback;

-- 16. Total spending after cashback:
SELECT
	SUM(Amount - Cashback) AS Total_spent_after_cashback
FROM
	expense_tb;

-- 17. Total spending after cashback for Each Category:
SELECT
	Category,
	SUM(Amount - Cashback) AS Total_spent_after_cashback
FROM
	expense_tb
GROUP BY
	Category
ORDER BY
	Total_spent_after_cashback DESC;

-- 18. Total cashback receive for each category:
SELECT
	Category,
	SUM(Cashback) AS Total_cashback
FROM
	expense_tb
GROUP BY
	Category
ORDER BY
	total_cashback DESC;

-- 19. Month-Wise Count of Transactions for Each Category:
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    Category,
    COUNT(*) AS Transaction_count
FROM
	expense_tb
GROUP BY
    Month, Category
ORDER BY
	Month,
    Transaction_count DESC;

-- 20. Count of transactions by Description:
SELECT
	Description,
    COUNT(*) AS count
FROM expense_tb
GROUP BY
	Description
ORDER BY
	count DESC;

-- 21. Category wise highest spending in each month:
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    Category,
    SUM(Amount) AS Total_spent
FROM
	expense_tb
GROUP BY
	Month, Category
ORDER BY
	Month, Total_spent DESC;