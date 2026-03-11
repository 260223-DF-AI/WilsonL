-- Active: 1773160166027@@127.0.0.1@5432@chinook_pg
-- Parking Lot*******
-- *                *
-- *                *
--- *****************

-- SETUP:
-- Connect to the server (Azure Data Studio / Database extension/psql)
-- Create a database (I recommend chinook_pg)
-- Execute the Chinook database (from the Chinook_pg.sql file) to create Chinook resources in your server (I recommend doing this from psql)

-- Comment can be done single line with --
-- Comment can be done multi line with /* */

/*
DQL - Data Query Language
Keywords:

SELECT - retrieve data, select the columns from the resulting set
FROM - the table(s) to retrieve data from
WHERE - a conditional filter of the data
GROUP BY - group the data based on one or more columns
HAVING - a conditional filter of the grouped data
ORDER BY - sort the data
*/

SELECT * FROM actor;
SELECT last_name FROM actor;
SELECT * FROM actor WHERE first_name = 'Morgan';
select * from actor where first_name = 'John';

-- BASIC CHALLENGES
-- List all customers (full name, customer id, and country) who are not in the USA
SELECT first_name || ' ' || last_name as full_name, customer_id, country FROM customer
WHERE NOT country = 'USA';
-- List all customers from Brazil
SELECT * FROM customer WHERE country = 'Brazil';

-- List all sales agents
SELECT * FROM employee WHERE title = 'Sales Support Agent';

-- Retrieve a list of all countries in billing addresses on invoices
SELECT DISTINCT(billing_country) FROM invoice;

-- Retrieve how many invoices there were in 2009, and what was the sales total for that year?
SELECT COUNT(*), SUM(total) AS sales_total FROM invoice WHERE EXTRACT(YEAR FROM invoice_date) = 2009;
-- (challenge: find the invoice count sales total for every year using one query)
SELECT COUNT(*), SUM(total) AS sales_total, EXTRACT(YEAR FROM invoice_date) AS year FROM invoice 
GROUP BY EXTRACT(YEAR FROM invoice_date);

-- how many line items were there for invoice #37
SELECT COUNT(*) FROM invoice_line WHERE invoice_id = 37;

-- how many invoices per country? BillingCountry  # of invoices -
SELECT COUNT(*), billing_country FROM invoice GROUP BY billing_country;

-- Retrieve the total sales per country, ordered by the highest total sales first.
SELECT billing_country, SUM(total) as total_sales FROM invoice 
GROUP BY billing_country ORDER BY billing_country DESC;


-- JOINS CHALLENGES
-- Every Album by Artist
SELECT al.title, ar.name FROM album al JOIN artist ar ON al.artist_id = ar.artist_id; 

-- (inner keyword is optional for inner join)
-- All songs of the rock genre
SELECT t.name AS song_name, g.name AS genre_name FROM track t 
JOIN genre g on t.genre_id = g.genre_id 
WHERE g.name = 'Rock';

-- Show all invoices of customers from brazil (mailing address not billing)
SELECT i.invoice_id, c.first_name || ' ' || c.last_name AS customer_name, c.country FROM invoice i
JOIN customer c on c.customer_id = i.customer_id
WHERE c.country = 'Brazil';

-- Show all invoices together with the name of the sales agent for each one
SELECT i.invoice_id, i.total, c.first_name || ' ' || c.last_name AS customer_name, 
e.first_name || ' ' || e.last_name AS agent_name FROM invoice i
JOIN customer c ON c.customer_id = i.customer_id
JOIN employee e ON e.employee_id = c.support_rep_id;

-- Which sales agent made the most sales in 2009?
SELECT COUNT(*) AS sales_count, e.first_name || ' ' || e.last_name AS agent_name FROM invoice i
JOIN customer c ON c.customer_id = i.customer_id
JOIN employee e ON e.employee_id = c.support_rep_id
GROUP BY e.employee_id ORDER BY sales_count DESC LIMIT 1;

-- How many customers are assigned to each sales agent?
SELECT COUNT(*) AS customer_count, e.first_name || ' ' || e.last_name AS agent_name FROM customer c
JOIN employee e ON e.employee_id = c.support_rep_id
GROUP BY e.employee_id;

-- Which track was purchased the most in 2010?
SELECT t.name AS track_name, COUNT(*) AS purchase_count FROM invoice i
JOIN invoice_line il ON i.invoice_id = il.invoice_id
JOIN track t ON t.track_id = il.track_id
WHERE EXTRACT(YEAR FROM i.invoice_date) = 2010
GROUP BY track_name ORDER BY purchase_count DESC LIMIT 1;

-- Show the top three best selling artists.
SELECT COUNT(*) AS sales_count, ar.name AS artist_name FROM invoice_line il
JOIN track t ON t.track_id = il.track_id
JOIN album al ON al.album_id = t.album_id
JOIN artist ar ON ar.artist_id =  al.artist_id
GROUP BY artist_name ORDER BY sales_count DESC LIMIT 3;

-- Which customers have the same initials as at least one other customer?
SELECT * FROM customer;
SELECT LEFT(first_name, 1) || '.' || LEFT(last_name, 1) AS customer_initials,
first_name || ' ' || last_name as customer_name FROM customer
WHERE CONCAT(LEFT(first_name, 1), LEFT(last_name, 1)) IN
(SELECT CONCAT(LEFT(first_name, 1), LEFT(last_name, 1)) FROM customer
GROUP BY CONCAT(LEFT(first_name, 1), LEFT(last_name, 1)) HAVING COUNT(*) > 1);

-- Which countries have the most invoices?
SELECT COUNT(*) AS invoice_count, 


-- Which city has the customer with the highest sales total?


-- Who is the highest spending customer?


-- Return the email and full name of of all customers who listen to Rock.


-- Which artist has written the most Rock songs?


-- Which artist has generated the most revenue?




-- ADVANCED CHALLENGES
-- solve these with a mixture of joins, subqueries, CTE, and set operators.
-- solve at least one of them in two different ways, and see if the execution
-- plan for them is the same, or different.

-- 1. which artists did not make any albums at all?


-- 2. which artists did not record any tracks of the Latin genre?


-- 3. which video track has the longest length? (use media type table)


-- 4. boss employee (the one who reports to nobody)


-- 5. how many audio tracks were bought by German customers, and what was
--    the total price paid for them?


-- 6. list the names and countries of the customers supported by an employee
--    who was hired younger than 35.


-- DML exercises

-- 1. insert two new records into the employee table.


-- 2. insert two new records into the tracks table.


-- 3. update customer Aaron Mitchell's name to Robert Walter


-- 4. delete one of the employees you inserted.


-- 5. delete customer Robert Walter.
