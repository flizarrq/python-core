# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x * self.y) + (other.x * other.y)

    def __sub__(self, other):
        return (self.x * self.y) - (other.x * other.y)

    def __eq__(self, other):
        return (self.x * self.y) == (other.x * other.y)

    def __ne__(self, other):
        return (self.x * self.y) != (other.x * other.y)

    def __lt__(self, other):
        return (self.x * self.y) < (other.x * other.y)

    def __gt__(self, other):
        return (self.x * self.y) > (other.x * other.y)

    def __len__(self):
        return self.x + self.y


rectangle1 = Rectangle(10, 11)
rectangle2 = Rectangle(10, 13)
print(len(rectangle2))
print(rectangle2 + rectangle1)

###############################################################################

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, leg_size):
        super().__init__(name, age)
        self.leg_size = leg_size
        Cinderella.__count += 1

    @classmethod
    def show_count(cls):
        print(cls.__count)


class Prince(Human):
    def __init__(self, name, age, found_size):
        super().__init__(name, age)
        self.found_size = found_size

    def find_cinderellas(self, cinderellas: list[Cinderella]):
        res = [i for i in cinderellas if i.leg_size == self.found_size]
        for i in res:
            print(i.__dict__)
            return
        print('Not found!')


cinderellas = [
    Cinderella('qwe', 23, 35),
    Cinderella('bob', 21, 232),
    Cinderella('oleg', 2, 333),
    Cinderella('kirill', 22, 35),
]

prince = Prince('bober', 24, 35)
prince.find_cinderellas(cinderellas)


###############################################################################

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом
# Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

class Printable(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def print(self):
        print(f'Book:{self.name}')


class Magazine(Printable):

    def print(self):
        print(f'Magazine:{self.name}')


class Main:
    __printable_list = []

    @classmethod
    def add(cls, item:Printable):
        if isinstance(item, Book) or isinstance(item, Magazine):
            cls.__printable_list.append(item)
        else:
            print('Ignored')
    @classmethod
    def show_all_magazines(cls):
        for i in cls.__printable_list:
            if isinstance(i, Magazine):
                i.print()

    @classmethod
    def show_all_books(cls):
        for i in cls.__printable_list:
            if isinstance(i, Book):
                i.print()


# Приклад:
#
Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))
#
Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
#
# для
# перевірки
# ксассів
# використовуємо
# метод
# isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False


# class User:
#     __slots__ = ('name', 'age')
#     __count = 0
#
#     def __init__(self, name):
#         self.__name = name
#         self.age = 15
#
#
# user1 = User('Max')
# print(user1._User__name)
# print(User._User__count)

# class User:
#     __slots__ = ('name')
#     __instance = None
#     count = 0
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls)
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#     def __init__(self, name):
#         self.name = name
#         User.count += 1
