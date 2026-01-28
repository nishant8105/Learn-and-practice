print('''7️⃣ Online Shopping Wallet
Create a class Wallet where:
Balance is private
Methods:
add_money(amount)
pay(amount)
get_balance()''')

class Wallet:
    def __init__(self, balance):
        self.__balance = balance
    
    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} is added to wallet")
        else :
            print("Invalid amount. Please enter positive value.")

    def pay(self, amount):
        if amount <= 0 :
            print("Invalid payment amount")
        elif amount <= self.__balance :
            self.__balance -= amount
            print(f"{amount} paid successfully")
        else :
            print(f"Insufficant balance in wallet.")
    
    def get_balance(self):
        return self.__balance

user = Wallet(1000)
user.pay(10000)
user.add_money(9000)
user.pay(10000)
user.get_balance()
print("Current Balance: ", user.get_balance())

print("8️⃣ Online Exam System Create a class Exam where: Answers are private Methods: submit_answer(question_no, answer) calculate_score()")
class Exam:
    def __init__(self):
        self.__answers = {
            1: "a",
            2: "c",
            3: "d",
            4: "b"
        }
        self.__student_answers = {}
        self.__score = 0

    def submit_answer(self, question_no, answer):
        self.__student_answers[question_no] = answer

    def calculate_score(self):
        self.__score = 0
        for q_no, correct_answer in self.__answers.items():
            if self.__student_answers.get(q_no) == correct_answer:
                self.__score += 1
        return self.__score


# Example usage
student1 = Exam()

student1.submit_answer(1, "a")
student1.submit_answer(2, "b")
student1.submit_answer(3, "d")
student1.submit_answer(4, "b")

print("Final Score:", student1.calculate_score())


print('''9️⃣ Hospital Patient Record
Create a class Patient where:
Medical history is private
Methods:
add_record(record)
view_record(doctor_id)''')

class Patient:
    
    def __init__(self, name, doctor_id):
        self.name = name
        self.__medical_history = [] 
        self.__authorized_doctor = doctor_id  

    def add_record(self, record):
        self.__medical_history.append(record)
        print("Record added successfully.")

    def view_record(self, doctor_id):
        if doctor_id == self.__authorized_doctor:
            return self.__medical_history
        else:
            return "Access Denied! Unauthorized doctor."


patient1 = Patient("vikram", 101)

patient1.add_record("Fever - Prescribed Paracetamol")
patient1.add_record("Blood Test - Normal")

print(patient1.view_record(101))
print(patient1.view_record(202))
