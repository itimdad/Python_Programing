#match choice

print("1. Add Student")
print("2. View Students")
print("3. Update student ")
print("4. Delete Student")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Adding students")
    case 2:
        print("Viewing students")
    case 3:
        print("Updating student")
    case 4:
        print("Deleting student")
    case _:
        print("Invalid choice")