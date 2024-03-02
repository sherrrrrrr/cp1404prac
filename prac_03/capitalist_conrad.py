import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.175  # 17.5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00
OUTPUT_FILE = "stock_prices.txt"

price = INITIAL_PRICE
print(f"Starting price: ${price:,.2f}")

out_file = open(OUTPUT_FILE, 'w')

day = 1
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {day} price is: ${price:,.2f}")
    print(f"${price:,.2f}", file=out_file)
    day += 1

out_file.close()

