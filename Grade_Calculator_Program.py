# Grade Calculator Program

print("Enter marks for 5 subjects:")

sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5


if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"
if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\nTotal Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)