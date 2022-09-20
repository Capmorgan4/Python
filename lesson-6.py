# print('Assignment 1')
# import math
# import time
#
# class Trafficlight:
#     color = ['red', 'yellow', 'green']
#     def running(self):
#         colors = ['red', 'yellow', 'green']
#         for el in colors:
#             if el == 'red':
#                 print('red')
#                 time.sleep(7)
#             elif el == 'yellow':
#                 print('yellow')
#                 time.sleep(2)
#             elif el == 'green':
#                 print('green')
#                 time.sleep(12)
#
#
# traffic_l = Trafficlight()
# print(traffic_l.running())


# print('Assignment 2')
#
#
# class Road:
#
#     def __init__(self, _length, _width):
#         self._length = _length
#         self._width = _width
#         print(f'The road length is {self._length}cm, the road width is {self._width}cm')
#
#     def RoadMass(self, _length, _width, mass_for_m_in_kg, thickness_in_cm):
#         self._length = _length
#         self._width = _width
#         self.mass_for_m_in_kg = mass_for_m_in_kg
#         self.thickness_in_cm = thickness_in_cm
#         mass_of_r = int(_length) * int(_width) * int(mass_for_m_in_kg) * int(thickness_in_cm)
#         print(f'Bitumen mass: {mass_of_r}kg')
#
# E67 = Road(10000000, 4500)
# print(E67.RoadMass(10000000, 4500, 25, 5))



# print('Assignment 3')
#
# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self.wage = float(wage)
#         self.bonus = float(bonus)
#         self._income = {"wage": self.wage, "bonus": self.bonus}
#
#
# class Position (Worker):
#     def get_full_name(self):
#         full_name = self.name + ' ' + self.surname
#         return full_name
#
#     def get_total_income(self):
#         self._income = sum(self._income.values())
#         return f'{self.name} {self.surname} works as a {self.position} and makes totally ${self._income} per month'
#
#
# Cleaner = Position('Ivan', 'Petrov', 'manager', 45000, 300)
#
#
# print(Cleaner.get_full_name())
# print(Cleaner.get_total_income())



# print('Assignment 4')
#
#
# class Car:
#     def __init__(self, speed, name, color, is_police):
#         self.speed = float(speed)
#         self.name = name
#         self.color = color
#         self.is_police = is_police
#         if self.is_police is True:
#             print(f'Car {self.name} of {self.color} color with current speed {self.speed} is a police car')
#         elif self.is_police is False:
#             print(f'Car {self.name} of {self.color} color with current speed {self.speed} is not a police car')
#
#     def go(self):
#         return f'{self.name} goes'
#
#     def stop(self):
#         return f'{self.name} stops'
#
#     def turn(self):
#         direction = input(f'Enter right or left: ').lower()
#         if direction == 'right':
#             return f'The car {self.name} turned right'
#         elif direction == 'left':
#             return f'The car {self.name} turned left'
#
#
#     def show_speed(self):
#         return f'Car speed at the moment is {self.speed}km/h.'
#
#
# class TownCar(Car):
#
#     def show_speed(self):
#         if self.speed > 60.0:
#             return f'You have exceeded the speed limit! Slow Down!'
#         else:
#             return f'Car speed at the moment is {self.speed}km/h. Go on!'
#
#
# class SportCar(Car):
#     pass
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40.0:
#             return f'You have exceed the speed limit! Slow down!'
#         else:
#             return f'Car {self.name} speed at the moment is {self.speed}km/h. Go on!'
#
#
# class PoliceCar(Car):
#     pass
#
#
# MazdaXR = TownCar(45, 'Mazda 678090', 'black', False)
# BMV = SportCar(170, 'BMV BN6789', 'yellow', False)
# Lada = WorkCar(67.9, 'Lada kalina', 'while', False)
# Volvo = PoliceCar(110.4, 'Volvo OO3457', 'blue', True)
#
# print(MazdaXR.go())
# print(MazdaXR.stop())
# print(MazdaXR.turn())
# print(MazdaXR.show_speed())
#
# print(BMV.go())
# print(BMV.stop())
# print(BMV.turn())
# print(BMV.show_speed())
#
# print(Lada.go())
# print(Lada.stop())
# print(Lada.turn())
# print(Lada.show_speed())
#
# print(Volvo.go())
# print(Volvo.stop())
# print(Volvo.turn())
# print(Volvo.show_speed())


# print('Assignment 5')
#
#
# class Stationery:
#     def __init__(self):
#         self.title = input(f'Tool title: ').title()
#
#     def draw(self):
#         return f'{self.title} starts drawing'
#
# class Pen(Stationery):
#     def draw(self):
#         return f'Pen {self.title} starts drawing'
#
# class Pencil(Stationery):
#     def draw(self):
#         return f'Start drawing with the {self.title}'
#
# class Handle(Stationery):
#     def draw(self):
#         return f'Start drawing with the {self.title} on a board'
#
# Bic = Pen()
# Green_pencil = Pencil()
# Black_marker = Handle()
#
# print(Bic.draw())
# print(Green_pencil.draw())
# print(Black_marker.draw())














