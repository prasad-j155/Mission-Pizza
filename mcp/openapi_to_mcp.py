import yaml
from backend.mock_backend import get_menu, place_order, track_order
from backend.scheduler_backend import schedule_delivery

def load_openapi(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def generate_tools(openapi_spec):
    tools = {}

    for path, methods in openapi_spec["paths"].items():
        for method, meta in methods.items():
            name = f"{method}_{path.replace('/', '_').replace('{','').replace('}','')}"

            if path == "/menu":
                tools[name] = {
                    "description": meta["summary"],
                    "handler": lambda args=None: get_menu()
                }

            elif path == "/order":
                tools[name] = {
                    "description": meta["summary"],
                    "handler": lambda args: place_order(**args)
                }

            elif path == "/order/{order_id}":
                tools[name] = {
                    "description": meta["summary"],
                    "handler": lambda args: track_order(args["order_id"])
                }

            # ✅ ADD THIS
            elif path == "/schedule":
                tools[name] = {
                    "description": meta["summary"],
                    "handler": lambda args: schedule_delivery(
                        args["order_id"],
                        args["time"]
                    )
                }

    return tools
