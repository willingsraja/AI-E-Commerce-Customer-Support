# Product database
products = [
    {
        "name": "HP Laptop",
        "category": "laptop",
        "price": 55000
    },
    {
        "name": "Dell Laptop",
        "category": "laptop",
        "price": 62000
    },
    {
        "name": "Samsung Galaxy Phone",
        "category": "phone",
        "price": 25000
    },
    {
        "name": "Boat Headphones",
        "category": "headphones",
        "price": 2500
    },
    {
        "name": "Nike Shoes",
        "category": "shoes",
        "price": 4000
    }
]


# Order database
orders = {
    "ORD1001": "Shipped",
    "ORD1002": "Out for Delivery",
    "ORD1003": "Delivered"
}


# TOOL 1: Search products
def search_products(category):

    results = []

    for product in products:
        if category.lower() in product["category"].lower():
            results.append(product)

    return results


# TOOL 2: Check order
def check_order(order_id):

    return orders.get(
        order_id.upper(),
        "Order ID not found"
    )


# TOOL 3: Return product
def return_product(product_name):

    return f"Return request created successfully for {product_name}."


# TOOL 4: Recommend product
def recommend_product(category):

    results = search_products(category)

    if results:
        return results[0]

    return None