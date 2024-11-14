-- WHERE CLAUSE

SELECT *
FROM employee_salary
WHERE first_name = 'Leslie' 
;

SELECT *
FROM employee_salary
WHERE salary <= 50000
;

SELECT *
FROM employee_demographics
WHERE birth_date > '1985-01-01'
;



-- AND OR NOT -- Logical operators

SELECT *
FROM employee_demographics
WHERE (first_name = "Leslie" AND age = 44) OR age > 55
;

-- like statement
-- % and _

SELECT *
FROM employee_demographics
WHERE birth_date LIKE "1989%"
;


-- group by 
SELECT *
FROM employee_demographics;




SELECT occupation, salary
FROM employee_salary
GROUP BY occupation, salary
;

SELECT gender, AVG(age), MAX(age), MIN(age),COUNT(age)
FROM employee_demographics
GROUP BY gender
;

-- order by

SELECT *
FROM employee_demographics
ORDER BY gender, age DESC
;


-- having or where
SELECT *
FROM employee_demographics
ORDER BY gender, age DESC;



-- having vs where
 
SELECT gender, AVG (age)
FROM employee_demographics
GROUP BY gender
HAVING AVG (age) > 40
;

-- where

SELECT occupation, AVG (salary)
FROM employee_salary
WHERE occupation LIKE "%manager%"
GROUP BY occupation
HAVING AVG (salary) > 75000
;


-- limit and aliasinng 

SELECT *
FROM employee_demographics
ORDER BY age DESC
LIMIT 2, 1
;

-- aliasing

SELECT gender, AVG (age)
FROM employee_demographics
GROUP BY gender
HAVING AVG (age) > 40
;












