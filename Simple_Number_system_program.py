

while True:
    print("\n1.Factorial  2.Prime  3.Fibonacci  4.Sum of Digits")
    print("5.Reverse  6.Armstrong  7.GCD  8.LCM  9.Perfect  0.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        n = int(input("Enter number: "))
        f = 1
        for i in range(1, n+1):
            f *= i
        print("Factorial:", f)

    elif ch == 2:
        n = int(input("Enter number: "))
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        print("Prime" if prime and n > 1 else "Not Prime")

    elif ch == 3:
        n = int(input("Enter terms: "))
        a, b = 0, 1
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()

    elif ch == 4:
        n = input("Enter number: ")
        print("Sum:", sum(int(d) for d in n))

    elif ch == 5:
        n = input("Enter number: ")
        print("Reverse:", n[::-1])

    elif ch == 6:
        n = input("Enter number: ")
        p = len(n)
        print("Armstrong" if sum(int(d)**p for d in n) == int(n) else "Not Armstrong")

    elif ch == 7:
        a = int(input("First: "))
        b = int(input("Second: "))
        while b:
            a, b = b, a % b
        print("GCD:", a)

    elif ch == 8:
        a = int(input("First: "))
        b = int(input("Second: "))
        x, y = a, b
        while y:
            x, y = y, x % y
        print("LCM:", (a*b)//x)

    elif ch == 9:
        n = int(input("Enter number: "))
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        print("Perfect" if s == n else "Not Perfect")

    elif ch == 0:
        break

    else:
        print("Invalid choice")