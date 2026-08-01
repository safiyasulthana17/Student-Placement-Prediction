CREATE DATABASE placement_db;
USE placement_db;
CREATE TABLE student_predictions (
    id INT PRIMARY KEY AUTO_INCREMENT,

    age INT,
    gender VARCHAR(20),
    cgpa FLOAT,
    branch VARCHAR(100),

    internships_count INT,
    projects_count INT,

    prediction VARCHAR(20),
    probability FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SELECT * FROM student_predictions;