from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

response={'messages': [HumanMessage(content='I’d like to order a large Margherita at 8 pm', additional_kwargs={}, response_metadata={}, id='722f3b9e-738f-4fca-bf05-3aad7ac17c37'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'pa1sf38sn', 'function': {'arguments': '{"delivery_time":"8 pm","pizza_name":"Margherita","quantity":1,"size":"large"}', 'name': 'place_order'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 38, 'prompt_tokens': 347, 'total_tokens': 385, 'completion_time': 0.077778718, 'completion_tokens_details': None, 'prompt_time': 0.034049402, 'prompt_tokens_details': None, 'queue_time': 0.053477018, 'total_time': 0.11182812}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_dae98b5ecb', 'service_tier': 'on_demand', 'finish_reason': 'tool_calls', 'logprobs': None, 'model_provider': 'groq'}, id='lc_run--019b5f99-2a15-7921-b48c-876b5d87d29a-0', tool_calls=[{'name': 'place_order', 'args': {'delivery_time': '8 pm', 'pizza_name': 'Margherita', 'quantity': 1, 'size': 'large'}, 'id': 'pa1sf38sn', 'type': 'tool_call'}], usage_metadata={'input_tokens': 347, 'output_tokens': 38, 'total_tokens': 385}), ToolMessage(content='{"order_id": "ORD-BDBF60", "pizza": "Margherita", "size": "large", "quantity": 1, "delivery_time": "8 pm", "total_price": 399, "status": "order_confirmed"}', name='place_order', id='8ce9f936-afa7-46ef-ad84-c9285b5f1aa2', tool_call_id='pa1sf38sn'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'p17700phw', 'function': {'arguments': '{"order_id":"ORD-BDBF60"}', 'name': 'track_order'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 449, 'total_tokens': 469, 'completion_time': 0.030079334, 'completion_tokens_details': None, 'prompt_time': 0.025094223, 'prompt_tokens_details': None, 'queue_time': 0.060228907, 'total_time': 0.055173557}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_c06d5113ec', 'service_tier': 'on_demand', 'finish_reason': 'tool_calls', 'logprobs': None, 'model_provider': 'groq'}, id='lc_run--019b5f99-2b42-7041-b8ed-19b9ea880487-0', tool_calls=[{'name': 'track_order', 'args': {'order_id': 'ORD-BDBF60'}, 'id': 'p17700phw', 'type': 'tool_call'}], usage_metadata={'input_tokens': 449, 'output_tokens': 20, 'total_tokens': 469}), ToolMessage(content='{"order_id": "ORD-BDBF60", "status": "preparing", "estimated_delivery": "30 minutes"}', name='track_order', id='eda68c7e-7c83-4151-bc65-bafccb54a85f', tool_call_id='p17700phw'), AIMessage(content='Your order has been confirmed and is being prepared for delivery. The estimated delivery time is 30 minutes. You can continue to track your order using the order ID: ORD-BDBF60.', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 40, 'prompt_tokens': 505, 'total_tokens': 545, 'completion_time': 0.121236965, 'completion_tokens_details': None, 'prompt_time': 0.110892958, 'prompt_tokens_details': None, 'queue_time': 0.053934351, 'total_time': 0.232129923}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_c06d5113ec', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'groq'}, id='lc_run--019b5f99-2c2b-7371-965a-05e7b85b8a4d-0', usage_metadata={'input_tokens': 505, 'output_tokens': 40, 'total_tokens': 545}), AIMessage(content=' \n\n', additional_kwargs={'tool_calls': [{'id': '6x59tg632', 'function': {'arguments': '{"delivery_time":"8 pm","order_id":"ORD-BDBF60","pizza_name":"Margherita"}', 'name': 'schedule_delivery'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 38, 'prompt_tokens': 457, 'total_tokens': 495, 'completion_time': 0.076989429, 'completion_tokens_details': None, 'prompt_time': 0.023566341, 'prompt_tokens_details': None, 'queue_time': 0.063070149, 'total_time': 0.10055577}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_c06d5113ec', 'service_tier': 'on_demand', 'finish_reason': 'tool_calls', 'logprobs': None, 'model_provider': 'groq'}, id='lc_run--019b5f99-2d92-7c90-807a-290a6f89dc2d-0', tool_calls=[{'name': 'schedule_delivery', 'args': {'delivery_time': '8 pm', 'order_id': 'ORD-BDBF60', 'pizza_name': 'Margherita'}, 'id': '6x59tg632', 'type': 'tool_call'}], usage_metadata={'input_tokens': 457, 'output_tokens': 38, 'total_tokens': 495}), ToolMessage(content='{"order_id": "ORD-BDBF60", "scheduled": true, "delivery_time": "8 pm", "calendar_event_created": true, "calendar_event_link": "calendar_link", "status": "delivery_scheduled"}', name='schedule_delivery', id='c475cb61-8f08-422a-b811-c407cd2ba4b7', tool_call_id='6x59tg632'), AIMessage(content='Your delivery has been scheduled for 8 pm. A calendar event has been created, and you can access it through the provided link: calendar_link. Your order is now ready for delivery.', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 39, 'prompt_tokens': 557, 'total_tokens': 596, 'completion_time': 0.125371258, 'completion_tokens_details': None, 'prompt_time': 0.028854963, 'prompt_tokens_details': None, 'queue_time': 0.065943756, 'total_time': 0.154226221}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_dae98b5ecb', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'groq'}, id='lc_run--019b5f99-2e9a-77a1-98f7-610807b5c4a3-0', usage_metadata={'input_tokens': 557, 'output_tokens': 39, 'total_tokens': 596})]}




#print(response["messages"]['content'])
print("\n=========== Human message ==============\n")
for msg in response["messages"]:
    if isinstance(msg, HumanMessage) and msg.content.strip():
        print("🤖 AI:", msg.content)

print("\n=========== AI message ==============\n")



for msg in response["messages"]:
    if isinstance(msg, AIMessage) and msg.content.strip():
        print("🤖 AI:", msg.content)

print("\n============= Tool message ============\n")


for msg in response["messages"]:
    if isinstance(msg, ToolMessage) and msg.content.strip():
        print("🤖 AI:", msg.content)

print("\n=========================\n")


"""
MESSAGE TYPES EXPLANATION (LangChain / LangGraph)

1. HumanMessage:
   Represents user input (e.g. "I’d like to order a pizza")
   Always the starting point
   No logic or tools executed here

2. AIMessage:
   Generated by the LLM
   Can be:
    a) Empty → when AI is deciding which tool to call
    b) Text → user-facing response shown in UI
    Final AIMessage contains the actual reply to the user

3. ToolMessage:
   Output returned by backend tools/functions
   Always structured data (dict / JSON)
   Not shown directly to users
   Used by AI to decide next actions

Typical Flow:
HumanMessage → AI (plan) → ToolMessage(s) → AI (final response)
"""
