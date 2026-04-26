-- Создание базы данных
CREATE DATABASE microservices_lab;

-- Подключение к базе данных
\c microservices_lab

-- Создание таблицы currencies
CREATE TABLE IF NOT EXISTS currencies (
    id INTEGER PRIMARY KEY,
    currency_name VARCHAR(50) UNIQUE NOT NULL,
    rate NUMERIC(10, 2) NOT NULL
);