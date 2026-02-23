class PINCodeError(Exception):
    pass
class UnderageTransactionError(Exception):
    pass
class MoneyIsNegativeError(Exception):
    pass
class MoneyNotEnoughError(Exception):
    pass


pin, start_balance, age = input().split(", ")
start_balance = float(start_balance)
age = int(age)


while True:
    command = input()
    if command == "End":
        break

    if command.startswith("Send Money#"):
        _, money_str, pin_code = command.split("#")
        money = float(money_str)
        if pin_code != pin:
            raise PINCodeError("Invalid PIN code")
        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        if money > start_balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        start_balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {start_balance:.2f} money left in the bank account")
    elif command.startswith("Receive Money#"):
        _, money_str = command.split("#")
        money = float(money_str)

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        money_income = money / 2
        start_balance += money_income
        print(f"{money_income:.2f} money went straight into the bank account")

# 9999, 3000, 18
# Send Money#1500#9999
# Receive Money#2000
# End

# 5545, 20000, 40
# Send Money#15000#5455
# End

# 2289, 1000, 17
# Send Money#100#2289
# End

# 1234, 10000, 21
# Send Money#10001#1234
# End

# 1111, 7000, 50
# Receive Money#-500#1111
# End
