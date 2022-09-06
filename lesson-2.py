# print('Assignment 1')
# address = ['Belarus', 'Minsk', 'Leschinskogo', 51.83, 211030]
# print(address)
# for el in address:
#     print(f'{el} - {type(el)}')

# print('Assignment 2')
# my_list = []
# for el in range(6):
#     age = int(input('Enter your age: '))
#     my_list.append(age)
# print(my_list)
# for i in range(0, len(my_list), 2):
#      my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
# print(my_list)

# print('Assignment 3')
# month = int(input('Enter months: '))
# Seasons = ['Winter', 'Spring', 'Summer', 'Fall']
# if month == 1 or month == 2 or month == 12:
#     print(f'Month number {month} belongs to {Seasons[0]}')
# elif month == 3 or month == 4 or month == 5:
#     print(f'Month number {month} belongs to {Seasons[1]}')
# elif month == 6 or month == 7 or month == 8:
#     print(f'Month number {month} belongs to {Seasons[2]}')
# elif month == 9 or month == 10 or month == 11:
#     print(f'Month number {month} belongs to {Seasons[3]}')
# else:
#     print('Wrong entry')

# month = int(input('Enter months: '))
# Seasons = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
# if month == 1 or month == 2 or month == 12:
#     print(Seasons.get(1))
# elif month == 3 or month == 4 or month == 5:
#     print(Seasons.get(2))
# elif month == 6 or month == 7 or month == 8:
#     print(Seasons.get(3))
# elif month == 9 or month == 10 or month == 11:
#     print(Seasons.get(4))
# else:
#     print('Wrong entry')


# print('Assignment 4')
# Complaints = str(input('Write your complaints: '))
# Compl_list = Complaints.split()
# print(Compl_list)
# for i, el in enumerate(Compl_list, 1):
#     if len(str(Compl_list)) <= 10:
#         print(f'{i}. {el.title()}')
#     else:
#         print(f'{i}. {el.title() [0:10]}')


# print('Assignment 5')
# rating = [56, 43, 41, 37, 25, 17]
# print(f'{rating} (max 10 entries)')
# element = int(input('Enter you rate: '))
# while len(rating) <= 9:
#     for el in range(0, len(rating)):
#         if rating[el] == element:
#             rating.insert(el+1, element)
#             break
#         elif rating[0] < element:
#             rating.insert(0, element)
#             break
#         elif rating[-1] > element:
#             rating.append(element)
#             break
#         elif rating[el] > element > rating[el + 1]:
#             rating.insert(el + 1, element)
#             break
#     print(rating)
#     element = int(input('Enter you rate: '))



