#model stops while repsonding by showing reason, in this case asking for a tool.
#the response is in pieces now depending on the input
#since the pieces can differ, it's best to look into the entire output before picking the first piece as the tool request
#the values are all coming out as a Python dictionary but if a direct API call is made, then the values need to be converted manually

import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv
from tools import REGISTRY

load_dotenv()
client = Anthropic()



response = client.messages.create(
    model = "claude-haiku-4-5-20251001",
    max_tokens = 1024,
    tools = [f.schema for f in REGISTRY.values()],
    messages=[{"role": "user", "content": "Add 4 & 8"}]
)

print(response)

print(response.stop_reason)
print(response.content)
print([type(item) for item in response.content])
print(len(response.content))
print([b.type for b in response.content])