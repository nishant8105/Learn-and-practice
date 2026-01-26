print("1️⃣ Bank Account Balance")
print("Create a class BankAccount where:")
print("Balance should be private")
print("Provide methods to:")
print("deposit(amount)")
print("withdraw(amount)")
print("get_balance()")

class BankAccount :
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        print(f"The balance in Bank account is {self.__balance}")

    def deposit(self, deposit):
        self.__balance = self.__balance + deposit
        print(f"The balance in Bank account is {self.__balance} after deposite of {deposit}.")
    def withdraw(self, withdraw):
        self.__balance = self.__balance - withdraw
        print(f"The balance in Bank account is {self.__balance} after withdraw of {withdraw}.")

bank = BankAccount(10000)
bank.get_balance()
bank.deposit(1000)
bank.withdraw(9000)
print(" ")
print("===============================================================")
print("2️⃣ Student Marks")
print("Create a class Student where:")
print("Marks are private")
print("Provide methods to:")
print("set_marks(marks)")
print("get_marks()")

class Marks:
    def __init__(self):
        self.__marks = 0
    
    def set_marks(self, marks):
        if (marks > 0) and (marks < 100) :
            self.__marks = marks
        else :
            print("Enter the vaild marks. Marks should be in between  0 to 100")
    
    def get_marks(self):
        print(f"The marks are {self.__marks}")

S1 = Marks()
S1.set_marks(20)
S1.get_marks()


print(" ")
print("===============================================================")
print("3️⃣ Password Protection")
print("Create a class User where:")
print("Password is private")
print("Provide methods to:")
print("set_password(password)")
print("validate_password(input_password)")

class User :
    def __init__(self):
        self.__password = " "
    
    def set_password(self, password):
        self.__password = password
        print("Password set")
    def validate_password(self, input_password):

        if (self.__password == input_password):
            print("Unlock")
            return "Unlock"
        else:
            print("Retry again")
            return "Retry again"
           


user = User()
user.set_password("Nishant")
validate = user.validate_password("Nishant")
while ( validate != "Unlock" ):
    password = input("Enter password: ")
    validate = user.validate_password(password)

print(" ")
print("===============================================================")

