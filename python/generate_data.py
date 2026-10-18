
import random
from datetime import date, timedelta
from pathlib import Path

# -------------------------
# Configuration
# -------------------------

random.seed(42)

CUSTOMERS_COUNT = 40
ORDERS_COUNT = 200

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "sql" / "02_insert_data.sql"

product_names = [
    "Laptop", "Mouse", "Keyboard", "Monitor", "Headphones",
    "Smartphone", "Tablet", "Webcam", "Speaker", "Printer",
    "Router", "Microphone", "Charger", "Power Bank", "Smartwatch",
    "SSD Drive", "USB Hub", "Graphics Card", "Desk Lamp",
    "External Hard Drive"
]

first_names = [
    "Alex", "Maria", "John", "Emma", "Michael",
    "Olivia", "James", "Sophia", "William", "Ava"
]

last_names = [
    "Smith", "Johnson", "Brown", "Wilson", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris"
]


# -------------------------
# Helpers
# -------------------------

def sql_string(value):
    """Escape a Python string for a SQL text literal."""
    return "'" + str(value).replace("'", "''") + "'"


def random_date(start_date, end_date):
    """Return a random date within the given range."""
    days = (end_date - start_date).days
    return start_date + timedelta(days=random.randint(0, days))


# -------------------------
# Customers
# -------------------------

customers = []

for customer_id in range(1, CUSTOMERS_COUNT + 1):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    name = f"{first_name} {last_name}"
    email = f"customer{customer_id}@example.com"

    registration_date = random_date(
        date(2026, 1, 1),
        date(2026, 2, 28)
    )

    customers.append((
        customer_id,
        name,
        email,
        registration_date.isoformat()
    ))


# -------------------------
# Products
# -------------------------

products = []

for product_id, product_name in enumerate(product_names, start=1):
    warehouse_quantity = random.randint(20, 300)
    price = random.randint(1000, 150000)

    products.append((
        product_id,
        product_name,
        warehouse_quantity,
        price
    ))

product_prices = {
    product_id: price
    for product_id, _, _, price in products
}


# -------------------------
# Orders and order items
# -------------------------

orders = []
order_items = []

for order_id in range(1, ORDERS_COUNT + 1):
    customer_id = random.randint(1, CUSTOMERS_COUNT)

    registration_date = date.fromisoformat(
        customers[customer_id - 1][3]
    )

    order_date = random_date(
        registration_date,
        date(2026, 12, 31)
    )

    status = random.choices(
        ["completed", "pending", "canceled"],
        weights=[75, 15, 10],
        k=1
    )[0]

    orders.append((
        order_id,
        customer_id,
        order_date.isoformat(),
        status
    ))

    items_count = random.randint(1, 3)

    selected_products = random.sample(
        range(1, len(products) + 1),
        items_count
    )

    for product_id in selected_products:
        quantity = random.randint(1, 5)

        # Historical price at the time of purchase
        base_price = product_prices[product_id]
        price_multiplier = random.choice([90, 95, 100, 100, 105, 110])
        unit_price = max(1, base_price * price_multiplier // 100)

        order_items.append((
            order_id,
            product_id,
            quantity,
            unit_price
        ))


# -------------------------
# Generate SQL file
# -------------------------

sql_lines = [
    "-- E-Commerce Sales Analytics",
    "-- Generated test data",
    "-- Run after 01_create_tables.sql",
    "",
    "PRAGMA foreign_keys = ON;",
    "",
    "BEGIN TRANSACTION;",
    "",
    "-- Reset existing data",
    "DELETE FROM order_items;",
    "DELETE FROM orders;",
    "DELETE FROM products;",
    "DELETE FROM customers;",
    "",
    "-- Customers"
]

for customer_id, name, email, registration_date in customers:
    sql_lines.append(
        "INSERT INTO customers "
        "(customer_id, name, email, registration_date) VALUES "
        f"({customer_id}, {sql_string(name)}, "
        f"{sql_string(email)}, {sql_string(registration_date)});"
    )

sql_lines.extend(["", "-- Products"])

for product_id, name, warehouse_quantity, price in products:
    sql_lines.append(
        "INSERT INTO products "
        "(product_id, product_name, warehouse_quantity, price) VALUES "
        f"({product_id}, {sql_string(name)}, "
        f"{warehouse_quantity}, {price});"
    )

sql_lines.extend(["", "-- Orders"])

for order_id, customer_id, order_date, status in orders:
    sql_lines.append(
        "INSERT INTO orders "
        "(order_id, customer_id, order_date, status) VALUES "
        f"({order_id}, {customer_id}, "
        f"{sql_string(order_date)}, {sql_string(status)});"
    )

sql_lines.extend(["", "-- Order Items"])

for order_id, product_id, quantity, unit_price in order_items:
    sql_lines.append(
        "INSERT INTO order_items "
        "(order_id, product_id, quantity, unit_price) VALUES "
        f"({order_id}, {product_id}, {quantity}, {unit_price});"
    )

sql_lines.extend(["", "COMMIT;", ""])

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE.write_text(
    "\n".join(sql_lines),
    encoding="utf-8"
)

print("SQL file generated successfully!")
print(f"File: {OUTPUT_FILE}")
print(f"Customers: {len(customers)}")
print(f"Products: {len(products)}")
print(f"Orders: {len(orders)}")
print(f"Order items: {len(order_items)}")
