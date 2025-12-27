from langgraph.graph import StateGraph
from pizza_agent import ordering_agent
from scheduler_agent import scheduling_agent

def build_graph():
    graph = StateGraph(dict)

    order_agent = ordering_agent()
    schedule_agent = scheduling_agent()

    # Add nodes
    graph.add_node("order", order_agent)
    graph.add_node("schedule", schedule_agent)

    # Connect order -> schedule
    graph.add_edge("order", "schedule")

    # Entry and finish points
    graph.set_entry_point("order")
    graph.set_finish_point("schedule")

    return graph.compile()
