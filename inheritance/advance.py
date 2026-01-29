print('''8️⃣ Payment System
Create a base class Payment with:
method: pay(amount)
Create child classes:
CreditCardPayment
UPIPayment
CashPayment
Each implements payment differently.''')
class Payment:
    def __init__(self, balance):
        self._balance = balance
    
    def payment(self, amount):
        if amount <= self._balance :
            self._balance -= amount
            print(f"Payment Done. Remaining balance is {self._balance}")
        else :
            print("Insufficiant balance")

class CreditCardPayment(Payment):
    def __init__(self, limit, pin):
        # super().__init__(balance)
        self.Card_limit  = limit
        self.__pin = pin

    def creditcardPayment(self, amount, pin):
        if (amount <= self.Card_limit ) and (pin == self.__pin):
            self.Card_limit -= amount
            print(f"Payment Done. Remaining card limit is {self.Card_limit}")
        else :
            print("Limit over or Incorrect pin")


class UPIPayment(Payment):
    def __init__(self, balance, pin):
        super().__init__(balance)
        self.__pin = pin
    
    def creditcardPayment(self, amount, pin):
        if (amount <= self._balance) and (pin == self.__pin):
            self._balance -= amount
            print(f"Payment Done. Remaining balance is {self._balance}")
        else :
            print("Insufficiant balance or Incorrect pin")

    