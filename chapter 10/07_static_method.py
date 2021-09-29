from datetime import datetime


class Employee:
    company = "Microsoft"

    # Self is an parameter is passed automatically when we call class.
    def getSalary(self, signature, address):
        print(
            f"Salary of this employee working in {self.company} is Rs.{self.salary}\n{signature}\n{address}")

    @staticmethod   # Using this decorator we do not have to use 'self'
    def greet():
        print("Shalam Shaabji.")

    @staticmethod
    def time():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current time is", current_time)


prasad = Employee()
prasad.salary = 100000

# We can pass more parameters other than self as it passes automatically.
prasad.getSalary("Bye.", "Mumbai")

prasad.greet()  # Using @staticmethod it will parse it as Employee.greet()
prasad.time()
