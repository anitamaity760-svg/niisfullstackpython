class Car:
    
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0
    
    def start(self):
        print(self.brand, "car started.")
    
    def accelerate(self):
        self.speed += 20
        print("Speed is", self.speed)
    
    def stop(self):
        self.speed = 0
        print("Car stopped.")


# Creating Objects
c1 = Car("BMW", "Red")
c2 = Car("Audi", "Blue")

c1.start()
c1.accelerate()
c1.stop()