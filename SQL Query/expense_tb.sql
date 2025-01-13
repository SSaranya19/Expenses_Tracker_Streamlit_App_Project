SELECT * FROM expenses_db.expense_tb;
USE expenses_db;
SELECT * FROM expense_tb LIMIT 2400;

-- 1. What is the total expenses?
SELECT
	SUM(Amount) AS Total_Expense
FROM
	expense_tb;

-- 2. What is the total number of transactions?
SELECT
	COUNT(*) AS Total_transactions
FROM
	expense_tb;

-- 3. What are the first and last transaction dates?
SELECT
	MIN(Date) AS First_transaction,
    MAX(Date) AS Last_transaction
FROM 
	expense_tb;

-- 4. What are the total, average, minimum, and maximum spending by category?
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

-- 5. What is the count of transactions by category?
SELECT
	Category,
    COUNT(*) AS Total_trans
FROM
	expense_tb
GROUP BY
	Category
ORDER BY
	total_trans DESC;

-- 6. What are the monthly expenses?
SELECT
	DATE_FORMAT(Date, '%Y-%m') AS month,
    SUM(Amount) AS Total_spent
FROM
	expense_tb
GROUP BY
	DATE_FORMAT(Date, '%Y-%m')
ORDER BY
	month;

-- 7. What are the daily expenses?
SELECT
	DATE(date) AS Day,
    SUM(amount) AS Total_expenses
FROM
	expense_tb
GROUP BY
	DATE(date)
ORDER BY
	day;

-- 8. What are the expenses for January?
SELECT * FROM expense_tb
WHERE
	DATE_FORMAT(Date, '%Y-%m') = '2024-01'
LIMIT 200;

-- 9. What is the total cashback received per month?
SELECT
	DATE_FORMAT(Date, '%Y-%m') AS Month,
    SUM(Cashback) AS Total_cashback
FROM
	expense_tb
GROUP BY
	Month
ORDER BY
	Month;

-- 10. What is the total cashback received per day?
SELECT
	Date,
    SUM(Cashback) AS Total_cashback
FROM
	expense_tb
GROUP BY
	Date
ORDER BY
	Date;

-- 11. What are the total, average, minimum, and maximum spending by payment mode?
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

-- 12. What is the count of transactions by payment mode?
SELECT
	Payment_Mode, COUNT(*) AS Transaction_count
FROM
	expense_tb
GROUP BY
	Payment_Mode
ORDER BY
	transaction_count DESC;

-- 13. What is the total cashback received?
SELECT
	SUM(Cashback) AS total_cashback
FROM
	expense_tb;

-- 14. What are the average, maximum, and minimum cashback amounts received in each transaction?
SELECT
	AVG(Cashback) AS Avg_cashback,
    MAX(Cashback) AS Max_cashback,
    MIN(Cashback) AS Min_cashback
FROM
	expense_tb;

-- 15. What is the total cashback received by payment mode?
SELECT
	Payment_Mode,
	SUM(Cashback) AS Total_cashback
FROM
	expense_tb
GROUP BY
	Payment_Mode
ORDER BY
	total_cashback;

-- 16. What is the total spending after cashback?
SELECT
	SUM(Amount - Cashback) AS Total_spent_after_cashback
FROM
	expense_tb;

-- 17. What is the total spending after cashback for each category?
SELECT
	Category,
	SUM(Amount - Cashback) AS Total_spent_after_cashback
FROM
	expense_tb
GROUP BY
	Category
ORDER BY
	Total_spent_after_cashback DESC;

-- 18. What is the total cashback received for each category?
SELECT
	Category,
	SUM(Cashback) AS Total_cashback
FROM
	expense_tb
GROUP BY
	Category
ORDER BY
	total_cashback DESC;

-- 19. What is the month-wise count of transactions for each category?
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

-- 20. What is the count of transactions by description?
SELECT
	Description,
    COUNT(*) AS count
FROM expense_tb
GROUP BY
	Description
ORDER BY
	count DESC;

-- 21. What is the category-wise highest spending per month?
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