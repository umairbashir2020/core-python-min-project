# Define the menu of restaurant

menu_list = {
    "burger": 150,
    "pizza": 700,
    "french fries": 100,
    "sandwich": 70,
    "milkshake": 100,
    "chicken nuggets": 120
}
# Greet
print('Welcome to PYTHON RESTAURANT')

print(" Burger: Rs150\n Pizza: Rs700\n French Fries: Rs100\n Sandwich: Rs70\n MilkShake: Rs100\n Chicken Nuggets: Rs120")

order_count = 0 # 80 + 70 = 150
while True:
    item_1 = input("Enter the name of item you want to order = ").strip().lower()

    if item_1 in menu_list:
        order_count += menu_list[item_1] #0 +50
        print(f"Your item {item_1.title()} has been added to your order!") #.title() in messages so names look nice (e.g., "burger" → "Burger").

    else:
        print(f"Ordered item {item_1.title()} is not available yet!")

    print(f"The total amount of items is Rs{order_count:,}") #inside {} tells Python to add commas as thousands separators.
    
    another_item = input("Do you want to add another item? Yes/No = ")
    
    if another_item != "yes":
        break
        
print(f"The total amount of items is Rs{order_count:,}")
