shop_name = "Tech World"
staff_name = "Aye Aye"
monthly_sales = 1200000
is_registered = True

products = ["laptop", "mouse", "keyboard", "monitor"]
new_products = ["webcam", "headphones"]

#(1) Print all variables and their data types
print("Shop Name:", shop_name)
print(type(shop_name))

print("Staff Name:", staff_name)
print(type(staff_name))

print("Monthly Sales:", monthly_sales)
print(type(monthly_sales))

print("Is_Registered:", is_registered)
print(type(is_registered))

print("Products:", products)
print(type(products))

print("New Products:", new_products)
print(type(new_products))

#(2) If ------ else
monthly_sales = int(input("Enter the monthly_sales: "))
if monthly_sales >= 1000000:
    print("Monthly Target achieved")
else:
    print("Monthly target not achieved")

#(3) Print the first, second, and last products
print("The first prodcut: ", products[0])
print("The second product: ", products[1])
print("The last product: ", products[3])

#(4) Change "mouse" to "wireless mouse"
products[1] = "Wireless Mouse"
print(products)

#(5) Add "printer" using append()
products.append("printer")
print(products)
new_products.append("printer")
print(new_products)

#(6) insert "USB cable" at index 1
products.insert(1, "USB cable")
print(products)
new_products(1, "USB cable")
print(new_products)

#(7) Use extend() to add new_products
products.extend(new_products)
print(products)

#(8) Remove "Keyboard"
products.remove("keyboard")
print(products)

#(9) Use pop() to remove the last item
products.pop()
print(products)
new_products.pop()
print(new_products)

#(10) Delete the item at index 0 using del
del products[3]
print(products)
del new_products[1]
print(new_products)

#(11) Print the final product list 
print("Final products:", products)
print("Final prodcuts:", new_products)