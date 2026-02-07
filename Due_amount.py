def calculate_change(*, price: float, payment: float) -> None:
    if payment < price:
        print("Not enough money!")
    else:
        change = payment - price
        dollars = int(change)
        cents = int(round((change - dollars) * 100))
        print("Change:")
        print("Dollars:", dollars)
        print("Cents:", cents)


item_price = float(input("Enter price of item: $"))
amount_given = float(input("Enter amount given: $"))


calculate_change(price=item_price, payment=amount_given)


