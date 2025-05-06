-- Using MySQL (SQL implementation)
-- This question tests you on using the 'COUNT' and 'GROUP BY' commands on MySQL.

-- Note: The 'HAVING' command is used here since the 'WHERE' command cannot be used with aggregate functions
-- (i.e. 'COUNT', 'SUM', 'AVG', 'MAX', 'MIN', etc.)

-- About MySQL 'GROUP BY' and 'HAVING' commands:
-- Source(s):
-- https://www.w3schools.com/mysql/mysql_groupby.asp (GeekforGeeks)
-- https://www.w3schools.com/mysql/mysql_having.asp (GeekforGeeks)
SELECT `email`
AS 'Email'
FROM Person
GROUP BY `email`

HAVING COUNT(`email`) > 1
  -- If you use this line of code, the MySQL (SQL implementation) query will not work!
-- WHERE COUNT(`email`) > 1

ORDER BY `email`;
