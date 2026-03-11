CREATE DATABASE training_db;

-- DDL - CREATE, DROP, ALTER

CREATE TABLE associates (
    associate_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE
)

 /*
DROP TABLE associates;
*/

--DML - INSERT, UPDATE, DELETE

INSERT INTO associates (
    first_name,
    last_name,
    email,
    hire_date
)
VALUES (
    'Dylan',
    'Parrott',
    'dylan.parrott@revature.net',
    DEFAULT
), (
    'Lee',
    'Wilson',
    'lee.wilson@revature.net',
    '2026-02-23'
);



ALTER TABLE associates ADD COLUMN department VARCHAR(50);
ALTER TABLE associates ALTER COLUMN hire_date SET NOT NULL;
ALTER TABLE associates ALTER COLUMN email TYPE VARCHAR(115);
UPDATE associates SET department = 'Training';

ALTER TABLE associates ALTER COLUMN department SET NOT NULL;

SELECT * FROM associates
