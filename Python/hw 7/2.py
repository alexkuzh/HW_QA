'''Найдите сумму чисел от 1 до 100, которые кратны 4.'''
print(sum(list(range(0, 101, 4))))

summa = 0
for i in range(0, 101, 4):
    summa += i
print(summa)
