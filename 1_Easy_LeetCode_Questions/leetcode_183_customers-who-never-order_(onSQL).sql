-- Using MySQL (SQL implementation)
-- This question tests you on using the 'IN' command on MySQL.

-- About MySQL 'IN' commands:
-- Source(s):
-- https://www.w3schools.com/mysql/mysql_in.asp (W3Schools)
SELECT `name`
AS 'Customers'
FROM `Customers`
WHERE `id` NOT IN (
    SELECT `customerId`
    FROM `Orders`
    );