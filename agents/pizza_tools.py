from langchain.tools import tool
import uuid

# --- Mock menu ---
MENU = {
    "Margherita": {
        "sizes": ["small", "medium", "large"],
        "price": {"small": 199, "medium": 299, "large": 399},
    },
    "Pepperoni": {
        "sizes": ["medium", "large"],
        "price": {"medium": 349, "large": 449},
    },
    "Veggie": {
        "sizes": ["small", "medium", "large"],
        "price": {"small": 249, "medium": 329, "large": 409},
    },
}


@tool
def get_menu() -> dict:
    """
    Returns the available pizza menu.
    """
    return {
        "menu": MENU
    }


@tool
def place_order(
    pizza_name: str,
    size: str,
    quantity: int,
    delivery_time: str
) -> dict:
    """
    Places a pizza order and returns structured order details.
    """

    if pizza_name not in MENU:
        return {
            "error": f"{pizza_name} is not available"
        }

    if size not in MENU[pizza_name]["sizes"]:
        return {
            "error": f"{size} size not available for {pizza_name}"
        }

    order_id = f"ORD-{uuid.uuid4().hex[:6].upper()}"
    price_per_item = MENU[pizza_name]["price"][size]
    total_price = price_per_item * quantity

    return {
        "order_id": order_id,
        "pizza": pizza_name,
        "size": size,
        "quantity": quantity,
        "delivery_time": delivery_time,
        "total_price": total_price,
        "status": "order_confirmed"
    }


@tool
def track_order(order_id: str) -> dict:
    """
    Mock order tracking.
    """

    return {
        "order_id": order_id,
        "status": "preparing",
        "estimated_delivery": "30 minutes"
    }
 #note: here i am directly returning the hardcoded values, but to add the functionallity i have created backend folder
    # we can add the logic there and call it here.