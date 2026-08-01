-- CREATE DATABASE student_crud_db;

CREATE TABLE studentcrud
(
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    roll_number VARCHAR(20),
    email VARCHAR(100),
    department VARCHAR(100),
    semester INTEGER,
    cgpa DECIMAL(3,2)
);

INSERT INTO studentcrud
(name,roll_number,email,department,semester,cgpa)
VALUES
('Ali','101A','ali@gmail.com','Software Engineering',4,3.60);


--rerieve all data

SELECT * FROM studentcrud;

UPDATE studentcrud
SET cgpa=3.90
WHERE student_id=1;

DELETE FROM studentcrud
WHERE student_id=1;