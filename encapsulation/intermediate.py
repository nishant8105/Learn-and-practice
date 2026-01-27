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

print(" ")
print("===============================================================")
print("5️⃣ Employee Salary System")
print("Create a class Employee where:")
print("Salary is private")
print("Methods:")
print("set_salary(salary)")
print("get_salary()")
print("calculate_annual_salary()")

class Employee:
    def __init__(self):
        self.__Salary = 0 
    
    def set_salary(self , Salary):
        if Salary > 0 :
            self.__Salary = Salary
        else :
            print("Salary should be grater than 0")
    
    def get_salary(self):
        print(f"Salary is {self.__Salary}")
    
    def calculate_annual_salary(self):
        self.annual_salary = self.__Salary * 12
        print(f"Anual Salary is {self.annual_salary}")

E1 = Employee()
E1.set_salary(10000)
E1.get_salary()
E1.calculate_annual_salary()

print(" ")
print("===============================================================")
print("6️⃣ Mobile Phone Lock")
print("Create a class Mobile where:")
print("Lock status is private")
print("Methods:")
print("unlock(pin)")
print("lock()")
print("make_call(number)")

class Mobile:
    def __init__(self, pin):
        self.__lock_status = False
        self.__pin = pin
    
    def unlock(self, pin):
        if pin == self.__pin :
            self.__lock_status = True
            print("Mobile Unlock")
        else:
            print("Incorrect pin retry")
            pin = input("Enter pin: ")
            self.unlock(pin)
    def lock (self):
        self.__lock_status = False
        print("Mobile locked")

user = Mobile("nopass")
user.unlock("nopass")
user.lock()