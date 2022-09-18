# print('Assignment 1')
#
#
# with open(r'les5.txt', 'w+', encoding='utf-8') as new_f:
#     ctr = input('Country: ')
#     city = input('City: ')
#     str = input('Street: ')
#     bld = input('Building: ')
#     apt = int(input('Apartment: '))
#     new_f.writelines([f'Country: {ctr}\n', f'City: {city}\n', f'Street: {str}\n', f'Building: {bld}\n', f'Apartment: {apt}\n'])
#     new_f.seek(0)
#     print(new_f.read())


# print('Assignment 2')
#
# with open(r'les5.2.txt', 'w+', encoding='utf-8') as n_file:
#     n_file.writelines(['Жалобы при периодогтите:\n', '1. чувствительность при накусывании\n', '2. потемнение\n', '3. подвижность зуба\n'])
#     n_file.seek(0)
#     print(n_file.read())
#
# with open(r'les5.2.txt', 'r', encoding='utf-8') as n_file:
#     lines = 0
#     for line in n_file:
#         lines = lines + 1
#         space = 0
#         words = 0
#         for word in line:
#             if word != ' ' and space == 0:
#                 words = words + 1
#                 space = 1
#             elif word == ' ':
#                 space = 0
#         print(f'Line: {line}. Number of words: {words}')
#
#     print(f'Number of lines: {lines}')


# print('Assignment 3')
#
# low_sal_pers = []
# n_of_empl = 0
# sum_of_sals = 0
# with open(r'Les5z3.txt', 'r', encoding='utf-8') as salaries:
#     for line in salaries:
#         print(line, end="")
#         pair = line.strip('\n').split(' ')
#         if float(pair[1]) < 20000:
#             low_sal_pers.append(pair[0])
#         sum_of_sals = sum_of_sals + float(pair[1])
#         n_of_empl = n_of_empl + 1
#     average_sal = sum_of_sals / n_of_empl
#     print(f'Employees with salary < 20000: {low_sal_pers}')
#     print(f'Average salary = {average_sal}')


# print('Assignment 4')
#
# rus = ['Один', 'Два', 'Три', 'Четыре']
# eng = ['One', 'Two', 'Three', 'Four']
# rus2 = []
#
# with open(r'Les5z4.txt', 'r', encoding='utf-8') as my_f:
#     text = my_f.readlines()
#     print(text)
#     i = 0
#     for el in text:
#         rus2.append(el.replace(eng[i], rus[i]))
#         i = i + 1
#     print(rus2)
#
# with open(r'Les5z4.1.txt', 'w', encoding='utf-8') as my_f2:
#     my_f2.writelines(rus2)


# print('Assignment 5')

# with open(r'Les5z5.txt', 'w', encoding='utf-8') as f5:
#     f5.write('1 2 3 4 5 6 7 9 15 57')
#
# with open(r'Les5z5.txt', 'r', encoding='utf-8') as f5:
#     nums = f5.readline()
#     print(nums)
#     nums_list = nums.split(' ')
#     print(nums_list)
#     print(sum(map(int, nums_list)))



# print('Assignment 6')
#
# subjects = {}
# with open(r'Les5z6.txt', 'r', encoding='utf-8') as classes:
#     lessons = classes.readlines()
#     print(lessons)
#     for line in lessons:
#         subject, lectures, practice, lab = line.split(' ')
#         subject, lectures, practice, lab = subject, lectures.strip('(л)'), practice.strip('(пр)'), lab.strip('(лаб).\n')
#         hours = ''
#         for el in line:
#             hours = ''.join([hours, (el if el in '0123456789' else ' ')])
#         res_h = [int(i) for i in hours.split()]
#         subjects[subject] = sum(res_h)
#     print(subjects)



