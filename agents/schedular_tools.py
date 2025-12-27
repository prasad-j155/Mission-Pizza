from langchain.tools import tool
from calender import create_ics_event

@tool
def schedule_delivery(order_id: str, delivery_time: str, pizza_name: str) -> dict:
    """
    Schedules a delivery slot for the given order in Google Calendar.
    """

    print("schedule_delivery")
    
    create_ics_event(order_id, delivery_time, pizza_name)
    return {
        "order_id": order_id,
        "scheduled": True,
        "delivery_time": delivery_time,
        "calendar_event_created": True,
        "calendar_event_link": "calendar_link",
        "status": "delivery_scheduled"
    }
    #note: here i am directly returning the hardcoded values, but to add the functionallity i have created backend folder
    # we can add the logic there and call it here.