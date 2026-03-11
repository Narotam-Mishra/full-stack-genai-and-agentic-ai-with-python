
def chai_flavour(flavour="masala"):
    """ Return the flavour of chai"""
    chai = "ginger"
    return flavour

print(chai_flavour.__doc__)
print(chai_flavour.__name__)

def generate_bill(chai=0, samosa=0):
    """
    calculate total bill

    :params chai: Number of chai cups
    :params samosa: number of samosa (10 rupees each)
    :return: (total amount, thank you message)
    """
    total = chai*10 + samosa*10
    return total, "Thank you"