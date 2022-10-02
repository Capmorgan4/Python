# print('Assignment 1')
# class Matrix:
#     def __init__(self, my_m):
#         self.my_m = my_m
#
#
#     def __str__(self):
#         res = ''
#         for i in range(len(self.my_m)):
#             new = '\t'.join(map(str, self.my_m[i]))
#             res = '\n'.join([res, new])
#         return res
#
#     def __add__(self, other):
#         new_m = []
#         for i in range(len(self.my_m)):
#             new_m.append([])
#             for j in range(len(self.my_m[0])):
#                 new_m[i].append(self.my_m[i][j] + other.my_m[i][j])
#         return Matrix(new_m)
#
# my_matr1 = Matrix([[1, 4, 6], [4, 6, 7]])
# my_matr2 = Matrix([[5, 8, 3], [1, 7, 9]])
#
# print(my_matr1)
# print(my_matr2)
# print(my_matr1 + my_matr2)

#

# print('Assignment 2')

# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#
#     @abstractmethod
#     def consumption(self, p):
#         pass
#
# class Costume(Clothes):
#     def __init__(self, height):
#         self.height = height
#
#     @property
#     def h(self):
#         return self.height
#
#     @h.setter
#     def h(self, height):
#         self.height = height
#
#     def consumption(self, height):
#         if height > 2.5:
#             return f'Unrealistic parameter'
#         elif height < 1.5:
#             return f'Only adult customer allowed'
#         else:
#             consump = 2 * self.height + 0.3
#         return consump
#
# class Coat(Clothes):
#
#     def __init__(self, size):
#         self.size = size
#
#     @property
#     def s(self):
#         return self.size
#
#     @s.setter
#     def s(self, size):
#         self.size = size
#
#     def consumption(self, size):
#         if size > 56:
#             return f'Out of size range'
#         elif size < 30:
#             return f'Only adult customer allowed'
#         else:
#             consump = self.size / 6.5 + 0.5
#         return consump
#
#
# costume1 = Costume(1.89)
# winter_coat = Coat(46)
#
# print(costume1.h)
# print(winter_coat.s)
# print(costume1.consumption(1.89))
# print(winter_coat.consumption(46))


# print('Assignment 3')
#
#
# class Cell:
#     def __init__(self, nucl):
#         self.nucl = int(nucl)
#         print(f'The cell contains {self.nucl} nuclei')
#
#     def __add__(self, other):
#         return f'The merged cell contains {self.nucl + other.nucl} nuclei.'
#
#     def __sub__(self, other):
#         if self.nucl >= other.nucl:
#             return f'The result of cells subtraction is {self.nucl - other.nucl}'
#         else:
#             return f'Subtraction is not possible'
#
#     def __mul__(self, other):
#         return f'The resulting cell contains {self.nucl * other.nucl} nuclei.'
#
#     def __truediv__(self, other):
#         return f'The divided cell contains {int(self.nucl / other.nucl)} nuclei.'
#
#     def make_order(self, c_in_row):
#         row = ''
#         for i in range(int(self.nucl / c_in_row)):
#             row = row + f'{"*" * c_in_row}\n'
#         row = row + f'{"*" * (self.nucl % c_in_row)}'
#         return row
#
# cell1 = Cell(15)
# cell2 = Cell(5)
# cell3 = Cell(26)
# print(cell1 + cell2)
# print(cell1 - cell2)
# print(cell1 - cell3)
# print(cell1 * cell2)
# print(cell1 / cell2)
# print(cell1.make_order(4))

