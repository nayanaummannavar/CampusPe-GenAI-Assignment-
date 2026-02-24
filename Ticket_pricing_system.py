

age = int(input("Enter your age: "))
tickets = int(input("Enter number of tickets: "))
day = input("Is it Wednesday? (yes/no): ")

# Base price based on age
if age < 12:
    price = 100
elif age <= 60:
    price = 150
else:
    price = 120

# Apply Wednesday discount
if day.lower() == "yes":
    price = price - 20

total_amount = price * tickets

print("Price per ticket:", price)
print("Total amount to pay:", total_amount)