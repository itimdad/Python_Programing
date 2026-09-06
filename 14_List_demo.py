#List data structure

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
print(items[-1])
print(items[-2])

nums = [10,20,30,40,50,60]
#List slicing => It is used to get part of the list
print(nums)  #it returns all list elements

print(nums[1:4])   #start index is exclusive and end index is exclusive

print(nums[:4])    #returns from 0 index to 3 index last index will be excluded

print(nums[2:])   #prints from 2 index to end

print(nums[::2])  #step by 2 (increased by 2)

print(nums[:: -1])  #print in reverse order