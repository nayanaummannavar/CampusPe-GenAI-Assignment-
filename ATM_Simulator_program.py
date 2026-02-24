

balance = 5000   # Initial balance
min_balance = 1000

print("----- Welcome to ATM -----")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    print("Your current balance is:", balance)

elif choice == 2:
    deposit = float(input("Enter amount to deposit: "))
    balance = balance + deposit
    print("Amount deposited successfully.")
    print("Updated balance:", balance)

elif choice == 3:
    withdraw = float(input("Enter amount to withdraw: "))
    if balance - withdraw >= min_balance:
        balance = balance - withdraw
        print("Please collect your cash.")
        print("Remaining balance:", balance)
    else:
        print("Withdrawal not allowed! Minimum balance must be", min_balance)

else:
    print("Invalid choice")