
print("Number Pattern Printer")
print("1. Increasing Pattern")
print("2. Same Number Pattern")
print("3. Reverse Pattern")

choice = int(input("Enter your choice (1-3): "))
height = int(input("Enter height of pattern: "))

if choice == 1:
    # Increasing Pattern
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif choice == 2:
    # Same Number Pattern
    for i in range(1, height + 1):
        for j in range(i):
            print(i, end=" ")
        print()

elif choice == 3:
    # Reverse Pattern
    for i in range(height, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

else:
    print("Invalid choice")