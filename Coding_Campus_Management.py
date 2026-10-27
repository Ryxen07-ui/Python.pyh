campus_name = "NuraDev"
student_count = 35
course_fee = 150000
is_registration_open = True

courses = ["Python", "Web Development", "Flutter", "Computer Basic"]
new_courses = ["AI for Life and Work", "Rust Programming"]

# (1) print all variables and their data types
print("Campus Name: ", campus_name)
print(type(campus_name))

print("Student count:", student_count)
print(type(student_count))

print("Course Fee:", course_fee)
print(type(course_fee))

print("Is_Registration: ", is_registration_open)
print(type(is_registration_open))

print("Courses:", courses)
print(type(courses))

print("New Courses:", new_courses)
print(type(new_courses))

# (2) If______else
student_count = int(input("Enter Student count:"))
if student_count >= 30:
    print("Enrollment target achieved")
else:
    print("Need more students")

# (3) Print the first, second , and last courses
print("The first course:", courses[0])
print("The second course:", courses[1])
print("The last course:", courses[3])

# (4) Change "flutter" to "Mobile App Development"
courses[1] = "Mobile App Development"
print(courses)

# (5) Add "UI/UX Design" using append()
courses.append("UI/UX Design")
print(courses)
new_courses.append("UI/UX Design")
print(new_courses)

# (6) Insert "Scratch Coding" at index 1
courses.insert(1, "Scratch Coding")
print(courses)
new_courses.insert(1, "Scratch Coding")
print(new_courses)

# (7) Use extend() to add new_courses
courses.extend(new_courses)
print(courses)

# (8) Remove "Computer Basic"
courses.remove("Computer Basic")
print(courses)

# (9) Use pop() to remove the last item
courses.pop()
print(courses)
new_courses.pop()
print(new_courses)

# (10) Delete the item at index 0 using del
del courses[0]
print(courses)
del new_courses[0]
print(new_courses)

# (11) Print the final course list
print("Final course list:", courses)
print("Final course list:", new_courses)