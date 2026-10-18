-- Analysis 1: Total revenue from completed orders

SELECT
    SUM(oi.unit_price * oi.quantity / 100.0) AS total_revenue_eur
FROM order_items AS oi
JOIN products AS p
    ON oi.product_id = p.product_id
JOIN orders AS o
    ON oi.order_id = o.order_id
WHERE o.status = 'completed';

-- Analysis 2: Revenue by product

SELECT
    p.product_name,
    SUM(oi.unit_price * oi.quantity / 100.0) AS total_revenue_eur
FROM order_items AS oi
JOIN products AS p
    ON oi.product_id = p.product_id
JOIN orders AS o
    ON oi.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY p.product_name 
ORDER BY total_revenue_eur DESC;

-- Analysis 3

SELECT
	c.name,
	SUM (oi.unit_price * oi.quantity ) / 100.0 AS total_spent_eur
FROM customers AS c
JOIN orders as o
	ON c.customer_id = o.customer_id 
JOIN order_items AS oi
	ON o.order_id  = oi.order_id 
WHERE o.status = 'completed'
GROUP BY c.customer_id 
ORDER BY total_spent_eur DESC;

-- Analysis 4: Repeat Customers

SELECT 
	c.name,
	COUNT( o.order_id ) AS total_orders
FROM 
	customers AS c 
JOIN 
	orders AS o
	ON c.customer_id = o.customer_id
WHERE
	o.status = 'completed'
GROUP BY 
	c.customer_id
HAVING
	COUNT( o.order_id ) > 1
ORDER BY 
	total_orders DESC

-- Analysis 5: Monthly Revenue

SELECT
	STRFTIME('%Y-%m', o.order_date) AS month,
	SUM(oi.quantity * oi.unit_price) / 100.0 AS total_revenue_eur
FROM
	orders AS o
JOIN order_items AS oi
	ON o.order_id = oi.order_id 
WHERE 
	o.status = 'completed' AND STRFTIME('%Y', o.order_date) = '2026'
GROUP BY
	month 
ORDER BY
	month ASC