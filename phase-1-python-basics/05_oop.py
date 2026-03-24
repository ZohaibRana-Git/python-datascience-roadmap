# ============================================================
# Phase 1 | Topic 5: OOP — Object Oriented Programming
# ============================================================
# OOP me hum real-world cheezein code me represent karte hain.
# Class = blueprint (design)
# Object = us blueprint se bana actual item
# ============================================================

# ─────────────────────────────────────────
# 1. Basic Class
# ─────────────────────────────────────────
class Student:
    """Ek student ko represent karta hai."""

    # __init__ = constructor — object bante waqt automatically chalta hai
    def __init__(self, name, age, grade):
        self.name  = name    # instance variable
        self.age   = age
        self.grade = grade

    def introduce(self):
        """Student apna introduction deta hai."""
        print(f"Hi! I'm {self.name}, age {self.age}, grade {self.grade}.")

    def is_passing(self):
        """50 se upar grade = pass."""
        return self.grade >= 50

    def __str__(self):
        """print(student) karne par ye string dikhti hai."""
        return f"Student({self.name}, {self.age}, {self.grade})"


# Objects banao
s1 = Student("Ali",   22, 85)
s2 = Student("Sara",  20, 45)
s3 = Student("Ahmed", 23, 72)

print("=== Basic Class ===")
s1.introduce()
s2.introduce()
print(f"\n{s1.name} passing? {s1.is_passing()}")
print(f"{s2.name} passing? {s2.is_passing()}")
print(f"\nprint(s1) → {s1}")

# ─────────────────────────────────────────
# 2. Class Variables vs Instance Variables
# ─────────────────────────────────────────
class BankAccount:
    bank_name = "Python Bank"   # class variable — sab objects share karte hain

    def __init__(self, owner, balance=0):
        self.owner   = owner    # instance variable — har object ka apna
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"  Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("  Insufficient funds!")
        else:
            self.balance -= amount
            print(f"  Withdrew {amount}. Balance: {self.balance}")

    def __str__(self):
        return f"{self.bank_name} | {self.owner} | Balance: {self.balance}"


print("\n=== Bank Account ===")
acc1 = BankAccount("Ali", 1000)
acc2 = BankAccount("Sara", 5000)

acc1.deposit(500)
acc1.withdraw(200)
acc2.withdraw(10000)   # insufficient
print(acc1)
print(acc2)

# ─────────────────────────────────────────
# 3. Inheritance
# ─────────────────────────────────────────
class Animal:
    """Base class (parent)."""

    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says: {self.sound}")

    def info(self):
        print(f"Animal: {self.name}")


class Dog(Animal):
    """Dog inherits from Animal."""

    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # parent __init__ call karo
        self.breed = breed

    def fetch(self):
        print(f"{self.name} fetches the ball!")

    def info(self):
        super().info()   # parent method call
        print(f"Breed : {self.breed}")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def purr(self):
        print(f"{self.name} is purring...")


print("\n=== Inheritance ===")
dog = Dog("Bruno", "Labrador")
cat = Cat("Whiskers")

dog.speak()
dog.fetch()
dog.info()

cat.speak()
cat.purr()

# ─────────────────────────────────────────
# 4. Data Science Example — Dataset class
# ─────────────────────────────────────────
class Dataset:
    """
    Ek simple dataset class — Data Science me
    hum aise classes banate hain data manage karne ke liye.
    """

    def __init__(self, name):
        self.name    = name
        self.records = []

    def add_record(self, record: dict):
        self.records.append(record)

    def count(self):
        return len(self.records)

    def get_column(self, col):
        """Ek column ki saari values list me return karta hai."""
        return [r[col] for r in self.records if col in r]

    def summary(self):
        print(f"\nDataset : {self.name}")
        print(f"Records : {self.count()}")
        if self.records:
            print(f"Columns : {list(self.records[0].keys())}")

    def __repr__(self):
        return f"Dataset(name='{self.name}', records={self.count()})"


print("\n=== Dataset Class ===")
ds = Dataset("Students")
ds.add_record({"name": "Ali",   "score": 85, "city": "Karachi"})
ds.add_record({"name": "Sara",  "score": 92, "city": "Lahore"})
ds.add_record({"name": "Ahmed", "score": 78, "city": "Islamabad"})
ds.add_record({"name": "Zara",  "score": 95, "city": "Karachi"})

ds.summary()

scores = ds.get_column("score")
print(f"\nScores  : {scores}")
print(f"Average : {sum(scores)/len(scores):.1f}")
print(f"Highest : {max(scores)}")
print(f"Lowest  : {min(scores)}")
