import typing
import inspect
REGISTRY = {}

def tool(func):
    hints = typing.get_type_hints(func)
    properties = {}
    for param_name, param_type in hints.items():
        if param_name == "return":
            continue
        properties[param_name] = {"type": TYPE_MAP[param_type]}

    signature = inspect.signature(func)
    required = []
    for param_name, param in signature.parameters.items():
        if param.default is inspect.Parameter.empty:
            required.append(param_name)

    schema = {
        "name": func.__name__,
        "description": func.__doc__,
        "input_schema": {
            "type": "object",
            "properties": properties,
            "required": required,
        },
    }
    func.schema = schema
    REGISTRY[func.__name__] = func
    return func

TYPE_MAP = {
    str: "string",
    int: "integer",
    bool: "boolean",
}

@tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@tool
def shout(text: str) -> str:
    """Convert text to uppercase and add an exclamation mark."""
    return text.upper() + "!"

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a given location"""
    return "72 degrees F and sunny in " + location

if __name__ == "__main__":
    print(REGISTRY)
    print(add.schema)