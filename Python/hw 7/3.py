'''Выведите в цикле "while" следующую последовательность:
13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1
Важно чтобы сохранились пробелы и запятые после выполнения цикла.'''

n = 13
l = []
while n:
    n -= 1
    if n == 9:
        continue
    l.append(str(n + 1))
print(', '.join(l))

n = 14
st = ''
while n>1:
    n -= 1
    if n == 10:
        continue
    st += str(n) + ', '
print(st[:-2])