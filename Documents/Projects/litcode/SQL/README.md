# SQL Practice
pgadmin download: https://www.postgresql.org/ftp/pgadmin/pgadmin4/v4.6/macos/

Host: ec2-54-245-31-214.us-west-2.compute.amazonaws.com
Port: 5291
User (Role): sqlpractice - only has select privileges.
Password: iloveSQL!
Database: ecommerce

## Practice Questions

### Easy Problems
**1. Return All fields for all shippers from Shippers table. (3 rows)**  
SELECT * FROM Shippers

**2. Return CategoryName and Description columns from Categories table. (8 rows)**  
SELECT CategoryName, Description from Categories   

**3. Return FirstName, LastName and HireDate fields for employees where the Title is "Sales Representative" from Employees table. (7 rows)**  
SELECT title, FirstName, LastNAme, HireDate FROM employees  
WHERE title='Sales Representative'   

**4. Return same fields for the same Title as in problem 3, but only for employees from the United States. (3 rows)**  
SELECT FirstName, LastName, HireDate FROM employees  
WHERE title='Sales Representative' AND country='USA'   

**5. Show all Orders placed by specific employee (Steven Buchanan) EmployeeID is 5. (42 rows)**  
SELECT * FROM Orders  
WHERE employeeid = 5   

**6. Show SupplierID, ContactName and ContactTitle from Suppliers table where ContactTitle is not(!) Marketing Manager. (24 rows)**   
SELECT SupplierID, ContactName, ContactTitle FROM Suppliers  
WHERE ContactTitle != 'Marketing Manager'   

**7. Show ProductID and ProductName from Products table where the ProductName includes 'Queso'. (2 rows)**  
SELECT ProductID, ProductName FROM Products  
WHERE ProductName LIKE '%ueso%'   

**8. Show OrderID, CustomerID and ShipCountry for Orders shipping to France or Belgium. (96 rows)**  
SELECT OrderID, CustomerID, ShipCountry from Orders   
WHERE ShipCountry = 'France' OR ShipCountry = 'Belgium'   

**9. Select OrderID, CustomerID and ShipCountry for Orders shipping to Brazil, Mexico, Argentina, Venezuela (Latin America). (173 rows). Use 'in' instead of multiple OR.**   
SELECT OrderID, CustomerID, ShipCountry from Orders  
WHERE ShipCountry IN ('Brazil', 'Mexico', 'Argentina', 'Venezuela')   

**10. Select FirstName, LastName, Title and BirthDate for Employees ordered by BirthDate. (9 rows)**    
SELECT FirstName, LastName, Title, BirthDate from Employees   
ORDER BY BirthDate   

**11. Select FirstName, LastName, Title and BirthDate for Employees ordered by BirthDate, but show only date for BirthDate without time.**   
SELECT FirstName, LastName, Title, date(BirthDate) from Employees   
ORDER BY BirthDate   

**12.  Select FirstName, LastName for Employees and then create a new column FullName. Use space between words. (9 rows). Look online for examples of string concatenation in PostgreSQL and read about Aliases.**   
SELECT FirstName, LastName, CONCAT(FirstName,' ', LastName) AS FullName   
FROM Employees   

**13. Select OrderID, ProductID, UnitPrice, Quantity and create new column TotalPrice (ignore Discount) for OrderDetails. Order by OrderID and ProductID. (2155 rows)**   
SELECT orderid, productid, unitprice, quantity, SUM(UnitPrice)   
OVER (ORDER BY orderid & productid)   
AS TotalPrice FROM orderdetails   

**14. How many different customers do we have in the Customers table? (1 row, 91 customers). Look online for aggregate functions.**   
SELECT COUNT(DISTINCT customerid)   
FROM customers   

**15. When was the first order in Orders? (1 row, 2014-07-04  8:00:00.000). You can use aggregate Min function or order by date  in asc order and select LIMIT 1 only.**   
select MIN(orderdate) from Orders   
select orderdate from Orders   
order by orderdate      
LIMIT 1   

**16.  Get a list of all unique ContactTitles from Customers table. Use Distinct or Group By.**   
select Distinct(ContactTitle) from Customers   

**17. Get a NumberOfCustomers for each Country where we have Customers. Order it by NumberOfCustomers  in DESC order.(21 rows). Use Group By clause.**   
select country, count(country) as NumberOfCustomers from Customers   
group by country   
order by numberofcustomers desc   

**18. Show ProductID(Products), SupplierID(Suppliers,Products) and CompanyName(Suppliers) for each product from Products. (77 rows). This question introduces a new concept - INNER JOIN.**  
select Products.ProductID, Products.SupplierID, Suppliers.CompanyName  
from Products   
inner join Suppliers   
on Products.SupplierID = CAST(Suppliers.SupplierID AS int)   

