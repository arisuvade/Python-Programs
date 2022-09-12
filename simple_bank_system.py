import sys

print("Welcome")
print("-------------------------------")

error1 = """
Error: Use numbers only, not word.
Restart the program.
"""
error2 = """
Error: Use (y) for yes and (n) for no.
Restart the program.
"""
error3 = """
Error: The amount you want to transfer is larger than your balance.
Restart the program.
"""
error4 = """
Error: Use (U) for utilities and (L) for loans.
Restart the program.
"""

depositor = input("Are you a new depositor? (y/n) ").lower()

if depositor == "y":
    print("Fill up the form.")
    account_name = input("Account Name: ")
    try:
        pin_number = int(input("Pin Number: "))
        initial_amount = float(input("Initial Deposit Amount: "))
    except ValueError:
        print(error1)
        sys.exit
    print("-------------------------------")
    print("Sign up successful.")

elif depositor == "n":
    initial_amount = 10_000
    print("Fill up the form.")
    try:
        account_number = int(input("Account Number: "))
        pin_number = int(input("Pin Number: "))
    except ValueError:
        print(error1)
        sys.exit
    print("-------------------------------")
    print("Log in successful")
else:
    print(error2)
    sys.exit

print("-------------------------------")

if depositor == "y":
    print(f"Account Name: {account_name}")
else:
    print(f"Account Number: {account_number}")

print("-------------------------------")

print("""What do you want to do?
Use only the first letter for transactions
-------------------------------
Widthraw(W)
Pay bills(P)
Transfer fund(T)
Deposit(D)
Change pin(C)
-------------------------------""")

action = input("Transaction: ").lower()

if depositor == "y" or "n":

    if action == "w":
        print("Withdrawal Transaction")
        try:
            amount_to_withdraw = float(input("Amount: "))
        except ValueError:
            print(error1)
        sys.exit
        print("Transaction successful")
        new_balance = initial_amount - amount_to_withdraw
        print(f"New balance: {new_balance}")

    elif action == "p":
        print("Pay Bills")
        pay_bills_for = input("Utilities(U) or Loans(L)? ").lower()
        if pay_bills_for == "u":
            company_name = input("Company Name: ")
            try:
                amount_to_pay = float(input("Amount: "))
            except ValueError:
                print(error1)
            sys.exit
            if initial_amount > amount_to_pay:
                print("Transaction successful")
                new_balance = initial_amount - amount_to_pay
                print(f"New balance: {new_balance}")
            else:
                print(error3)
        elif pay_bills_for == "l":
            company_name = input("Company Name: ")
            try:
                amount_to_pay = float(input("Amount: "))
            except ValueError:
                print(error1)
            sys.exit
            if initial_amount > amount_to_pay:
                print("Transaction successful")
                new_balance = initial_amount - amount_to_pay
                print(f"New balance: {new_balance}")
            else:
                print(error3)
        else:
            print(error4)

    elif action == "t":
        print("Transfer Fund")
        try:
            amount_to_transfer = float(input("Amount: "))
            account_number = int(input("To Account Number: "))
        except ValueError:
            print(error1)
        if initial_amount > amount_to_transfer:
            print("Transaction successful")
            new_balance = initial_amount - amount_to_transfer
            print(f"New balance: {new_balance}")
        else:
            print(error3)

    elif action == "d":
        print("Deposit")
        try:
            deposit_amount = float(input("Deposit: "))
        except ValueError:
            print(error1)
        print("Transaction successful")
        new_balance = initial_amount + deposit_amount
        print(f"New balance: {new_balance}")

    elif action == "c":
        changed_pin = True
        try:
            new_pin_number = int(input("New Pin: "))
        except ValueError:
            print(error1)
        print("The pin is changed")
        print(f"Old pin {pin_number} change to {new_pin_number}")
        print(f"New Pin: {new_pin_number}")
