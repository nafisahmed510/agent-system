REGISTRY = {}

def tool(func):
    REGISTRY[func.__name__] = func
    return func

@tool
def add(a, b):
    return a + b

@tool
def shout(text):
    return text.upper() + "!"

print(REGISTRY)

print(add(2, 3))
print(shout("hello"))