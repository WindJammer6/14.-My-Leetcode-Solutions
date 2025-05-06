-- Using MySQL (SQL implementation)
-- This question tests you on using aliases on MySQL and self inner joins of a table

-- About MySQL aliases:
-- Source(s):
-- https://www.w3schools.com/mysql/mysql_alias.asp (W3Schools)
SELECT e.name
AS 'Employee'
FROM Employee e
INNER JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
