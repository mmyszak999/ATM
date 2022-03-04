def check_pin(_pin):
    if (pin_same_numbers(_pin)
            and pin_length(_pin)
            and pin_consecutive_numbers(_pin)
            and pin_if_none(_pin)
            and pin_with_zeros(_pin)
            and pin_same_numbers(_pin)):
        return True
    return False


def pin_if_none(_pin):
    return False if _pin == "None" else True


def pin_consecutive_numbers(_pin):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(10):
        results = [digits[i - 3], digits[i - 2], digits[i - 1], digits[i]]
        if _pin == "".join(results):
            return False
    return True


def pin_length(_pin):
    return False if len(_pin) != 4 else True


def pin_same_numbers(_pin):
    for i in range(10):
        result = str("".join(4 * str(i)))
        if str(_pin) == str(result):
            return False
    return True


def pin_with_zeros(_pin):
    for i in range(1, 5):
        zeros = str("0" * i)
        if _pin.startswith(zeros):
            return False
    return True


class Account:
    def __init__(self, balance=500, _pin=None, max_debit=-150):
        self.balance = balance
        self._pin = str(_pin)
        self.max_debit = max_debit

    def set_pin(self):
        chances = 3
        while chances != 0:
            print("Before you set the PIN, remember that the PIN:\n"
                  "1) Must have 4 digits\n"
                  "2) Can't consists of 4 consecutive numbers (for example: 1234, 4567, 8901 etc.)\n"
                  "3) Can't be empty\n"
                  "4) Can't start with 1 or more zeros\n"
                  "5) Can't contain the same 4 digits (for example 4444, 0000, 2222)\n"
                  )
            typed_pin = str(input("Type PIN:\n"))
            typed_pin_again = str(input("Type the number again:\n"))
            if (typed_pin == typed_pin_again != self._pin
                    and (check_pin(typed_pin) and check_pin(typed_pin_again)) is True):
                self._pin = str(typed_pin)
                return "PIN has been set successfully!\n"
            else:
                chances -= 1
                print("\nPIN can't be set! Please follow the rules of setting the PIN.\n")
                print(f"{chances} attempts left.\n")
        return exit(0)

    @property
    def show_balance(self):
        if self.balance == self.max_debit:
            print("You can't withdraw any money!\n")
        return f"Your balance is {self.balance}"

    def allow_operation(self, amount):
        return False if self.balance - amount < self.max_debit else True

    def authenticate(self):
        print("\nPlease, confirm the account ownership in order to perform operations!\n ")
        typed_pin = str(input("Introduce your PIN number : \n"))
        return True if typed_pin == self._pin else False

    def deposit_money(self, amount):
        if not self.authenticate():
            return "Wrong PIN number! You can't deposit the money!"
        else:
            self.balance += amount
            print(f"Your balance has been increased by {amount} !")
            return self.show_balance

    def withdraw_money(self, amount):
        if not self.authenticate():
            return "Wrong PIN number! You can't deposit the money!"
        else:
            if not self.allow_operation(amount):
                print("You don't got enough money to withdraw that amount\n")
                withdraw_to_debit = str(input("Do you want to withdraw the biggest available amount?\n "
                                              "Choose 'Yes' or 'No': "))
                if withdraw_to_debit == 'Yes':
                    rest = self.balance - amount - self.max_debit
                    amount += rest
                    self.balance -= amount
                    print(f"Your balance has been decreased by {amount} !\n")
                    return self.show_balance
                else:
                    print("No money has been withdrawn!\n")
                    return self.show_balance
            else:
                self.balance -= amount
                print(f"Your balance has been decreased by {amount} !\n")
                return self.show_balance

    def change_pin(self):
        if self.authenticate():
            return self.set_pin()
        else:
            return "Sorry! You can't change your PIN. Try later!"
