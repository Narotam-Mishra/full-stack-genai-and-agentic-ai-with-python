
def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [70, 90, 50]

for price in orders:
    actual_amount = add_vat(price, 15)
    print(f"original: {price}, final with VAT: {actual_amount}")