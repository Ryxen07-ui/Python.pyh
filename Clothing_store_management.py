store_name = "Fashion House"
staff_count = 5
monthly_income = 850000.0
is_open = True

clothes = ["shirt", "jeans", "jacket", "dress"]
new_clothes = ["skirt", "hoodie"]

# (1) print all variable and their data types 
print("Store name:", store_name)
print(type(store_name))

print("Staff count:", staff_count)
print(type(staff_count))

print("Monthly Income:", monthly_income)
print(type(monthly_income))

print("Is_Open:", is_open)
print(type(is_open))

print("Clothes:", clothes)
print(type(clothes))

print("New Clothes:", new_clothes)
print(type(new_clothes))

# (2) If ------ else
monthly_income = int(input("Enter the monthly_income: "))
if monthly_income >= 800000:
    print("Income target achieved")
else:
    print("Income target not achieved")

# (3) Print the first, second, and last clothing items
print("The first clothing item:", clothes[0])
print("The second clothing item:", clothes[2])
print("The last clothing item:" clothes[3])

# (4) Change "Jeans" to "black jeans"
clothes[1] = "black jeans"
print(clothes)

# (5) Insert "T-shirt" at index 1
clothes.insert(1, "T-shirt")
print(clothes)
new_clothes.insert(1, "T-shirt")
print(new_clothes)

# (6) add "sweater" using append()
clothes.append("sweater")
print(clothes)
new_clothes.append("sweater")
print(new_clothes)

# (7) Use extend() to add new_clothes
clothes.extend(new_clothes)
print(clothes)

# (8) Remove "jacket"
clothes.remove("jacket")
print(clothes)

# (9) Use pop() to remove the last item
clothes.pop()
print(clothes)
new_clothes.pop()
print(new_clothes)

# (10) delete the item at index 0 using del
del clothes[0]
print(clothes)
del new_clothes[0]
print(new_clothes)

# (11) Print the final clothing list
print("final clothing list: , clothes")
print("final clothing list:" , new_clothes)