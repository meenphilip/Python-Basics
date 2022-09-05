sandwich_orders = ['tuna', 'cheese', 'fish', 'vegetable', 'cheese']

finished_sandwich = []
while sandwich_orders:
    last_item = sandwich_orders.pop()
    print("I made your " + last_item + " sandwich order")
    finished_sandwich.append(last_item)

print("\nHere is the list of sandwiches made:")
for order in finished_sandwich:
    print(order)