**19. Show the OrderID, OrderDate(date only) and CompanyName(Shippers) for all Orders with OrderID<10270. Sort by OrderID. (22 rows). Note: when you join two tables, the field that's joined on not necessarily need to have the same name - ShipVia in Orders and ShipperID in Shippers.**   
select Orders.OrderID, date(Orders.OrderDate), Shippers.CompanyName   
from Orders   
inner join Shippers   
on Orders.ShipVia = Shippers.ShipperID   
where Orders.OrderID < 10270   
order by Orders.OrderID ASC   




### Medium Problems
**1. Show the list with CategoryNames and the TotalNumber of products for each Category sorted by number of products in desc order. (8 rows). Here you have to combine JOIN and GROUP BY.**   
select categories.CategoryName, count(categories.CategoryName) as categoryname_count   
from categories   
join products   
on categories.categoryid = products.categoryid   
group by categoryname   

**2. In the Customers table, show the total number of Customers per Country and City. (69 rows)**   
select customers.city,    
count(customers.city) as customers_per_city,   
customers.country,   
count(customers.country) as customer_per_country   
from customers   
group by customers.city, customers.country   

**3. What Products do we have in our inventory that needs to be reordered? Sort results by ProductID.  (22 rows). Use UnitsInStock field  <=  ReorderLevel field only.**   
select productid, unitsinstock, reorderlevel from products  
where unitsinstock <= reorderlevel  
order by productid  

**4. Incorporate UnitsOnOrder and Discontinued fields. So, now UnitsInOrder + UnitsInStock <= ReorderLevel and  Discontinued flag is False. (2 rows)**   
select unitsonorder, discontinued, unitsinstock, reorderlevel from products   
where unitsonorder + unitsinstock <= reorderlevel and discontinued = false   

**5.  Create a list of all Customers sorted by Region and put customers with Null Region value at the beginning (not at the end). By default Null values are at the end. So, you have to create a new column HasRegion (0/1) with CASE statement and Order By two columns: HasRegion and Region.**   
select contactname, region,   
case   
	when region is NULL then '0'   
	else '1'   
end as HasRegion   
from customers   
order by HasRegion   

**6. We want to investigate some more shipping options for our customers. Return the three countries with the highest average freight ordered by average freight in descending order. Use GROUP BY, AVG() and LIMIT statements.**   
select shipcountry, avg(cast(freight as decimal(10,2))) avg_freight   
from orders    
group by shipcountry   
order by avg_freight desc   
limit 3   


**7. Return the same result as previous problem, but for only 2015. You can use BETWEEN statement. France should be the third country.**   
select shipcountry, avg(cast(freight as decimal(10,2))) avg_freight   
from orders   
where orderdate between '2015-01-01 00:00:00' and '2015-12-31 23:59:59'   
group by shipcountry   
order by avg_freight desc   
limit 3   

**8. Return the same result as previous problem, but for last 12 months only.**

**9. Show OrderId, Quantity, ProductName, EmployeeID and LastName for each order in Orders table. Sort by OrderId and ProductID.(2155 rows). Yes, you have to JOIN 4 tables and select only these columns.**

**10. Show all "customers" that have never placed an order.(2 rows). You can use LEFT JOIN**    
select customers.customerid from customers   
left join orders    
on orders.customerid = customers.customerid   
where orders.customerid is NULL   

**11. Show all Customers who have never placed an order with Employee 4.(16 rows)**    




### Hard Problems
**1. Assuming that now is January 1, 2017, we want to find all high-value customers from 2016, who've made at least one order with a total value of $10,000 and give them VIP status. (6 rows)**

**2.  What if sales person changes her mind and instead of 1 order with >$10,000 would ask about $15,000 in total during 2016?**

**3. Change the above query including Discount in your calculations.  Order it by total amount which includes discount.**

**4. At the end of the month salespeople are trying harder to get orders. Select all orders which were placed on the last day of the month. Ordered by EmployeeID and OrderID. (24 rows)**

**5. We want to identify the size of the table for our website. Show the top 10 orders with maximum items. Ordered by number of items.**

**6. Select 2% of OrderDetails table. (41 rows). Use statement  random() < 0.02**

**7. One of the salespeople think that she accidentally entered line item twice on an order, each time with different ProductId, but the same quantity.  She remembers that quantity was 60 or more. Show all OrderID that match this, ordered by OrderID. (5 rows)**

**8. For all orders from previous question, show OrderDetails.**

**9. Get the list of all orders that are late. Ordered by delay.**

**10.  Which salespeople has the most late orders?**

**11. For each EmployeeID show a number of AllOrders and LateOrders in one table.  Show "0" if there is no LateOrders for Employee. (9 rows)**

**12. Add percentage of LateOrders column rounded by 0.01%.**
