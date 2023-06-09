# #ДЗ
#
# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'
onlynums = ','.join(i for i in st if i.isdigit())
print(onlynums)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34'
print(','.join((''.join(ch if ch.isdigit() else ' ' for ch in st)).split()))

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
upp = [i.upper() for i in greeting]
print(upp)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

print([i ** 2 for i in range(50) if i % 2 != 0])


# function
#
# - створити функцію яка виводить ліст

def show_list(list):
    print(list)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def show_max(a, b, c):
    print(max(a, b, c))
    return max(a, b, c)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def show_max_min(*args):
    print(max(args))
    return min(args)


print(show_max_min(1, 100, -100))


# - створити функцію яка повертає найбільше число з ліста

def maxfromlist(list):
    return max(list)


# - створити функцію яка повертає найменьше число з ліста

def maxfromlist(list):
    return min(list)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sumlist(list):
    return sum(list)


print(sumlist([1, 2, 3, 34, 44]))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
def avg(list):
    return sum(list) // len(list)


print(avg([1, 2, 3, 4, 5]))

# ################################################################################################
# 1)Дан list:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#   - знайти мін число

def findmin(list):
    print(min(list))


#   - видалити усі дублікати

def deletedupl(list):
    print(set(list))


#   - замінити кожне 4-те значення на 'X'
def changefourtel(list):
    print(['X' if i % 4 == 0 else ch for i, ch in enumerate(list)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def quadrat(a):
    for i in range(a):
        if i == 0 or i == a - 1:
            print('*' * a)
        else:
            print('*' + ' ' * (a - 2) + '*')


# 3) вывести табличку множення за допомогою цикла while

def table():
    i = 1
    while i <= 9:
        j = 1
        while j <= 9:
            res = i * j
            print(f'{res:4}', end='')
            j = j + 1
        print()
        i = i + 1


# 4) переробити це завдання під меню

while True:
    print('1) find min')
    print('2) delete duplicates')
    print('3) change every 4-th element')
    print('4) quadrat')
    print('5) table')
    print('0) exit')

    choice = input('make ur choice: ')

    if choice == '1':
        findmin(list)
    elif choice == '2':
        deletedupl(list)
    elif choice == '3':
        changefourtel(list)
    elif choice == '4':
        a = int(input('enter a: '))
        quadrat(a)
    elif choice == '5':
        table()
    elif choice == '0':
        break
    else:
        print('error(')
