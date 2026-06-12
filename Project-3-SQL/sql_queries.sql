--Query 1: Show first 10 rows
SELECT * FROM Orders LIMIT 10;

-- Query 2: Count total orders
SELECT COUNT(*) AS TotalOrders FROM Orders;

-- Query 3: Average unit price
SELECT AVG(c6) AS AverageUnitPrice FROM Orders;

-- Query 4: Orders by status
SELECT c9, COUNT(*) AS Count 
FROM Orders 
GROUP BY c9 
ORDER BY Count DESC;

-- Query 5: Most sold products
SELECT c4, COUNT(*) AS TotalSold 
FROM Orders 
GROUP BY c4 
ORDER BY TotalSold DESC;

-- Query 6: Total revenue
SELECT SUM(c14) AS TotalRevenue FROM Orders;

-- Query 7: High value orders
SELECT * FROM Orders 
WHERE c14 > 1000 
ORDER BY c14 DESC;