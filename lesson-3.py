# print('Assignment 1')
#
#
# def new_f(a = int(input('a: ')), b = int(input('b: '))):
#     try:
#        res = a / b
#     except ValueError:
#         return 'Wrong data type'
#     except ZeroDivisionError:
#         return 'Cannot devide by zero'
#     return res
#
# print(new_f())

# print('Assignment 2')


# def user(first_name, last_name, year_of_birth, city, email, tel):
#     print(f'user {first_name} {last_name} was born in {year_of_birth} in {city}. Contacts: {email}, {tel}')
#
#
# user('Nastassia', 'Kurakevich', 1988, 'Minsk', 'lv@bk.ru', 6780598)



# print('Assignment 3')
#
#
# def my_func(arg1, arg2, arg3):
#     summa = arg1 + arg2 + arg3 - min(arg1, arg2, arg3)
#     return summa
#
#
# print(my_func(4, 7, 68))

# def my_func(arg1, arg2, arg3):
#     res = [arg1, arg2, arg3]
#     total = []
#     max1 = max(res)
#     total.append(max1)
#     res.remove(max1)
#     max2 = max(res)
#     total.append(max2)
#     return sum(total)
#
# print(my_func(5, 90, 1))


# print('Assignment 4')


# def my_func(x, y):
#     i = 1
#     v = 1 / x
#     while i <= abs(y):
#         wow = v
#         i = i + 1
#         v = v * 1 / x
#     return wow
#
# print(my_func(2, -4))


# print('Assignment 5')
#
#
# def my_list():
#     total = 0
#     while True:
#         user_data = input('Enter data. For exit - #: ').split()
#         for digits in user_data:
#             if digits == '#':
#                 return total
#             else:
#                 try:
#                     total = total + int(digits)
#                 except ValueError:
#                     return 'For exit - #'
#         print('summa =', total)
#
# print(my_list())


# print('Assignment 6 and 7')
#
# def int_func():
#     wishes = input('Enter your wishes: ').lower()
#     return wishes.title()
#
# print(int_func())









