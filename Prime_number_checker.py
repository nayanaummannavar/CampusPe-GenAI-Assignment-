

num = int(input("Enter a number to check prime: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")



start = int(input("\nEnter start of range: "))
end = int(input("Enter end of range: "))

print("Prime numbers between", start, "and", end, "are:")

for number in range(start, end + 1):
    if number > 1:
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            print(number, end=" ")