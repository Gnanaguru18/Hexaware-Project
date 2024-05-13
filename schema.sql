create database Ecom_application
use Ecom_application


CREATE TABLE Customer (
    customer_id INT PRIMARY KEY identity(10001,1),
    name VARCHAR(100),
    email VARCHAR(255),
    password VARCHAR(50)
);


CREATE TABLE Cart (
    cart_id INT PRIMARY KEY identity(30001,1),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Product (
    product_id INT PRIMARY KEY identity(20001,1),
    name VARCHAR(255),
    price INT,
    description VARCHAR(100),
    stock_quantity INT
);

CREATE TABLE Cart_items (
    cart_item_id INT PRIMARY KEY identity(31001,1),
    cart_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY identity(40001,1),
    customer_id INT,
    order_date VARCHAR(20),
    total_price INT,
    shipping_address VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);


CREATE TABLE Order_items (
    order_item_id INT PRIMARY KEY identity(41001,1),
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);



