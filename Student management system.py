students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Check Pass/Fail")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students.append([name, marks])
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent List:")
        for s in students:
            print("Name:", s[0], "| Marks:", s[1])

    elif choice == "3":
        name = input("Enter student name to check result: ")
        for s in students:
            if s[0] == name:
                if s[1] >= 33:
                    print(name, "is PASS")
                else:
                    print(name, "is FAIL")

    elif choice == "4":
        print("Thank you! Program closed.")
        break

    else:
        print("Invalid choice, try again!")