from car import Car
import random

small_car = Car("white", "BMW", 250, 0, 0)
big_car = Car("brown", "Range Rover", 250, 0, 0)

# start the race
for x in range(3):
    big_car.start()
    small_car.start()
    # accelerate cars
    big_car.accelerate(x * random.randint(5, 20))
    small_car.accelerate(x * random.randint(5, 20))

for x in range(3):
    # brake cars
    big_car.brake(x * random.randint(5, 20))
    small_car.brake(x * random.randint(5, 20))

print(f"{big_car.brand} speed: ", big_car.get_current_speed())
print(f"{small_car.brand} speed: ", small_car.get_current_speed())
# find the winner
speed_small_car = small_car.get_current_speed()
speed_big_car = big_car.get_current_speed()

if speed_small_car == 0 and speed_big_car > 0:
    # big car wins
    print(f"{small_car.brand} has lost the race")
    print(f"{big_car.brand} has won the race")
elif speed_big_car == 0 and speed_small_car > 0:
    # small car wins
    print(f"{big_car.brand} has lost the race")
    print(f"{small_car.brand} has won the race")
elif speed_big_car == 0 and speed_small_car == 0:
    # it is a tie
    print(f"Both {big_car.brand} and {small_car.brand} have tied in the race")
else:
    print("No winner is found")
