
# The SOLID principles can be applied to Python code, just as they can be applied to code written in any other programming language. Here's a brief overview of how each SOLID principle can be implemented in Python:

# Single Responsibility Principle (SRP): In Python, you can ensure that a class has a single responsibility by organizing your code into modules and classes that focus on specific functionalities or concerns. Each class or module should have a well-defined purpose and handle a specific part of the overall functionality.

# Open-Closed Principle (OCP): Python supports the concept of abstraction and polymorphism, which allows you to follow the Open-Closed Principle. You can define abstract base classes using the abc module and use inheritance to create concrete subclasses that extend or override the behavior of the base class. This way, you can add new functionality by creating new subclasses without modifying existing code.

# Liskov Substitution Principle (LSP): In Python, you can adhere to the Liskov Substitution Principle by ensuring that derived classes can be used interchangeably with base classes. This means that the derived classes should honor the contract defined by the base class and not introduce any unexpected behavior or violate any preconditions or postconditions.

# Interface Segregation Principle (ISP): Python supports interfaces through the use of abstract base classes and protocols. By defining specific interfaces that contain only the necessary methods, you can ensure that clients depend only on the interfaces they need. This allows for more fine-grained control over dependencies and promotes decoupling.

# Dependency Inversion Principle (DIP): Python makes it easy to implement the Dependency Inversion Principle through dependency injection and the use of abstractions. By depending on interfaces or abstract classes rather than concrete implementations, you can achieve loose coupling and allow for easier swapping of dependencies.

# Remember that the SOLID principles are not specific to any programming language, including Python. They are general design principles that apply to software development in any language. Python's flexibility and support for object-oriented programming concepts make it well-suited for implementing SOLID principles.

class Order:
    def __init__(self, order_id, customer_name, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount

    def calculate_discount(self):
        # Calculate discount logic
        pass

    def calculate_tax(self):
        # Calculate tax logic
        pass

    def process_payment(self):
        # Process payment logic
        pass

    def save_order(self):
        # Save order to database
        pass


class EmailNotifier:
    def __init__(self, smtp_server):
        self.smtp_server = smtp_server

    def send_order_confirmation(self, order):
        # Send order confirmation email
        pass

    def send_payment_confirmation(self, order):
        # Send payment confirmation email
        pass