#model stops while repsonding by showing reason, in this case asking for a tool.
#the response is in pieces now depending on the input
#since the pieces can differ, it's best to look into the entire output before picking the first piece as the tool request
#the values are all coming out as a Python dictionary but if a direct API call is made, then the values need to be converted manually

import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

get_weather_tool = {
    "name": "get_weather",
    "description": "Get the current weather for a given location. Use this whenever the user asks about weather conditions in a specific place.",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city or place to get the weather for, e.g. 'Queens' or 'San Francisco'."
            }
        },
        "required": ["location"]
    }
}

response = client.messages.create(
    model = "claude-haiku-4-5-20251001",
    max_tokens = 1024,
    tools = [get_weather_tool],
    messages=[{"role": "user", "content": "What should I wear in Queens today?"}]
)

print(response)

print(response.stop_reason)
print(response.content)
print([type(item) for item in response.content])
print(len(response.content))
print([b.type for b in response.content])