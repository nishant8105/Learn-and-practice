print('''8️⃣ Payment System
Create a base class Payment with:
method: pay(amount)
Create child classes:
CreditCardPayment
UPIPayment
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
    
    def upipayment(self, amount, pin):
        if (amount <= self._balance) and (pin == self.__pin):
            self._balance -= amount
            print(f"Payment Done. Remaining balance is {self._balance}")
        else :
            print("Insufficiant balance or Incorrect pin")

Card = CreditCardPayment(50000, 2983)
Card.creditcardPayment(3000, 2983)
upi = UPIPayment(500000, 2389)
upi.upipayment(3000, 2389)
print('''9️⃣ Game Characters
Create a base class Character with:
health, attack_power
method: attack()
Create child classes:
Warrior
Mage
Archer
Override attack behavior.''')

class Character :
    def __init__(self, health, attack_power):
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        print("attacking")
class Warrior(Character):
    def __init__(self, health, attack_power):
        super().__init__( health, attack_power)
    
    def attack (self):
        self.attack_power += (self.attack_power * 0.10)
        print(f"attack power increase by 10 percent") 

class Mage (Character):
    def __init__(self, health, attack_power):
        super().__init__( health, attack_power)
    
    def attack (self):
        self.attack_power += (self.attack_power * 0.15)
        print(f"attack power increase by 15 percent") 


class Archer (Character):
    def __init__(self, health, attack_power):
        super().__init__( health, attack_power)
    
    def attack (self, distance):
        if distance > 100 :
            self.attack_power -= (self.attack_power * 0.15)
            print(f"attack power decrease by 15 percent")
        elif (distance < 100) and (distance > 30): 
            self.attack_power += (self.attack_power * 0.20)
            print(f"attack power increase by 20 percent")
        else :
            print("Switch to Warrior")

barberian = Warrior(1500, 25)
barberian.attack()
print("Warrior attack power", barberian.attack_power)
wizard = Mage(2000, 50)
wizard.attack()
print("Mage attack power", wizard.attack_power)
archer = Archer(1720, 40)
archer.attack(120)
print("Archer attack power", archer.attack_power)
archer.attack(70)
print("Archer attack power", archer.attack_power)
archer.attack(20)
print("Archer attack power", archer.attack_power)

print('''🔟 Transport Booking System
Create a base class Transport with:
method: calculate_fare(distance)
Create ch1ild classes:
Bus
Taxi
Train
Each calculates fare differently.''')
class Transport :
    def __init__(self , distance):
        self.distance = distance
        self.fare = 12.99
        self.total_fare = 0
    
    def calculate_fare(self):
        self.total_fare = self.fare *  self.distance
        print(f"Your fare is {round(self.total_fare, 2)} for {self.distance} at rate of {self.fare}")

class Bus(Transport):
    def __init__(self , distance):
        super().__init__(distance)
        self.fare = 6.99
        self.total_fare = 0

    def calculate_fare(self):
        self.total_fare = self.fare * self.distance
        print("Well Come to bus")
        print(f"Your fare is {round(self.total_fare, 2)} for {self.distance} at rate of {self.fare}")
class Taxi(Transport):
    def __init__(self , distance):
        super().__init__(distance)
        self.fare = 9.99
        self.total_fare = 0

    def calculate_fare(self):
        self.total_fare = self.fare * self.distance
        print("Well Come to Taxi")
        print(f"Your fare is {round(self.total_fare, 2)} for {self.distance} at rate of {self.fare}")
class Train(Transport):
    def __init__(self , distance):
        super().__init__(distance)
        self.fare = 3.99
        self.total_fare = 0

    def calculate_fare(self):
        self.total_fare = self.fare * self.distance
        print("Well Come to Train")
        print(f"Your fare is {round(self.total_fare, 2)} for {self.distance} at rate of {self.fare}")

Tata = Bus(39)
Tata.calculate_fare()
swift = Taxi(38)
swift.calculate_fare()
metro = Train(34)
metro.calculate_fare()