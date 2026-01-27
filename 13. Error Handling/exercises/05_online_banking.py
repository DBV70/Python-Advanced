class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

pin_code, balance, age = input().split(', ')
balance = int(balance)
age = int(age)

while True:
    line = input()
    if line == "End":
        break

    if "Send Money" in line:
        command, money, pin = line.split('#')
        money = int(money)
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")
        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    if "Receive Money" in line:
        command, money = line.split('#')
        money = int(money)
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        balance += money
        print(f"{money:.2f} money went straight into the bank account")

