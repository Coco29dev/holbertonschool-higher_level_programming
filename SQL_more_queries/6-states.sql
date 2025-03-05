-- create database and table
-- in table with id attribut : unique, primary key, auto increment
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    UNIQUE (id),
    PRIMARY KEY (id)
);