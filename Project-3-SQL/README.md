# Project 3: SQL Data Analysis

##  Overview
This project uses SQL queries to analyze an Orders dataset and extract meaningful insights from 1000 records.

##  Objective
The goal of this project is to practice SQL fundamentals and perform data analysis using various SQL operations.

##  Dataset
- Dataset: Orders dataset
- Number of records: 1000 rows
- Contains information such as:
  - Order ID
  - Customer ID
  - Product
  - Quantity
  - Unit Price
  - Order Status
  - Total Price

##  Tools Used
- SQL
- SQLite Online IDE
- GitHub

##  SQL Queries Performed

### 1. Display First 10 Rows
```sql
SELECT * FROM Orders
LIMIT 10;
```

### 2. Count Total Orders
```sql
SELECT COUNT(*) AS TotalOrders
FROM Orders;
```

### 3. Calculate Average Unit Price
```sql
SELECT AVG(c6) AS AverageUnitPrice
FROM Orders;
```

### 4. Orders by Status
```sql
SELECT c9, COUNT(*) AS Count
FROM Orders
GROUP BY c9
ORDER BY Count DESC;
```

### 5. Most Sold Products
```sql
SELECT c4, COUNT(*) AS TotalSold
FROM Orders
GROUP BY c4
ORDER BY TotalSold DESC;
```

### 6. Calculate Total Revenue
```sql
SELECT SUM(c14) AS TotalRevenue
FROM Orders;
```

### 7. Retrieve High-Value Orders
```sql
SELECT *
FROM Orders
WHERE c14 > 1000
ORDER BY c14 DESC;
```

##  SQL Concepts Used
- SELECT
- WHERE
- ORDER BY
- GROUP BY
- COUNT()
- AVG()
- SUM()


##  Author
Tejaswini B

DecodeLabs Internship Project
