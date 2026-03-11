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
SELECT LEFT(first_name, 1) || '.' || LEFT(last_name, 1) AS customer_initials,
first_name || ' ' || last_name as customer_name FROM customer
WHERE CONCAT(LEFT(first_name, 1), LEFT(last_name, 1)) IN
(SELECT CONCAT(LEFT(first_name, 1), LEFT(last_name, 1)) FROM customer
GROUP BY CONCAT(LEFT(first_name, 1), LEFT(last_name, 1)) HAVING COUNT(*) > 1);

-- Which countries have the most invoices?
SELECT COUNT(*) AS invoice_count, billing_country FROM invoice
GROUP BY billing_country ORDER BY invoice_count DESC; 


-- Which city has the customer with the highest sales total?
SELECT * FROM customer;
SELECT * FROM invoice;
SELECT i.billing_city, SUM(i.total) AS sales_total, c.first_name || ' ' || c.last_name AS customer_name FROM invoice i
JOIN customer c ON i.customer_id = c.customer_id
GROUP BY customer_name, i.billing_city ORDER BY sales_total DESC LIMIT 1;

-- Who is the highest spending customer?
SELECT SUM(i.total) AS sales_total, c.first_name || ' ' || c.last_name as customer_name FROM invoice i
JOIN customer c on i.customer_id = c.customer_id
GROUP BY customer_name ORDER BY sales_total DESC LIMIT 1;
-- Return the email and full name of of all customers who listen to Rock.
SELECT c.first_name, c.last_name, c.email FROM customer c 
JOIN invoice i ON i.customer_id = c.customer_id
JOIN invoice_line il on il.invoice_id = i.invoice_id
JOIN track t on t.track_id = il.track_id
JOIN genre g on g.genre_id = t.genre_id
WHERE g.name = 'Rock'
GROUP BY c.customer_id;

-- Which artist has written the most Rock songs?
SELECT COUNT(*) AS track_count, ar.name FROM track t
JOIN album al ON al.album_id = t.album_id
JOIN artist ar ON ar.artist_id = al.artist_id
JOIN genre g ON g.genre_id = t.genre_id
WHERE g.name = 'Rock'
GROUP BY ar.artist_id ORDER BY track_count DESC LIMIT 1;

-- Which artist has generated the most revenue?
SELECT * FROM album;
SELECT * FROM track;
SELECT SUM(i.total) AS sales_total, ar.name FROM invoice i
JOIN invoice_line il ON i.invoice_id = il.invoice_id
JOIN track t ON t.track_id = il.track_id
JOIN album al ON al.album_id = t.album_id
JOIN artist ar ON ar.artist_id = al.artist_id
GROUP BY ar.artist_id ORDER BY sales_total DESC LIMIT 1;



-- ADVANCED CHALLENGES
-- solve these with a mixture of joins, subqueries, CTE, and set operators.
-- solve at least one of them in two different ways, and see if the execution
-- plan for them is the same, or different.

-- 1. which artists did not make any albums at all?
SELECT name, artist_id FROM artist
WHERE name NOT IN
(SELECT ar.name FROM artist ar
RIGHT JOIN album al ON ar.artist_id = al.artist_id);



-- 2. which artists did not record any tracks of the Latin genre?
SELECT name, artist_id FROM artist
WHERE name NOT IN 
(SELECT ar.name FROM artist ar
JOIN album al ON ar.artist_id = al.artist_id
JOIN track t ON t.album_id = al.album_id
JOIN genre g ON g.genre_id = t.genre_id
WHERE NOT g.name = 'Latin' 
)
GROUP BY artist_id ORDER BY name;

-- 3. which video track has the longest length? (use media type table)
SELECT t.name AS track_name, t.track_id, mt.name AS media_type, t.milliseconds AS runtime FROM track t
JOIN media_type mt ON t.media_type_id = mt.media_type_id
WHERE mt.media_type_id = 3
GROUP BY t.track_id, t.name, mt.name
ORDER BY t.milliseconds DESC LIMIT 1;

-- 4. boss employee (the one who reports to nobody)
SELECT first_name, last_name FROM employee
WHERE reports_to IS NULL;

-- 5. how many audio tracks were bought by German customers, and what was
--    the total price paid for them?
SELECT SUM(i.total), COUNT(il.quantity) FROM track t
JOIN invoice_line il ON il.track_id = t.track_id
JOIN invoice i ON il.invoice_id = i.invoice_id
JOIN media_type mt ON t.media_type_id = mt.media_type_id
WHERE i.billing_country = 'Germany'
AND NOT mt.media_type_id = 3;
-- 6. list the names and countries of the customers supported by an employee
--    who was hired younger than 35.
SELECT c.first_name, c.last_name, c.country FROM customer c
JOIN employee e ON c.support_rep_id = e.employee_id
WHERE EXTRACT(YEAR FROM AGE(e.hire_date, e.birth_date)) < 35;

-- DML exercises

-- 1. insert two new records into the employee table.
INSERT INTO employee(
    last_name,
    first_name
) VALUES (
    'Wilson',
    'Lee'
),
(
    'Watson',
    'Lester'
);

-- 2. insert two new records into the tracks table.
INSERT INTO track (
    name,
    media_type_id,
    milliseconds,
    unit_price
) VALUES (
    'Unfinished Business',
    1,
    258000,
    0.99
), (
    'Pink Pony Club',
    1,
    240000,
    0.99
);

-- 3. update customer Aaron Mitchell's name to Robert Walter
UPDATE customer SET first_name = 'Robert', last_name = 'Walter'
WHERE first_name = 'Aaron' AND last_name = 'Mitchell';

-- 4. delete one of the employees you inserted.
DELETE FROM employee WHERE first_name = 'Lester' AND last_name = 'Watson';

-- 5. delete customer Robert Walter.
DELETE FROM customer WHERE first_name = 'Robert' AND last_name = 'Walter';