
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

total_bill = calculate_bill(3, 20)
print("Total bill:",total_bill)
print("order for table 3:", calculate_bill(5, 30))