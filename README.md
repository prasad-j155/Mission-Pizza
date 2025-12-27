# Mission-Pizza
AI Pizza Ordering System using MCP + LangChain
This project demonstrates how to build an AI-powered pizza ordering system using LangChain agents and an MCP-style tool server built with FastAPI.
## The agent can:
- Take a pizza order from natural language
- Ask follow-up questions (like delivery time)
- Call backend tools (order, schedule, track)
- Orchestrate multiple agents using a graph-based flow



## Key Concepts Used
- LangChain Agents
- MCP-style Tool Server
- FastAPI as MCP Server
- LangGraph for orchestration
- Groq LLM API (free tier) (https://console.groq.com/keys)
- OpenAPI → Tool conversion
- Async agent execution



## Why MCP?
- MCP (Model Context Protocol) provides a standard way to expose tools to LLM agents.

### In this project:
- APIs are exposed via FastAPI
- Tools are auto-generated from OpenAPI
- Agents call tools using structured JSON inputs
- I did not use FastMCP, because it was not effective for this use case.
- Instead, I used FastAPI as an MCP-compatible server, which gave better control and flexibility.

 ## Project Architecture
- User -> LangChain Agent (Groq LLM) -> LangGraph Orchestrator -> MCP Tool Server (FastAPI) -> Backend Logic (Order / Schedule / Track)

## Project Structure
### order-pizza
#### agents
- pizza_agent.py – Handles pizza ordering logic
- scheduler_agent.py – Handles delivery scheduling
- pizza_orchestrator.py – Main agent runner

#### backend
- mock_backend.py – get_menu, place_order, track_order
- scheduler_backend.py – schedule_delivery logic
- graph.py – LangGraph orchestration

#### mcp
- mcp_server.py – FastAPI MCP server
- openapi_to_mcp.py – Converts OpenAPI to agent tools

#### openapi
- pizza.yaml – API specification

calendar.py – Generates .ics delivery calendar event
output-study.py – Output analysis and human-readable logs
requirements.txt – Python dependencies
README.md – Project documentation


## How to Run the Project
- Install Dependencies-
  - pip install -r requirements.txt
  - Set Groq API Key (LLM)
    - set GROQ_API_KEY=your_api_key_here( i have called directly in the function, but that’s not recommended)
    - Groq is used because it provides free limited LLM calls, making it ideal for demos.

## Run the MCP Server (FastAPI)
- uvicorn mcp.mcp_server:app --reload

- This starts the tool server that exposes:
  - Place order
  - Track order
  - Schedule delivery



- Run the Agent
 - python .\agents\pizza_orchestrator.py

- Example input handled by the agent:
 - "I’d like to order a large Margherita at 8 pm"

## The agent will:
- Understand the intent
- Call the correct tools
- Schedule delivery



## Analyze Agent Output
- To make agent output human-readable, I created:
- python output-study.py 
 - (for now i have just copy-pasted my output, but we can directly fetch the output from Pizza_orchetrator.py)

## This script:
- Takes raw agent output
- Extracts messages
- Prints clean conversation flow



 ## Important Notes
- The show_menu API exists, but I have not explicitly called it yet
- The agent logic supports it , calling can be enabled later
- No UI chatbot yet (planned)
- No FastMCP used (for this project I used FastApi)



## Future Enhancements
- Planned improvements include:
- Chatbot UI
- Web-based chatbot interface
- User-friendly conversation flow
- Smart Scheduling
  - If user does not specify time, agent auto-schedules delivery based on availability
- Compensation Logic
  - If delivery is delayed Agent automatically assigns discounts or offers

- Order Analytics
  - Track popular pizzas
  - Optimize delivery times

- CI/CD with GitHub Actions
  - Add GitHub Actions pipelines to:
  - Automatically test MCP tools and agent workflows on every PR.
  - Validate OpenAPI → MCP tool conversion.
  - Run linting and formatting checks.
  - Ensure agents can successfully call tools end-to-end before merging.



## Learning Outcomes
- This project demonstrates:
- How to convert APIs into agent tools
- How agents reason and call tools
- How to orchestrate multi-agent workflows



