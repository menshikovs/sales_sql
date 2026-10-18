-- Analysis 1: Total revenue from completed orders

SELECT
    SUM(oi.unit_price * oi.quantity / 100.0) AS total_revenue_eur
FROM order_items AS oi
JOIN products AS p
    ON oi.product_id = p.product_id
JOIN orders AS o
    ON oi.order_id = o.order_id
WHERE o.status = 'completed';