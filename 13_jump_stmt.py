#Jumping stmt => It is used to control flow of loop execution

#break statement
count = 1

while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1

print("==================================")
for i in range(1, 11):
    if i == 6:
        break
    print(i)

print("====================================")
students = ["AJay","Karan", "Vijay"]

for student in students:
    print("checking student: ", student)
    if student == "Karan":
        print("Student found name is: ", student)
        break

#continue statement

for i in range(1, 11):
    if i == 5:
        continue

    print(i)


