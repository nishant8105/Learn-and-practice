print('''5️⃣ Bank Account Types
Create a base class Account with:
attributes: account_number, balance
methods: deposit(), withdraw()
Create child classes:
SavingsAccount (interest)
CurrentAccount (overdraft)
Override withdraw() logic.''')

class Account:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    
    def deposit(self, account_number, amount):
        if (self._account_number == account_number) :
            self._balance += amount
            print(f"{amount} is deposite")
            print(f"Balance is {self._balance}")
        else :
            print("Enter correct account nnumber")
    
    def withdraw(self, account_number, amount):
        if (self._account_number == account_number) :
            if (self._balance >= amount):
                self._balance -= amount
                print(f"{amount} is withdraw")
                print(f"Remaining balance is {self._balance}")
            else:
                print(f"Insfficiant balance : {self._balance}")
        else :
            print("Enter correct account nnumber")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest ):
        super().__init__(account_number, balance)
        self._interest = interest
    def AddInterset(self):
        self._balance += (self._balance * (self._interest / 100))
        print("Interest amount is added to your account")
        print(f"Your account balance is {self._balance}")

class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft):
        super().__init__(account_number, balance)
        self.overdraft = overdraft
    
    def withdraw(self, account_number, amount):
        if (self._account_number == account_number) :
            if (amount <= self._balance + self.overdraft):
                print(f"{amount} is withdraw")
            else:
                print(f"Exceed overdraft limit")
        else :
            print("Enter correct account nnumber")

# Savings Account Test
savings = SavingsAccount(101, 5000, 5)
savings.deposit(101,1000)
savings.AddInterset()
savings.withdraw(101,3000)

print()

# Current Account Test
current = CurrentAccount(201, 3000, 2000)
current.withdraw(201, 4500)
current.withdraw(201, 6000)

print('''6️⃣ Online Shopping Discount
Create a base class Product with:
attributes: name, price
method: get_price()
Create child classes:
Electronics
Clothing
Each child applies different discounts.''')
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_price(self):
        print(self._price," of ", self._name)

class Electronics(Product):
    def __init__(self):
        self.product = {
            "Fan" : 5700,
            "Mobile" : 12500,
            "ipad" : 25000,
            "laptop" : 56000
        }
    def get_product(self, name):
        for key, value in self.product.items() :
            if key == name :
                self.name = key
                self.price = value
                super().__init__(self.name, self.price)
                break
    def get_discount(self, discount):
        self.price -= (self.price *(discount/100))
        super().__init__(self.name, self.price)
class Clothing(Product):
    def __init__(self):
        self.product = {
            "t-shirts" : 1299,
            "shirts" : 999,
            "jeans" : 1399,
            "jacket" : 1500
        }
    def get_product(self, name):
        for key, value in self.product.items() :
            if key == name :
                self.name = key
                self.price = value
                super().__init__(self.name, self.price)
                break
    def get_discount(self, discount):
        self.price -= (self.price *(discount/100))
        super().__init__(self.name, self.price)

e1 = Electronics()
e1.get_product("laptop")
e1.get_discount(10)
e1.get_price()
t1 = Clothing()
t1.get_product("shirts")
t1.get_discount(9)
t1.get_price()

print('''7️⃣ School System
Create a base class Person with:
name, age
Create child classes:
Student (roll_no, marks)
Teacher (subject, salary)
Add a method get_info() for each.''')

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self,name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks
    
    def get_info(self):
        print(f'''
Nmae : {self.name}
Age :{self.age} year
Roll No. : {self.roll_no}
Marks : {self.marks}''')


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    
    def get_info(self):
        print(f'''
Nmae : {self.name}
Age :{self.age} year
Subject : {self.subject}
Salary : {self.salary}''')

s1 = Student("Nishant", 21, 41, 88)
s1.get_info()
T1 = Teacher("Gopal Ade sir", 32 , "OOPs", 25000)
T1.get_info()
