

number = int(input("Enter a number: "))
range_limit = int(input("Enter range: "))

print("\nMultiplication Table of", number)

for i in range(1, range_limit + 1):
    print(number, "x", i, "=", number * i)