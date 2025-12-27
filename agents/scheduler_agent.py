from langchain_groq import ChatGroq
from langchain.agents import create_agent
from schedular_tools import schedule_delivery



def scheduling_agent():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key="" ,

    )
     
    tools = [schedule_delivery]

    agent = create_agent(
        model=llm,
        tools=tools
        
    )

    return agent
