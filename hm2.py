# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
#
# 2) протипізувати перше завдання

def notebook():
    todo_list: list[str] = []

    def add_todo(todo: str):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> None:
        nonlocal todo_list
        print(todo_list)

    return add_todo, get_all


add_todo, get_all = notebook()
add_todo('eat')
add_todo('drink')
add_todo('sleep')
get_all()


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
def expanded_form(num: int):
    st = str(num)
    length = len(st) - 1

    res = ' + '.join(ch + '0' * (length - i) for i, ch in enumerate(st) if ch != '0') + ' = ' + st

    print(res)


expanded_form(70304)
expanded_form(100001)
expanded_form(230001)


# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# \та буде виводити це значення після виконання функцій

def decor(func):
    count = 0

    def inner(*args, **kwargs):
        func(*args, **kwargs)
        nonlocal count
        count = count + 1
        print(count)

    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func2()
func2()
func2()
func1()
func1()
func2()
func1()
func2()


################ time #######################
import time
def time_fun(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        print(time.time()-start)

    return inner

@time_fun
def foo():
    for i in range(100000000):
        pass

foo()
