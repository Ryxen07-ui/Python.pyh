business_name = "Quick Online Shop"
customer_name = "Su Su"
order_total = 75000
is_paid = True

orders = ["phone case", "charger", "earphones", "power bank"]
new_orders = ["USB cable", "phone stand"]

# (1) print all variables and their data types
print("business name:", business_name)
print(type(business_name))

print("customer name:", customer_name)
print(type(customer_name))

print("Total order:", order_total)
print(type(order_total))

print("Is paid:", is_paid)
print(type(is_paid))

print("orders: ", orders)
print(type(orders))

print("new order:", new_orders)
print(type(new_orders))

# (2) If ----- else
order_total =int(input("Enter the total order:"))
if order_total >= 50000:
    print("Large order")
else:
    print("Small order")

# (3) Change "charger" to "fast charger"
orders[1] = "fast charger"
print(orders)

# (4) put the first, second, and last order items
print("first order: ", orders[0])
print("second order:", orders[1])
print("last order:", orders[3])

# (5) add 'screen protector' using append()
orders.append("screen protector")
print(orders)

# (6) insert 'phone holder' at index 1
orders.insert(1, "phone holder")
print(orders)

# (7) use extend() to add new_order
orders.extend(new_orders)
print(orders)

# (8) Remove "earphones"
orders.remove("earphones")
print(orders)

# (9) Use pop() to remove the last item
orders.pop()
print(orders)
new_orders.pop()
print(new_orders)

# (10) Delete the item at index 0 using del 
del orders[0]
print(orders)
del new_orders[0]
print(new_orders)

# (11) Print the final order list
print("final order list:", orders)
print("Final order list:", new_orders)