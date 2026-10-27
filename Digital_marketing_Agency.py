agency_name = "Creative Digital"
team_size = 8
project_fee = 450000.0
is_accepting_clients = True

services = ["web design", "social media", "SEO", "branding"]
new_services = ["video editing", "AI automation"]

# (1) Print all variables and their data types
print("Agency name:", agency_name)
print(type(agency_name))

print("Team size:", team_size)
print(type(team_size))

print("Project fee:", project_fee)
print(type(project_fee))

print("Is accepting clients: ", is_accepting_clients)
print(type(is_accepting_clients))

print("Service:", services)
print(type(services))

print("New Service:", new_services)
print(type(new_services))

# (2) If______eles
project_fee = int(input("Project Fee:"))
if project_fee >= 400000:
    print("High-Value Project") 
else:
    print("Standard Project")

# (3) print the first, second, and the last services
print("The first service:", services[0])
print("the second service:", services[1])
print("the last service:", services[3])

# (4) Change "SEO" to "SEO Optimization"
services[1] = "SEO Optimization"
print(services)

# (5) Add "UI/UX design" using append()
services.append("UI/UX design")
print(services)
new_services.append("UI/UX design")
print(new_services)

# (6) Insert "content writing" at index 1 
services.insert(1, "content writing")
print(services)
new_services.insert(1, "content writing")
print(new_services)

# (7) Use extend() to add new_services
services.extend(new_services)
print(services)

# (8) Remove "branding"
services.remove("branding")
print(services)

# (9) Use pop() to remove the last item
services.pop()
print(services)
new_services.pop()
print(new_services)

# (10) Delete the item at index 0 using del
del services[0]
print(services)
del new_services[0]
print(new_services)

# (11) Print the final serive list
print("Final service list:", services)
print("Final service list:", new_services)