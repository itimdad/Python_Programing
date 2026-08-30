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
students[0] = "Vijay"
print(students)
print(type(students))

#tuple data type (ordered +immutable + duplicates allowed)
ids = (2,5,7,9,0,1)
courses = ("AI", "Python", "Java")
print(ids)
print("courses => ", courses)
print(type(ids))

#set data type (unordered + Mutable + No Duplicates)
skills = {"Java", "SonarQube", "Maven", "Gradle", "Vunerability"}
print(skills)
print(type(skills))