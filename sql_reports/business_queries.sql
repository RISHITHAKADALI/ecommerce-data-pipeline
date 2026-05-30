CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE ecommerce_orders (
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    order_status VARCHAR(50),
    order_purchase_timestamp DATETIME,
    order_delivered_timestamp DATETIME,
    customer_city VARCHAR(100),
    customer_state VARCHAR(50),
    payment_type VARCHAR(50),
    payment_value FLOAT,
    product_id VARCHAR(50),
    product_category_name VARCHAR(100),
    price FLOAT,
    freight_value FLOAT,
    review_score INT
);