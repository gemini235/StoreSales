CREATE DATABASE SuperstoreDB;
USE SuperstoreDB;

-- Create Customer Dimension Table
CREATE TABLE DimCustomer (
    CustomerID VARCHAR(50) PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    Segment VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    PostalCode VARCHAR(20),
    Region VARCHAR(50) NOT NULL
);

-- Create Product Dimension Table
CREATE TABLE DimProduct (
    ProductID VARCHAR(50) PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    SubCategory VARCHAR(50) NOT NULL
);

-- Create Date Dimension Table
CREATE TABLE DimDate (
    DateID DATE PRIMARY KEY,
    Year SMALLINT NOT NULL,
    Month SMALLINT NOT NULL,
    Day SMALLINT NOT NULL,
    Weekday SMALLINT NOT NULL
);

-- Create Ship Mode Dimension Table
CREATE TABLE DimShipMode (
    ShipMode VARCHAR(50) PRIMARY KEY
);

-- Create Fact Sales Table
CREATE TABLE FactSales (
    OrderID VARCHAR(50),
    CustomerID VARCHAR(50) REFERENCES DimCustomer(CustomerID),
    ProductID VARCHAR(50) REFERENCES DimProduct(ProductID),
    OrderDate DATE REFERENCES DimDate(DateID),
    ShipDate DATE REFERENCES DimDate(DateID),
    ShipMode VARCHAR(50) REFERENCES DimShipMode(ShipMode),
    Sales DECIMAL(10,2) NOT NULL,
    Order_Year SMALLINT NOT NULL,
    Order_Month SMALLINT NOT NULL,
    Order_Day SMALLINT NOT NULL,
    Order_Weekday SMALLINT NOT NULL,
    Shipping_Delay SMALLINT NOT NULL,
    Log_Sales DECIMAL(10,5) NOT NULL,
    Scaled_Sales DECIMAL(10,5) NOT NULL,
    PRIMARY KEY (OrderID, ProductID)
);

-- Import Data from CSV Files
COPY DimCustomer(CustomerID, CustomerName, Segment, Country, City, State, PostalCode, Region)
FROM "C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\customers.csv" DELIMITER ',' CSV HEADER;

COPY DimProduct(ProductID, ProductName, Category, SubCategory)
FROM "C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\products.csv" DELIMITER ',' CSV HEADER;

COPY FactSales(OrderID, ProductID, Sales, Order_Year, Order_Month, Order_Day, Order_Weekday, Shipping_Delay, Log_Sales, Scaled_Sales)
FROM "C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\sales.csv" DELIMITER ',' CSV HEADER;

COPY FactSales(OrderID, CustomerID, OrderDate, ShipDate, ShipMode)
FROM "C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\orders.csv" DELIMITER ',' CSV HEADER;

