from ics import Calendar, Event
from datetime import datetime, timedelta

def create_ics_event(order_id, delivery_time, pizza_name):
    c = Calendar()
    e = Event()
    e.name = f"Pizza Delivery: {pizza_name}"
    e.begin = datetime.strptime(delivery_time, "%I %p")
    e.duration = timedelta(minutes=30)
    e.description = f"Order ID: {order_id}"
    c.events.add(e)

    with open(f"{order_id}.ics", "w") as f:
        f.writelines(c)
    return f"{order_id}.ics"
