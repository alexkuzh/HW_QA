'''Найдите сумму всех чисел от 5 до 57, исключив числа 34, 46 и 52.
Сделайте это при помощи цикла while и for.
'''
sum = 0
for i in range(5,58):
    if i in ( 34,46,52):
        continue
    sum += i
print(sum)

i = 5
while sum<58:
    if i in ( 34,46,52):
        continue
    i+=1
    sum += i
print(sum)