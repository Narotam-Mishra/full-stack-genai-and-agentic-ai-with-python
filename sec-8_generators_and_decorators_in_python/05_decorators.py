
# decorators example

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("before function runs")
        func()
        print("after function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators")

greet()
print("func name:",greet.__name__)