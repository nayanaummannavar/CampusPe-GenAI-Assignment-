
num = int(input("Enter a number: "))

factorial = 1

print("\nStep-by-step calculation:")

for i in range(1, num + 1):
    factorial = factorial * i
    print("After multiplying by", i, "->", factorial)

print("\nFinal Factorial of", num, "is:", factorial)