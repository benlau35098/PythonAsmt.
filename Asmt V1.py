# This is version 1 of my program. It asks the user for their opening balance,
# then asks if they would like to deposit or withdraw from this balance.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
    print("You are too young. Please come again when you are 12.")
    exit()  

balance = float(input("Enter your starting balance: "))

ans = input("This system allows you to withdraw or deposit money.\nWould you like to use the system? (yes/no): ").strip().lower()

if ans == "yes":
    choice = input("Would you like to deposit or withdraw? ").strip().lower()#any capital letters the user uses does not matter

    if choice == "deposit":
        while True:
            dep_amt = float(input("How much would you like to deposit? : "))
            if dep_amt < 0:
                print("You cannot enter a negative number.")
            else:
                balance += dep_amt
                break

    elif choice == "withdraw":
        while True:
            with_amt = float(input("How much would you like to withdraw? : "))
            if with_amt < 0:
                print("You cannot enter a negative number.")
            elif with_amt > balance:
                print("You cannot exceed your balance.")
            else:
                balance -= with_amt
                break

    else:
        print("Invalid choice.")

    print(f"Your new balance is {balance}")

else:
    print("Thank you. Goodbye!")
