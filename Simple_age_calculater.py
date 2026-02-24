
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))

age = current_year - birth_year

print("Age in years:", age)
print("Age in months:", age * 12)
print("Age in days:", age * 365)
print("Age in hours:", age * 365 * 24)
print("Age in minutes:", age * 365 * 24 * 60)
print("Years left to 100:", 100 - age)