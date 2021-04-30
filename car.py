class Car:
    def __init__(self, color, brand, top_speed, current_speed, min_speed):
        self.color = color
        self.brand = brand
        self.topSpeed = top_speed
        self.currentSpeed = current_speed
        self.min_speed = min_speed

    def get_min_speed(self):
        return self.min_speed

    def set_min_speed(self, min_speed):
        self.min_speed = min_speed

    def get_current_speed(self):
        return self.currentSpeed

    def get_top_speed(self):
        return self.topSpeed

    def set_current_speed(self, current_speed):
        self.currentSpeed += current_speed

    def set_top_speed(self, top_speed):
        self.topSpeed = top_speed

    def start(self):
        # starts the car
        # set min speed
        self.set_min_speed(self.get_min_speed())
        self.set_top_speed(self.get_top_speed())
        self.set_current_speed(0)

    def brake(self, amount):
        # decrement the car's speed by the amount
        if (self.currentSpeed - amount) < self.min_speed:
            self.currentSpeed = self.min_speed
        else:
            self.set_current_speed(-amount)

    def accelerate(self, amount):
        # increment the car's speed by the amount
        if (self.currentSpeed + amount) > self.topSpeed:
            self.currentSpeed = self.topSpeed
        else:
            self.set_current_speed(amount)

    def stop(self):
        speed = self.get_current_speed()
        self.brake(speed)

#
# myCar = Car("white", "BMW", 250, 0, 0)
#
# myCar.start()
# print(myCar.get_current_speed())
# myCar.accelerate(10)
# print(myCar.get_current_speed())
# myCar.accelerate(20)
# print(myCar.get_current_speed())
# myCar.brake(5)
# print(myCar.get_current_speed())
# myCar.stop()
# print(myCar.get_current_speed())
