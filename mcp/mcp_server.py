from fastapi import FastAPI
from mcp.openapi_to_mcp import load_openapi, generate_tools

app = FastAPI(title="Pizza MCP Server")

openapi_spec = load_openapi("openapi/pizza.yaml")
TOOLS = generate_tools(openapi_spec)

@app.get("/tools")
def list_tools():
    return {
        name: tool["description"]
        for name, tool in TOOLS.items()
    }

@app.post("/call_tool/{tool_name}")
def call_tool(tool_name: str, arguments: dict = None):
    if tool_name not in TOOLS:
        return {"error": "Tool not found"}

    handler = TOOLS[tool_name]["handler"]
    return handler(arguments)
