
# generator comprehension

daily_sales = [5,10,12,7,3,8,9,15]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print("Total Cups Sum:", total_cups)