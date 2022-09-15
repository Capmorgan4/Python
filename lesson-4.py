
# from sys import argv
#
# print(f'total_hours = {argv[1]}, rate = {argv[2]}, bonus = {argv[3]}')
# path, total_hours, rate, bonus = argv
# p1, p2, p3 = map(int, argv[1:])
#
#
# def payment():
#     zarplata = p1 * p2 + p3
#     return f'Month payment: {zarplata}'

# print(payment())

# print('Assignment 2')
#
# Old_list = [498, 5, 13, 44, 2, 3, 4, 11, 9, 1, 78, 567, 53]
# New_list = [Old_list[el] for el in range(1, len(Old_list)) if Old_list[el] > Old_list[el - 1]]
#
# print(New_list)


# print('Assignment 3')
#
# spis = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
# print(spis)


# print('Assignment 4')
#
# s1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# s2 = [el for el in s1 if s1.count(el) == 1]
# print(s2)


# print('Assignment 5')
#
# from functools import reduce
# def gen_f(el1, el2):
#     return el1 * el2
#
# gen1 = [el for el in range(100, 1001) if el % 2 == 0]
# print(gen1)
# print(reduce(gen_f, [el for el in gen1]))


# print('Assignment 6')
#
# from itertools import count, cycle
#
# def it_list():
#     for el in count(10):
#         print(el)
#         if el > 100:
#             break

# print(it_list())


# def sp_func():
#     sp = ['summer', 'fall', 'winter', 'spring']
#     i = 0
#     for el in cycle(sp):
#         i = i + 1
#         if i > 20:
#             break
#         print(el)
#
# print(sp_func())


print('Assignment 7')

def fact(n):
    f = 1
    for i in range(1, n + 1):
       f = f * i
    yield f

for el in fact(4):
    print(el)








