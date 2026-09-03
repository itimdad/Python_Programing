
#if conditional statements

age = 17

if age >= 18:
    print("candidate can vote")

#if else statements

if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

#if-elif-else
marks = input("Enter marks: ")

marks = int(marks)
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Failed")


#Nested if

balance = 5000;
withdrawMoney = int(input("Enter amount to witdrawl"))

if balance > 0:
    if withdrawMoney <= balance:
        #debit logic
        balance = balance - withdrawMoney
        print("Successfully withdrawl")
        print("Remaining balance is ", balance)
else:
    print("Funds are not available")

