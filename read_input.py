#Taking input from user

name = input("Enter your name")
print("Welcome", name)

age = input("Enter your age")
print("Your age :", age)

#Taking 2 input
a, b = input("Engter value of a and b").split(" ")
print("First number is ", a)
print("Second number is ", b)

print("Type of a :", type(a), "Type of b:",type(b))

print("sum before type casting  => ", a + b)   #concatenation is happening

a = int(a)
b = int(b)
print("Sum after Type casting: ", a + b)    #addition is happening

#list type casting
course_name = "Java"
letters = list(course_name)
print(letters)