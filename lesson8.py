# print('Assignment 1')

# class Date:
#     d_m_y = input(f'Date: ')
#     def __init__(self, d_m_y):
#         self.d_m_y = str(d_m_y)
#         print(f'Date: {self.d_m_y}')
#
#     @classmethod
#     def n_date(cls):
#         n_date = str(cls.d_m_y)
#         new_date = []
#         for el in n_date.split('-'):
#             new_date.append(int(el))
#         return new_date
#
#
#     @staticmethod
#     def date_valid(day, month, year):
#
#         if 0 < day <= 31:
#             if 0 < month <= 12:
#                 if 2020 <= year < 2030:
#                     return f'Actual date'
#                 else:
#                     return f'Year out of range'
#             else:
#                 return f'Wrong month'
#         else:
#             return f'Wrong date'
#
# d1 = Date('3-5-2022')
#
# print(d1.n_date())
# print(d1.date_valid(3, 45, 2022))



# print('Assignment 2')
#
# class DivisionByZero (Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# def divizion():
#     num = input('Numerator: ')
#     den = input('Denominator: ')
#     try:
#         num = int(num)
#         den = int(den)
#         if den == 0:
#             raise DivisionByZero('Can not divide by zero. Enter another denominator.')
#     except DivisionByZero as err:
#         print(err)
#     else:
#         return num / den
#
# print(divizion())


# print('Assignment 3')
#
# class Numb (Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# my_list = []
# while True:
#     n = input('Enter numbers: ')
#     if n == 'stop':
#         break
#     try:
#         if not n.isdigit():
#             raise Numb(f'Not a number! Enter again!')
#     except Numb as err:
#         print(err)
#     else:
#         my_list.append(int(n))
# print(my_list)


# print('Assignment 4, 5, 6')
#
# class Warehouse:
#     def __init__(self, *equipment):
#         self.equipment = list(equipment)
#
#     def receive_equip_date(self, date):
#         self.date = date
#         return f'Equipment {self.equipment} arrived at the warehouse {self.date}'
#
#     def sort_equip (self, *departments):
#         self.departments = list(departments)
#         equip_list = {}
#         send_to_dep = {}
#         for tool in self.equipment:
#             if tool == 'printer':
#                 equip_list[tool] = input('Amount of printers: ')
#             elif tool == 'scaner':
#                 equip_list[tool] = input('Amount of scaners: ')
#             elif tool == 'xerox':
#                 equip_list[tool] = input('Amount of xerox: ')
#         print(equip_list)
#
#         for dep in self.departments:
#             if dep == 'sales department':
#                 send_to_dep[dep] = 'printer'
#             elif dep == 'management department':
#                 send_to_dep[dep] = 'scaner'
#             elif dep == 'head office':
#                 send_to_dep[dep] = 'xerox'
#         print(send_to_dep)
#
#
# class Equipment:
#     def __init__(self):
#         try:
#             self.tool = input('Enter tool: ')
#             self.mark = input('Enter mark: ')
#             self.year = int(input('Enter year: '))
#             print(f'Item {self.tool} {self.mark} of the {self.year} year of production is present in the warehouse.')
#         except ValueError:
#             self.year = int(input('Error! Enter year as a number: '))
#         finally:
#             print(f'Item {self.tool} {self.mark} of the {self.year} year of production is present in the warehouse.')
#
#
# class Printer (Equipment):
#     def __init__(self):
#         super().__init__()
#         self.color_printer = 'color'
#
#     def util(self):
#         if self.color_printer is False:
#             return f'Send this printer for utilization'
#         elif self.year < 2010:
#             return f'Send this printer for utilization'
#         else:
#             return f'The printer {self.mark} is fine'
#
# class Scaner (Equipment):
#     def __init__(self):
#         super().__init__()
#         self.scner_type = input('Scaner type (drum, microfim, slide): ')
#
#
#     def util(self):
#         if self.scner_type == 'microfilm':
#             return f'The scaner {self.mark} is fine'
#         else:
#             return f'Send this scaner {self.mark} for utilization'
#
# class Xerox (Equipment):
#     def __init__(self):
#         super().__init__()
#         self.buildin_scaner = input('Supplied with build-in scaner (Yes/No): ').capitalize()
#
#     def xerox_valid(self):
#         if self.buildin_scaner == 'Yes' and self.year > 2020:
#             return f'Xerox {self.mark} is acceptable for the head office'
#         else:
#             return f'Utilize or use in different department'
#
# stor = Warehouse('printer', 'scaner', 'xerox')
# print(stor.receive_equip_date('20.07.2022'))
# stor.sort_equip('sales department', 'management department', 'head office')
#
# p1 = Printer()
# print(p1.util())
# p2 = Printer()
# print(p2.util())
#
# s1 = Scaner()
# print(s1.util())
#
# x1 = Xerox()
# print(x1.xerox_valid())



# print('Assignment 7')
#
# class ComplNum:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         c = complex(self.a, self.b)
#         print(c)
#
#     def __add__(self, other):
#         compl_sum = complex(self.a, self.b) + complex(other.a, other.b)
#         return compl_sum
#
#     def __mul__(self, other):
#         compl_mul = complex(self.a, self.b) * complex(other.a, other.b)
#         return compl_mul
#
#
# n1 = ComplNum(2, 7)
# n2 = ComplNum(3, 4)
# print(f'n1 + n2 = {n1 + n2}')
# print(f'n1 * n2 = {n1 * n2}')
