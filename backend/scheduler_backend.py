def schedule_delivery(order_id, time):
    return {
        "order_id": order_id,
        "scheduled_time": time,
        "status": "Delivery scheduled"
    }

if __name__ == "__main__":
    print(schedule_delivery("ORD123", "8 PM"))
