year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a Leap Year because it is divisible by 400.")

elif year % 100 == 0:
    print(year, "is NOT a Leap Year because it is divisible by 100 but not by 400.")

elif year % 4 == 0:
    print(year, "is a Leap Year because it is divisible by 4.")

else:
    print(year, "is NOT a Leap Year because it is not divisible by 4.")