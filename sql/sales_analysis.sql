-- 1. Total sales by region
SELECT Region, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region;

-- 2. Total profit by category
SELECT Category, SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category;

-- 3. Monthly sales trend
SELECT 
    MONTH(`Order Date`) AS Month,
    SUM(Sales) AS Monthly_Sales
FROM superstore
GROUP BY Month
ORDER BY Month;

-- 4. Top 10 customers by sales
SELECT 
    `Customer Name`,
    SUM(Sales) AS Total_Spent
FROM superstore
GROUP BY `Customer Name`
ORDER BY Total_Spent DESC
LIMIT 10;

-- 5. Loss-making sub-categories
SELECT 
    `Sub-Category`,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Sub-Category`
HAVING SUM(Profit) < 0;
