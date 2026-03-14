
# Dictionary Comprehension

tea_prices_inr = {
    "Masala Chai": 40,
    "Green Chai": 50,
    "Lemon Tea": 100
}

tea_prices_usd = {tea: price / 93 for tea, price in tea_prices_inr.items()}
print("Tea Price in USD:", tea_prices_usd)