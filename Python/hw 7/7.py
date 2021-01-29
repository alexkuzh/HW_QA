'''Выведите числа от 1 до 100 с пропуском чисел 50 и 99.
Создайте вывод при помощи цикла for, а также цикла while.'''
for i in range(1,101):
    if i in (50,99):
        continue
    print(i)


i = 0
while i<100:
    i+=1
    if i in (50,99):
        continue
    print(i)
