restaurant_name = "Golden Restaurant"
daily_customers = 45
daily_income = 350000.0
is_open = True

menu = ["fried rice", "noodles", "soup", "salad"]
new_menu = ["coffee", "juice"]

# (1)  Print all variables and their data types

print("Restaurant Name:", restaurant_name)
print(type(restaurant_name))

print("Daily Customers:", daily_customers)
print(type(daily_customers))

print("Daily Income:", daily_customers)
print(type(daily_income))

print("Is_Open:", is_open)
print(type(is_open))

print("Menu:", menu)
print(type(menu))

print("New Menu:", new_menu)
print(type(new_menu))

# (2) If ...... else
daily_customers = int(input("Enter the daily customers: "))
if daily_customers >= 40:
    print("Good Customer Traffic")
else:
    print("Need more Customers")

# (3) Print the fist, third, and last menu items
print("The first menu item:", menu[0])
print("The third menu item:", menu[2])
print("The last menu items:", menu[3])
print("The first new menu item:", new_menu[0])


# (4) Change "Sopu" to "Chicken Soup"
menu[2] = "Chicken Soup"
print(menu)

#(5) Add "Burger" using append()
menu.append("burger")
print(menu)
new_menu.append("burger")
print(new_menu)

#(6) Insert "pizza" at index 1
menu.insert(1, "Pizza")
print(menu)

# (7) Use extend() to add new_menu
menu.extend(new_menu)
print(menu)

# (8) Remove "Salad"
menu.remove("salad")
print(menu)

#(9) Use pop() to remove the last item
menu.pop()
print(menu)
new_menu.pop()
print(new_menu)

#(10) Delete the item at index 0 using del
del menu[0]
print(menu)
del new_menu[0]
print(new_menu)

#(11) Print the final menu
print("The Final menu:", menu)
print("The Final new menu:", new_menu)