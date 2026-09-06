#for loop programe to print number from 1 to 10

for i in range(1,11):
    print("numb", i)
print("======================================")

#Range with end only
for i in range(5):
    print(i)

print("=======================================")
#Range with start stop and increament by
for i in range(1, 10, 2):
    print(i)
print("=======================================")
#List of students print using for loop
students = ["Imdad", "Krishna", "Vijay"]
for student in students:
    print(student)
print("========================================")

#printing each character in a String
name = "Vijay"
for ch in name:
    print(ch)

print("======================================")
#for loop for Tuple ()
courses = ("Java", "Microservices", "Python","DSA")
for course in courses:
    print(course)

print("========================================")

#For loop for SET
cities = {"Hyd", "Delhi", "NCR", "Noida"}
for city in cities:
    print(city)

print("========================================")

#for loop for Dictionary
student = {
    "Id": 1,
    "name": "Imdad",
    "Place": "Gorakhpur"
}

for key in student:
    print(key, "====", student[key])

print("=======================================")
#Total cart prices
cart_prices = [500, 774, 880, 990]
total_price = 0;
for price in cart_prices:
    total_price += price

print("Total cart price is => ",total_price)


