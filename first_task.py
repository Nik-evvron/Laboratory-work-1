# 1 задание

print('Введите число с плавающей точкой:')
a = float(input())

print('Введите слово:')
s = input()

print('Введите строку:')
st = input().split()

print('Введите числа через пробел:')
sp = list(map(int, input().split()))
sp.sort()

kort = ('a', 'b', 'c', 'd')  # кортеж с внесенными данными

print()
print('Округленное число:')
print(round(a))
print('Слово записано наоборот:')
print(s[::-1])
print('Разделение строки на объекты:')
print(st)
print('Сортировка списка от меньшего к большему:')
print(sp)
print('Тип переменной:')
print(type(kort))
