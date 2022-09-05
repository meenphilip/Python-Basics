sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'cheese', 'tuna']
finished_list = []
while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        print("We have run out of Pastrami")
        sandwich_orders.remove('pastrami')
    else:
        last_item = sandwich_orders.pop()
        print("I made your " + last_item + " sandwich")
        finished_list.append(last_item)

print("\n------------")
print("\nHere is the filtered list:")
for order in finished_list:
    print(order)
