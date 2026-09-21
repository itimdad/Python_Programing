#some more functions in the list
from type_casting import numbers

nums = [1,2,3,4,0,1,2,8,9]
print(len(nums))
print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
#ascending order
print(nums)
nums.sort(reverse=True)
#Descending order
print(nums)


#Add elements in the list using for loop

#normal way
numbers = []
for i in range(1, 6):
    print(i, "Added in the list")
    numbers.append(i)
print(numbers)

#list comprehension
numbers = [i for i in range(1, 6)]
print(numbers)

#squares of a numbers using comprehension
numbers = [i * i for i in range(1,6)]
print(numbers)

#even number
even_nums = []
for i in range(1, 11):
    if i % 2 == 0:
        even_nums.append(i)

print("even nums=>", even_nums)

#even numbers using comprehension
even_nums = [ i  for i in range(1, 11) if i % 2 == 0]
print("even nums using comprehension =>", even_nums)

#Make all names in capital using comprehension

names = ["karan", "vijay", "jai",]
#using normal way
for name in names:
    print(name.upper())

#Using comprehension
#names = [name.upper() for name in names]
print([name.upper() for name in names])
print(names)

#student grade using comprehension
marks = [20, 33, 31,55, 20,99,60]

result = ["Passed" if mark >= 33 else "Failed" for mark in marks]
print(result)

#calculate GST
prices = [1000, 2000, 3000, 4000]
prices_with_gst = [price + (price * 18/100) for price in prices]
print(prices_with_gst)
