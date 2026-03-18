
from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwwargs):
        print(f"before Calling: {func.__name__}")
        res = func(*args, **kwwargs)
        print(f"after Finished: {func.__name__}")
        return res
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")

brew_chai("Masala")
# brew_chai("Ginger")