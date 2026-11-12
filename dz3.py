class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "done" if self.done else "not done"
        return f"{self.title} - {self.description} (deadline: {self.deadline}) [{status}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        self.tasks.append(Task(title, description, deadline))

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return

    def mark_as_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                return

    def show_tasks(self):
        for task in self.tasks:
            print(task)


manager = TaskManager()
manager.add_task("Homework", "Do python homework", "15.11.2026")
manager.add_task("Shopping", "Buy milk and bread", "12.11.2026")
manager.add_task("Reading", "Read chapter 5", "10.11.2026")

print("All tasks:")
manager.show_tasks()

manager.mark_as_done("Shopping")
print("\nAfter marking Shopping as done:")
manager.show_tasks()

manager.remove_task("Reading")
print("\nAfter removing Reading:")
manager.show_tasks()


# -----------------------------------------------------------

class Product:
    def __init__(self, name, price, in_stock=True):
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def __str__(self):
        return f"{self.name} - {self.price} uah"


class Cart:
    def __init__(self):
        self.products = []

    def add(self, product):
        if product.in_stock:
            self.products.append(product)
        else:
            print(f"{product.name} is not in stock")

    def remove(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                return

    def total(self):
        return sum(p.price for p in self.products)

    def show(self):
        for p in self.products:
            print(p)
        print(f"Total: {self.total()} uah")


cart = Cart()
cart.add(Product("Laptop", 25000))
cart.add(Product("Mouse", 500))
cart.add(Product("Keyboard", 1200))
cart.add(Product("Monitor", 8000, in_stock=False))

print("\nCart:")
cart.show()

cart.remove("Mouse")
print("\nAfter removing Mouse:")
cart.show()


# -----------------------------------------------------------

class BankAccount:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
            return
        self.balance -= amount

    def __str__(self):
        return f"{self.owner} ({self.number}) - balance: {self.balance} uah"


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, owner, number, balance=0):
        acc = BankAccount(owner, number, balance)
        self.accounts.append(acc)
        return acc

    def find(self, number):
        for acc in self.accounts:
            if acc.number == number:
                return acc
        return None

    def transfer(self, from_num, to_num, amount):
        sender = self.find(from_num)
        receiver = self.find(to_num)
        if sender and receiver and sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
        else:
            print("Transfer failed")

    def show_all(self):
        for acc in self.accounts:
            print(acc)


bank = Bank()
bank.create_account("Alex", "001", 10000)
bank.create_account("Maria", "002", 5000)
bank.create_account("Ivan", "003", 0)

print("\nAccounts:")
bank.show_all()

bank.find("003").deposit(3000)
bank.find("001").withdraw(2500)
bank.transfer("001", "002", 4000)

print("\nAfter operations:")
bank.show_all()


# -----------------------------------------------------------

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} - {self.position}, salary: {self.salary} uah"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add(self, name, position, salary):
        self.employees.append(Employee(name, position, salary))

    def remove(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                return

    def total_salary(self):
        return sum(e.salary for e in self.employees)

    def show(self):
        print(f"Department: {self.name}")
        for emp in self.employees:
            print(f"  {emp}")
        print(f"  Total salary: {self.total_salary()} uah")


dev = Department("Development")
dev.add("Alex", "Senior Dev", 45000)
dev.add("Anna", "Junior Dev", 18000)
dev.add("Dmitry", "Middle Dev", 32000)

hr = Department("HR")
hr.add("Natalia", "HR Manager", 28000)
hr.add("Olga", "Recruiter", 22000)

print("\n")
dev.show()
print()
hr.show()

dev.remove("Anna")
print("\nAfter removing Anna:")
dev.show()
