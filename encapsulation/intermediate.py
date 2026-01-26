print("4️⃣ ATM Machine")
print("Create a class ATM where:")
print("PIN is private")
print("Balance is private")
print("Methods:")
print("check_balance(pin)")
print("withdraw(pin, amount)")

class ATM :
    def __init__(self, pin, Balance):
        self.__PIN = pin
        self.__Balance = Balance
    
    def check_balance(self, pin):
        if (self.__PIN == pin ):
            print(self.__Balance)
        else :
            pin = int(input("Incorrect password Enter again: "))
            self.check_balance(pin)

    def Withdraw(self, pin, amount):
        if (self.__PIN == pin ):
            if (self.__Balance > amount):
                self.__Balance -= amount
                print(f"{amount} is withdraw")
            else :
                print("insufficant balance")
        else :
            pin = int(input("Incorrect password Enter again: "))
            self.Withdraw(pin, amount)

holder = ATM("nopass", 10000)
holder.check_balance("nopass")
holder.Withdraw("nopass", 5000)