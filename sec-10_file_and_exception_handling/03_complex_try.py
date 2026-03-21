
def server_chai(flavor):
    try:
        print(f"Prepare {flavor} chai")
        if flavor == "unknown":
            raise ValueError("We don't know this flavor")
    except ValueError as e:
        print("Error: ",e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")

server_chai("masala")
server_chai("unknown")
