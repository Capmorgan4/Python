# print('First assignment')
# number_of_patients = input('enter number of patients: ')
# print(number_of_patients)
# number_of_effected_teeth = input('enter number of carries teeth: ')
# print(number_of_effected_teeth)
# patients_with_complaints = input('enter number of patients with complaints: ')
# print(patients_with_complaints)
#
# typy_of_complaint = input('What complaints do you have? ')
# print(typy_of_complaint)


# print('Second assignment')
# time = int(input('Insert time in seconds: '))
# hours = time // 3600
# time_rest1 = time % 3600
# minutes = time_rest1 // 60
# seconds = time_rest1 % 60
# print(f'time in h:m:s formst: {hours}:{minutes}:{seconds}')


# print('assignment 3')
# value = int(input('Insert n value: '))
# n = str(value)
# nn = n + n
# print(int(nn))
# nnn = n + n + n
# print(int(nnn))
# comp = int(n) + int(nn) + int(nnn)
# print('Result:', comp)


# print('assignment 4')
# a = int(input('Insert a: '))
# m = 0
# while a > 0:
#     if a % 10 > m:
#         m = a % 10
#     a = a // 10
# print('Maximum number is:', m)


print('Assignment 5')
employees = int(input('How many people do work in your compony? '))
earnings = int(input('What are your earnings per month (in $)? '))
profit = int(input('What is your profit per month (in $)? '))
expenses = int(input('What are your expenses per month (in $) ? '))
profitability = profit / earnings
prof_per_employee = profit / employees
if earnings > expenses:
    print('Congratulations! Your business is profitable')
    print('Profitability:', profitability)
    print('Profit per employee:', prof_per_employee)
else:
    print('You need to change your business strategy. Your business is unprofitable.')





