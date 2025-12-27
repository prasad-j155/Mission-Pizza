import uuid

ORDERS = {}

def get_menu():
    return ["Margherita", "Pepperoni", "Veggie"]

def place_order(pizza, size, quantity):
    order_id = str(uuid.uuid4())[:8]
    ORDERS[order_id] = {
        "pizza": pizza,
        "size": size,
        "quantity": quantity,
        "status": "preparing",
        "eta": "20 minutes"
    }
    return {"order_id": order_id, "eta": "20 minutes"}

def track_order(order_id):
    return ORDERS.get(order_id, {"error": "Order not found"})
