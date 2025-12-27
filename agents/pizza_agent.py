from langchain_groq import ChatGroq

#i am using free llm model ,provided by groq, we can use llama,gpt models for free(limited api calls)

from langchain.agents import create_agent
from pizza_tools import get_menu, place_order, track_order

ORDERING_SYSTEM_PROMPT = {"role": "system", "content": """
You are a Pizza Ordering Agent.
...
"""}
def ordering_agent():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key="" ,

    )
#we can create a single module for llm,and calling it rather than writing it multiple times
    tools = [get_menu, place_order, track_order]

    agent = create_agent(
        model=llm,
        tools=tools
        
    )

    return agent
