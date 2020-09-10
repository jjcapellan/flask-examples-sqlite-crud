DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  department TEXT NOT NULL,
  age INTEGER NOT NULL,
  salary INTEGER NOT NULL
);

-- Create some rows
INSERT INTO employees (name, department, age, salary) VALUES ('John', 'accounting', 35, 1900);
INSERT INTO employees (name, department, age, salary) VALUES ('Peter', 'manufacturing', 24, 1100);
INSERT INTO employees (name, department, age, salary) VALUES ('Paul', 'manufacturing', 41, 1250);
INSERT INTO employees (name, department, age, salary) VALUES ('Alice', 'accounting', 45, 2080);