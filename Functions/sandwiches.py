def sandwich_order(*orders):
    print("\nHere your orders:")
    for order in orders:
        print(order)


sandwich_order('cheese')
sandwich_order('spinach', 'pepper', 'beef')
sandwich_order('cheese extra', 'sauges', 'hamberger', 'chicken sandwich')
