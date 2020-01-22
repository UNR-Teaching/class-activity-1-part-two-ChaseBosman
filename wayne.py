class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
   
    def rev_engine(self):
        print("Vroooooooooom")


class Wheel:
    def __init__(self, size):
        self.size = size

    def turn_wheel(self):
        print("Squeak")

class Vehicle:
    def __init__(self, color, wheel_sz):
        self.color = color
        self.wheels = Wheel(wheel_sz)

class Car(Vehicle):
    def __init__(self, make, model, color, door_count, wheel_sz):
        self.make = make
        self.model = model
        self.door_count = door_count
        self.engine = Engine(102)
        Vehicle.__init__(self, color, wheel_sz)

    def color(self, color):
        self.color = color

    def car_start(self):
        print("Vroom")

    def car_move(self):
        self.wheels.turn_wheel()
        	

class Bicycle(Vehicle):
    def __init__(self, purpose, color, wheel_sz):
        self.purpose = purpose
        Vehicle.__init__(self, color, wheel_sz)

    def pedal(self):
        print("Vroom vroom vroom")


def main():
    wayne = Car("Ford", "Pinto", "black", 4, 22)
    garth = Bicycle("BMX", "red", 16)
    wayne.car_start()
    garth.pedal()
    wayne.car_move()

main()
