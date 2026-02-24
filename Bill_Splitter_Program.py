

total_bill = float(input("Enter total bill amount: "))
tax_percent = float(input("Enter tax percentage: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))


tax_amount = (total_bill * tax_percent) / 100

tip_amount = (total_bill * tip_percent) / 100


final_bill = total_bill + tax_amount + tip_amount


per_person = final_bill / people

print("\nTotal Bill after tax and tip:", final_bill)
print("Each person should pay:", per_person)