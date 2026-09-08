from tools import (
    search_products,
    check_order,
    return_product,
    recommend_product
)


def run_agent(message, memory):

    message_lower = message.lower()


    # -------------------------
    # MEMORY
    # -------------------------

    if "my name is" in message_lower:

        name = message_lower.split("my name is")[-1].strip()

        # Make first letter capital
        name = name.title()

        memory["name"] = name

        return f"Nice to meet you, {name}! How can I help you?"


    if "what is my name" in message_lower:

        if "name" in memory:

            return f"Your name is {memory['name']}."

        else:

            return "You haven't told me your name yet."


    # -------------------------
    # PRODUCT SEARCH TOOL
    # -------------------------

    if "laptop" in message_lower:

        products = search_products("laptop")

        response = "💻 Available Laptops:\n\n"

        for product in products:

            response += (
                f"• {product['name']} - "
                f"₹{product['price']}\n"
            )

        return response


    if "phone" in message_lower:

        products = search_products("phone")

        response = "📱 Available Phones:\n\n"

        for product in products:

            response += (
                f"• {product['name']} - "
                f"₹{product['price']}\n"
            )

        return response


    if "headphone" in message_lower:

        products = search_products("headphones")

        response = "🎧 Available Headphones:\n\n"

        for product in products:

            response += (
                f"• {product['name']} - "
                f"₹{product['price']}\n"
            )

        return response


    if "shoe" in message_lower:

        products = search_products("shoes")

        response = "👟 Available Shoes:\n\n"

        for product in products:

            response += (
                f"• {product['name']} - "
                f"₹{product['price']}\n"
            )

        return response


    # -------------------------
    # ORDER STATUS TOOL
    # -------------------------

    if "order" in message_lower:

        words = message.upper().split()

        for word in words:

            if word.startswith("ORD"):

                status = check_order(word)

                return (
                    f"📦 Order {word}\n\n"
                    f"Status: {status}"
                )

        return (
            "Please provide your order ID.\n"
            "Example: ORD1001"
        )


    # -------------------------
    # RETURN TOOL
    # -------------------------

    if "return" in message_lower:

        if "shoe" in message_lower:

            return return_product("Nike Shoes")

        elif "phone" in message_lower:

            return return_product(
                "Samsung Galaxy Phone"
            )

        elif "laptop" in message_lower:

            return return_product("HP Laptop")

        else:

            return (
                "Please tell me which product "
                "you want to return."
            )


    # -------------------------
    # RECOMMENDATION TOOL
    # -------------------------

    if "recommend" in message_lower:

        if "phone" in message_lower:

            product = recommend_product("phone")

        elif "laptop" in message_lower:

            product = recommend_product("laptop")

        elif "headphone" in message_lower:

            product = recommend_product("headphones")

        else:

            product = None


        if product:

            return (
                f"⭐ Recommended Product\n\n"
                f"{product['name']}\n"
                f"Price: ₹{product['price']}"
            )

        return (
            "What type of product would you "
            "like me to recommend?"
        )


    # -------------------------
    # DEFAULT RESPONSE
    # -------------------------

    return (
        "I can help you with:\n\n"
        "🛍️ Product search\n"
        "📦 Order status\n"
        "↩️ Product returns\n"
        "⭐ Product recommendations\n"
        "🧠 Remembering your name"
    )