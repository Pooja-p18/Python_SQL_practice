CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    city VARCHAR(50) NOT NULL,
    marks INT
);

INSERT INTO students
(student_name, age, city, marks)
VALUES
('Alice', 20, 'New York', 85),
('Bob', 22, 'Los Angeles', 90),
('Charlie', 19, 'Chicago', 78),
('David', 21, 'Houston', 92),
('Eva', 23, 'Phoenix', 88);

