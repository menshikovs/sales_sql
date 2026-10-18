-- Insert customers

INSERT INTO customers (
    customer_id,
    name,
    email,
    registration_date
)
VALUES
    (1, 'Alex Johnson', 'alex@example.com', '2026-01-15'),
    (2, 'Maria Smith', 'maria@example.com', '2026-02-10'),
    (3, 'Irina Smith', 'irina@example.com', '2026-02-02'),
    (4, 'John Doe', 'john@example.com', '2026-06-08'),
    (5, 'Peter Smith', 'peter@example.com', '2026-09-10');

-- Insert products

INSERT INTO products (
    product_id,
    product_name,
    warehouse_quantity,
    price
)
VALUES
    (1, 'Laptop', 15, 120000),
    (2, 'Mouse', 50, 2500),
    (3, 'Keyboard', 30, 7500),
    (4, 'Monitor', 20, 30000),
    (5, 'Headphones', 40, 10000);

-- Insert orders

INSERT INTO orders (
    order_id,
    customer_id,
    order_date,
    status
)
VALUES
    (1, 1, '2026-03-10', 'completed'),
    (2, 2, '2026-04-15', 'completed'),
    (3, 3, '2026-05-20', 'canceled'),
    (4, 4, '2026-07-12', 'pending'),
    (5, 5, '2026-10-01', 'pending'),
    (6, 1, '2026-08-15', 'completed');

-- Insert order_items

INSERT INTO order_items (
    order_id,
    product_id,
    quantity,
    unit_price
)
VALUES
    (1, 1, 1, 120000),
    (2, 2, 2, 2500),
    (3, 3, 1, 7500),
    (4, 4, 2, 30000),
    (5, 5, 3, 10000),
    (6, 2, 1, 2500),
    (6, 5, 1, 10000);