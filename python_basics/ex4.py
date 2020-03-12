cars = 100 #assign number of cars to be 100;
space_in_a_car = 4.0 #assume each car can carry upto 4 persons;
drivers = 30 #there are a total of 30 drivers;
passengers = 90 #total passengers to be carried;
cars_not_driven =cars - drivers #number of extra available cars;
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print('There are', cars, 'cars available.')
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")
