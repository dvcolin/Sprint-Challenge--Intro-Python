# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# BASE CLASS
class Vehicle:
    def __init__(self):
        pass


# GROUND VEHICLE
class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()


# GROUND VEHICLE SUBCLASSES
class Car(GroundVehicle):
    def __init__(self):
        super().__init__()


class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()


# FLIGHT VEHICLE
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()

# FLIGHT VEHICLE SUBCLASS


class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()


# STARSHIP
class Starship(Vehicle):
    def __init__(self):
        pass
