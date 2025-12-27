from graph import build_graph
from langchain_core.messages import HumanMessage

graph = build_graph()

result = graph.invoke({
    "messages": [
        HumanMessage(content="I’d like to order a large Margherita at 8 pm")
    ]
})


print(result)
# Example usage