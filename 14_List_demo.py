#List data structure
from typing import List

courses = ["Java", "Python", "PHP", "HTML", "C++"]
print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])
print(courses[4])

items = ["Mouse", "Keyboard", "Monitor", "LCD", "CPU"]
#positive index access (start from left to right --->)
print(items[1])
print(items[3])

#Negative index access(start from right to left <-----)
print("Ulta",items[-1])
print("Ulta",items[-2])

nums = [10,20,30,40,50,60]
#List slicing => It is used to get part of the list
print(nums)  #it returns all list elements

print(nums[1:4])   #start index is exclusive and end index is exclusive

print(nums[:4])    #returns from 0 index to 3 index last index will be excluded

print(nums[2:])   #prints from 2 index to end

print(nums[::2])  #step by 2 (increased by 2)

print(nums[:: -1])  #print in reverse order


##List functions
coursess = ["Java", "Python", "PHP", "HTML", "C++", "DSA"]
#for loop in courses
for course in coursess:
    print(course)
#append => add element at the end
print(courses)

#insert => add element in specific position
coursess.insert(0, "COA")
print(coursess)

#extends => add two list
frontend=["HTML", "CSS", "JavaScript"]
backend=["JAVA", "SPRING", "Spring Boot", "SQL", "Docker", "K8s"]
frontend.extend(backend)
print(frontend)

#remove => remove specified value
coursess.remove("Java")
print(coursess)

#pop => remove based on index, without index will remove last
numbers = [10,20,30,40,50,60]

#removes last
numbers.pop()
print(numbers)

#removes index wise
numbers.pop(1)
print(numbers)

#clear => Removes all elements from the list
# numbers.clear()
# print(numbers)

#del function => delete an elemnet or entire list
del numbers[0]
print(numbers)