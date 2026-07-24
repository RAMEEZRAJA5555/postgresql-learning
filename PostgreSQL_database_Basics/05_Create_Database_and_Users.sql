-- PostgreSQL: Create Database and Users

-- Create a new database
CREATE DATABASE bookstore;

-- Create a new user (role) with a password
CREATE USER app_user
WITH PASSWORD 'securepassword123';

-- Grant all privileges on the database
GRANT ALL PRIVILEGES
ON DATABASE bookstore
TO app_user;

-- Connect to the bookstore database
\c bookstore

-- Grant schema permissions (PostgreSQL 15+)
GRANT ALL
ON SCHEMA public
TO app_user;

-- Notes


-- CREATE DATABASE:
-- Creates a new database.

-- CREATE USER:
-- Creates a PostgreSQL user (role) with a password.

-- GRANT ALL PRIVILEGES:
-- Gives the specified user full access to the database.

-- \c:
-- Connects to the specified database.

-- GRANT ALL ON SCHEMA:
-- Allows the user to create and manage database objects
-- inside the public schema.