-- 1.1 Add phone column
ALTER TABLE employees ADD COLUMN phone VARCHAR(20);

-- 1.2 Modify budget column
ALTER TABLE departments ALTER COLUMN budget TYPE DECIMAL(15, 2);

--1.3
CREATE TABLE training_courses(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    duration_hours INTEGER,
    instructor VARCHAR(100)
);

-- 2.1
INSERT INTO employees(
    first_name,
    last_name,
    email,
    salary
) VALUES (
    'Grace',
    'Lee',
    'grace.lee@company.com',
    58000
), (
    'Ivan',
    'Chen',
    'ivan@company.com',
    61000
), (
    'Julia',
    'Kim',
    'julia@company.com',
    55000
);

-- 2.2
UPDATE employees SET salary = salary * 1.1 WHERE dept_id = 1;
UPDATE employees SET email = 'bob.smith@company.com' WHERE emp_id = 2;
-- 2.3
DELETE FROM projects WHERE end_date < CURRENT_DATE;
DELETE FROM employees WHERE dept_id = NULL;
/* this is dangerous since all other information in
those rows will be lost*/

-- 3.1
SELECT * FROM employees ORDER BY salary DESC;

-- 3.2
SELECT * FROM employees WHERE dept_id = 1;

-- 3.3
SELECT * FROM employees WHERE hire_date > '2021-01-01';

-- 3.4
SELECT * FROM employees WHERE salary > 60000 AND salary < 80000;

-- 3.5
SELECT * FROM employees WHERE email LIKE '%company%';

-- 3.6
SELECT * FROM departments WHERE location = 'Building A' or location = 'Building B';

-- 3.7
SELECT SUM(salary), dept_id FROM employees GROUP BY dept_id;
-- 3.8
SELECT AVG(salary) as avg_salary, MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM employees;

-- 3.9
SELECT COUNT(DISTINCT emp_id) as num_employees, dept_id FROM employees GROUP BY dept_id HAVING COUNT(DISTINCT emp_id) >= 2;
-- 3.10
SELECT first_name || ' ' || last_name as full_name, dept_id, '$' || salary AS salary_formatted FROM employees; 

-- 4.1
SELECT emp_id, first_name, last_name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

-- 4.2
SELECT dept_name, COUNT(DISTINCT project_id) as project_count FROM departments d
    JOIN projects p ON d.dept_id = p.dept_id GROUP BY d.dept_id;
-- 4.3
SELECT dept_id, MAX(salary) AS max_salary FROM employees GROUP BY dept_id;

-- 4.4
SELECT EXTRACT(YEAR FROM age(CURRENT_DATE, hire_date)) AS years, 
EXTRACT(MONTH FROM age(CURRENT_DATE, hire_date)) AS months, 
first_name, last_name, emp_id FROM employees;

SELECT * FROM employees;
SELECT * FROM departments;
SELECT * FROM projects;