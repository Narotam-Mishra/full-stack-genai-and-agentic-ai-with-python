
def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "lemon"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai....")

try:
    brew_chai("ginger")
    brew_chai("mint")
except ValueError as e:
    print(e)
