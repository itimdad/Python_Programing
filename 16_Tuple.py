#ordered, immutable, allows duplicates, faster than list


numbers = ()
print(numbers)

courses = ("Java", "Python", "CSS")
print(courses)
print(type(courses))
print(courses[0:2])

print(courses.index("Java"))


#tuple packing
student = "Imdad", "GKP", 70
print(student)
print(type(student))

#tuple unpacking
student = ("Imdad", "GKP", 70)
name, place, money = student
print(name)
print(place)
print(money)

#convert tuple into list
courses = ("Java", "Python", "CSS")
courses_list = list(courses)
print(courses_list)

#check value exist in tuple or not
if "Python" in courses:
    print("Python is in the tuple")
else:
    print("Python is not in the tuple")
