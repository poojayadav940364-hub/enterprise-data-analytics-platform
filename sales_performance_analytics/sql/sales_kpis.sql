-- Total Revenue
SELECT 
    SUM(revenue) AS total_revenue
FROM sales;

-- Revenue by Region
SELECT 
    region,
    SUM(revenue) AS region_revenue
FROM sales
GROUP BY region
ORDER BY region_revenue DESC;

-- Top Selling Products
SELECT 
    product,
    SUM(quantity) AS total_quantity_sold
FROM sales
GROUP BY product
ORDER BY total_quantity_sold DESC;

-- Monthly Sales Trend
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(revenue) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;
