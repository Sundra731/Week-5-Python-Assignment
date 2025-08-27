#QUESTION 1
# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in %

    def call(self, contact):
        return f"Calling {contact} from {self.model}..."

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"{self.model} charged to {self.battery}%"

    def __str__(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%"


# Subclass (Inheritance and Polymorphism)
class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixels):
        super().__init__(brand, model, storage, battery)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        if self.battery > 5:
            self.battery -= 5
            return f"Photo taken with {self.camera_megapixels}MP camera. Battery now {self.battery}%"
        else:
            return "Battery too low to take photo!"

    # Polymorphism (overriding the call method)
    def call(self, contact):
        return f"Video calling {contact} from {self.model} using front camera..."


phone1 = Smartphone("Samsung", "Galaxy S22", 256, 60)
print(phone1)
print(phone1.call("Alice"))
print(phone1.charge(20))

print("-----")

phone2 = CameraPhone("Apple", "iPhone 14 Pro", 512, 60, 48)
print(phone2)
print(phone2.take_photo())
print(phone2.call("Bob"))  # polymorphism

#QUESTION 2 (Polymorphism)
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Toyota", "Corolla")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     

car1.move()
boat1.move()
plane1.move()
