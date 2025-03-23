def calculate_total(price, tax_rate=0.08):
    return price + (price* tax_rate)


order_price = 50

total_prices = calculate_total(order_price)
print(f"The total price for the order ${total_prices}")


""" List and list cpmprehensions : list stores multiple items, and list copmprehensions provides 
a concise way to create lists:  """

steps = [5000, 7000, 8000, 6000, 10000]  # Steps per day
colories_burned = [step *0.04 for step in steps]

print(f"the colories burned for each steps are :  ${colories_burned}")


""" Dictionaries is key value store for structed data  """

product = {
    "name":"Wireless Headphones",
    "price":79.99,
    "stock ":25,
    "categories":"Electronics"
}

print(product["name"], "-", product["price"])