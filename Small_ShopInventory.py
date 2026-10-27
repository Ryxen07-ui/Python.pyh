shop_name = "Smart Shop"
owner = "Mg Mg"
total_sales = 250000
is_open = True

products = ["rice", "oil", "sugar", "milk"]
new_products = ["coffee", "tea"]

 # (1) For Data Types

print("Shop Name:", shop_name)
print(type(shop_name))

print("Owner:", owner)
print(type(owner))

print("Total Sales:", total_sales)
print(type(total_sales))

print("Is_Open:", is_open)
print(type(is_open))

print("Products:", products)
print(type(products))

print("New Products:", new_products)
print(type(new_products))

# (2) For Sales Target Achieved

Total_Sales = int(input(" Enter the total sales: "))
if Total_Sales >= 200000:
    print("Sales target achieved")
else:
    print("Sales target not achieved")

#(3) For "Print the first, second, and last products"
print("The first prodcuts:", products[0])
print("The second products:", products[1])
print("The last prodcuts:", products[3])

#(4) Change "Sugar" to "Salt"
products[2] = "Salt"
print(products)

#(5)  Add "eggs" using append()
products.append ("Eggs")
print(products)
new_products.append("Eggs")
print(new_products)

#(6)  Insert "bread" at index 1 using extend()
products.insert(1, "bread")
print(products)
new_products.insert(1, "bread")
print(new_products)

#(7)  For Add all items from new_products using extend()
products.extend(new_products)
print(products)
new_products.extend(products)
print(new_products)

#(8)  For remove "oil" using remove()
products.remove("oil")
print(products)

#(9) For Remove the last product using pop()
products.pop()
print(products)
new_products.pop()
print(new_products)

#(10) For Delete the item at index 0 using del.
del products[0]
print(products)
del new_products[0]
print(new_products)

#(11) For Print the final product list.
print("The Final prodcut list:", products)
print("The Final product list:", new_products)
