from multipledispatch import dispatch

# METHOD OVERRIDING 

class Device:
    def __init__(self, user, location):
        self.user = user
        self.location = location

    def delivery_info(self):
        print(f"User: {self.user}")
        print(f"Delivery Location: {self.location}")
        print("Using Smart Delivery Service")

class Drone(Device):
    def delivery_info(self):
        print("_____Smart Delivery via DRONE_____")
        print(f"User: {self.user}")
        print(f"Delivery Location: {self.location}")
        print("Your package will arrive by drone.")
        print("__________________________________")

class Robot(Device):
    def delivery_info(self):
        print("_____Smart Delivery via ROBOT_____")
        print(f"User: {self.user}")
        print(f"Delivery Location: {self.location}")
        print("Your package will arrive by ground robot.")
        print("___________________________________")

# Instantiate and call
order1 = Drone("Alice", "Downtown")
order1.delivery_info()

order2 = Robot("Bob", "Uptown")
order2.delivery_info()

# METHOD OVERLOADING EXAMPLE

print("______USER REGISTRATION SYSTEM_______")

@dispatch(str, str, int)
def register_user(name, email, age):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print("User registered via email.")

@dispatch(str, str)
def register_user(name, phone_number):
    print(f"Name: {name}")
    print(f"Phone Number: {phone_number}")
    print("User registered via mobile.")

# Calls
register_user("Clara", "clara@example.com", 22)
register_user("David", "0700123456")

# METHOD RESOLUTION ORDER (MRO)

class Bird:
    def fly(self):
        print("Bird can fly.")

class Plane:
    def fly(self):
        print("Plane can fly faster.")

class Jet(Plane, Bird):
    pass

jet1 = Jet()
jet1.fly() 

