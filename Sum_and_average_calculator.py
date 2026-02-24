count = int(input("How many numbers do you want to enter? "))

numbers = []

for i in range(count):
    num = float(input("Enter number: "))
    numbers.append(num)

total = sum(numbers)
average = total / count
maximum = max(numbers)
minimum = min(numbers)

print("\nSum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)