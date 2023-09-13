# 2 задание

def plus(a):
    print('Введите значения через знак "+":')
    sm = sum(list(map(float, input().split('+'))))
    return sm


def minus(a):
    print('Введите значения через знак "-":')
    mn = list(map(float, input().split('-')))
    mi = mn[0]
    for i in range(1, len(mn)):
        mi -= mn[i]
    return mi


def mult(a):
    print('Введите значения через знак "*":')
    mlt = list(map(float, input().split('*')))
    ml = mlt[0]
    for i in range(1, len(mlt)):
        ml *= mlt[i]
    return ml


def divide(a):
    print('Введите значения через знак "/":')
    dv = list(map(float, input().split('/')))
    d = dv[0]
    for i in range(1, len(dv)):
        d /= dv[i]
    return d


n = True
while n == True:
    a = input(
        'Введите цифру функции, которая вам нужна ([1]сложение, [2]вычитание, [3]умножение, [4]деление, [0]выход из программы)\n').lower()
    if a == '0':
        n = False
        exit
    elif a == '1':
        print(plus(a))
    elif a == '2':
        print(minus(a))
    elif a == '3':
        print(mult(a))
    elif a == '4':
        print(divide(a))
    else:
        print('Этой цифры нет в списке функций')
