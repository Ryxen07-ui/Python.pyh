hotel_name = "Crown Hotel"
total_rooms = 30
room_price = 50000.0
is_open = True

room_types = ["standard", "deluxe", "family", "suite"]
new_room_types = ["premium", "executive"]

# (1) print all variables and their data types
print("hotel name:", hotel_name)
print(type(hotel_name))

print("total rooms:", total_rooms)
print(type(total_rooms))

print("room price:", room_price)
print(type(room_price))

print("is_open :", is_open)
print(type(is_open))

print("room types: ", room_types)
print(type(room_types))

print("New Room Types:" , new_room_types)
print(type(new_room_types))

# (2) if _____ else
total_rooms = int(input("Enter the rooms:"))
if total_rooms >= 20:
    print("Enough rooms available")
else:
    print("Limited rooms available")

# (3) print the first, second, and last room types
print("the first room:", room_types[0])
print("the second room:", room_types[1])
print("the last room:", room_types[3])

# (4) Change "deluxe" to "deluxe twin"
room_types[1] = "deluxe twin"
print(room_types)

# (5) add "single" using append()
room_types.append("single")
print(room_types)

# (6) insert "double" at index 1 
room_types.insert(1, "double")
print(room_types)
new_room_types.insert(1, "double")
print(new_room_types)

# (7) use extend() to add new_room_types
room_types.extend(new_room_types)
print(new_room_types)

# (8) Remove "family"
room_types.remove("family")
print(room_types)

# (9) Use pop() to remove the last item
room_types.pop()
print(room_types)
new_room_types.pop()
print(new_room_types)

# (10) delete the item at index 0 using del
del room_types[0]
print(room_types)
del new_room_types[0]
print(new_room_types)

# (11) print the final room-type list
print("final room-type:", room_types)
print("final room-type:", new_room_types)