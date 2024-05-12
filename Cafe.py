menu = {
    "PIZZA": 199,
    "VEG BURGER": 59,
    "PLATE NEGGETS": 65,
    "FRENCH FRIES": 70,
    "CORN SANDWICH": 50,
    "VEG SANDWICH": 50,
    "SAMOSA": 20,
    "PUFF": 20
}

print("\t\t    Welcome to Darshan's Cafe\n")
print("Today's special Menu\n")
print("1. PIZZA = 199rs\n2. VEG BURGER = 59rs\n3. PLATE NUGGETS = 65rs\n4. FRENCH FRIES = 70rs\n5. CORN SANDWICH = 120rs\n6. VEG SANDWICH = 90rs\n7. SAMOSA = 20rs\n8. PUFF = 20rs \n")

order_total = 0
ordered_items = []

item1 = input("Can I Have A Order please..? =\n").upper()
if item1 in menu:
    order_total += menu[item1]
    ordered_items.append(item1)
    print(f"Your Item {item1} will be there in 10 mins")
else:
    print(f"The Ordered item {item1} is not yet Ready")

another_order = input("Do you want to Order More...!(YES/NO) = \n").upper()
if another_order == "YES":
    item3 = input("Your Second Order Please..!").upper()
    if item3 in menu:
        order_total += menu[item3]
        ordered_items.append(item3)
        print(f"Your Item {item3} will be there in 15 mins\n")
    else:
        print(f"The Ordered item {item3} is not yet Ready\n")

print("Your Order details are :", ', '.join(ordered_items))
print(f"The Total Bill of ordered Items = {order_total}rs",)
print("\t\t   Thank You Visit Again..!")
