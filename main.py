from ATM import *

print("Hi! This is ATM simulator!\n\n")
user = Account()
print("This is your first usage, so you need to set your PIN of the account:\n")
user.set_pin()
exit(0) if user.authenticate() is not True else True
while True:
    print("\nPick the digit assigned to the wanted action:\n"
          "1 - Show balance\n"
          "2 - Deposit money to the account\n"
          "3 - Withdraw money from the account\n"
          "4 - Change the PIN\n"
          "5 - Exit\n"
          )
    option = int(input())
    if option == 1:
        print(user.show_balance)
    if option == 2:
        amount = int(input("Please, type the amount you want to deposit:\n"))
        user.deposit_money(amount)
    if option == 3:
        amount = int(input("Please, type the amount you want to withdraw:\n"))
        user.withdraw_money(amount)
    if option == 4:
        user.change_pin()
    if option == 5:
        print("Bye!")
        exit(0)
