#variables
import sys
name = "Imdad"
age = 20

print(name)
print(age)
print(type(name))
print(type(age))

print(sys.getsizeof(name))

#complex data type
number = 5 + 3j
print(number)
print(type(number))
print(sys.getsizeof(number))

#list data type(ordered + mutable + duplicates allowed)
students = ["Aman", "Ajay", "Karan", "Aman"]
print(students)
print(type(students))