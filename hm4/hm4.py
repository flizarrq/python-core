# try:
#     with open(file='gmails.txt', mode='w') as gmails, open(file='emails.txt', mode='r') as emails:
#         for i in emails:
#             read = emails.readline()
#             email = read.split()[1]
#             if email.endswith('gmail.com'):
#                 gmails.write(f'{email}\n')
# except Exception as err:
#     print(err)

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

from typing import TypedDict
import json

Purchase = TypedDict('Purchase', {'id': int, 'name': str, 'price': int})


class NoteBook:
    def __init__(self):
        self.__file_name = input('Enter filename: ')
        self.__data: list[Purchase] = []
        self.__read_file()
        self.__menu()

    def __get_all(self):
        for item in self.__data:
            print(item)

    def __add(self):
        pk = self.__data[-1]['id'] + 1 if len(self.__data) else 1
        name = input('enter name of purchase: ')
        price = self.__input__int('enter price: ')
        self.__data.append({'id': pk, 'name': name, 'price': price})
        self.__write_file()

    def __find(self):
        count = 0
        search = input('enter what you want to find: ')
        for item in self.__data:
            for value in item.values():
                if search == str(value):
                    print(item)
                    count += 1
                    break
        if not count:
            print('Not found!')

    def __find_most_expensive(self):
        sorted_data = sorted(self.__data, key=lambda item: item['price'])
        if not sorted_data:
            print('not found')
            return
        for i in sorted_data:
            print(i)

    def __delete(self):
        self.__get_all()
        pk = self.__input__int('enter id to delete: ')
        index = next((i for i, v in enumerate(self.__data) if v['id'] == pk), None)
        if int(index):
            del self.__data[index]
            self.__write_file()
            print('deleted...')
        else:
            print(index)

    def __read_file(self):
        try:
            with open(file=self.__file_name, mode='r') as file:
                self.__data = json.load(file)
        except Exception:
            pass

    def __write_file(self):
        try:
            with open(file=self.__file_name, mode='w') as file:
                json.dump(self.__data, file)
        except Exception:
            pass

    def __menu(self):
        while True:
            print('1) - get all')
            print('2) - add')
            print('3) - find')
            print('4) - most expensive')
            print('5) - delete')
            print('0) - exit')
            choice = input('ur choice: ')
            match choice:
                case '1':
                    self.__get_all()
                case '2':
                    self.__add()
                case '3':
                    self.__find()
                case '4':
                    self.__find_most_expensive()
                case '5':
                    self.__delete()
                case '0':
                    break
                case _:
                    continue

    @staticmethod
    def __input__int(msg) -> int:
        while True:
            data = input(msg)

            if not data.isdigit():
                continue
            return int(data)


# NoteBook()
# *********Кому буде замало ось завдання з співбесіди
# Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]
#
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# в результат має записатись тільки 5 id
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]

res = []
gens = []

for item in data:
    gens.append((i['id'] for i in item if i['id'] not in res))
while gens and len(res) < 5:
    gen = gens.pop(0)

    try:
        res.append(next(gen))
    except StopIteration:
        continue

    gens.append(gen)
print(gens)
print(res)
