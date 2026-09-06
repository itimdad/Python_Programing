#Design ATM machine System

balance = 5000



while True:
    print("1 Check balance: ")
    print("2 Deposit")
    print("3 withdrawl money")
    print("4 Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance is : ", balance)
    elif choice == 2:
        balance += float(input("Enter amount you want to deposit:"))
        print("New balance : ", balance)
    elif choice == 3:
        balance -= float(input("Enter amount you want to withdraw:"))
        print("New balance :", balance)
    elif choice == 4:
        break
    else:
        print("Invalid choice")