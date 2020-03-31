'''1. Создайте декоратор, который обернет любую функцию и будет выполнять:
- вывод строки до выполнения функции: «Code before function»;
- выполнение переданной функции;
- вывод строки после выполнения функции: «Code after function».
'''
print('* 1 *******************************')
def dec(func):
    def wrapper():
        print("Code before function")
        func()
        print("Code after function")
    return wrapper

@dec
def hello():
    print('Middle code')

hello()

'''2. Extend your decorator code to adding one more decorator for existing function, use pattern like "@decorator" for your function.
- add second decorator to your function to print out one more string "This is one more line"'''
print('* 2 *******************************')
def dec2(func):
    def wrapper():
        func()
        print('This is one more line')
    return wrapper

@dec2
@dec
def hello():
    print('Middle code')

hello()

'''3. Создайте программу, которая будет принимать число (n), введенное пользователем, и выдавать результат в виде (n+nn)'''
print('* 3 *******************************')
#n = input('input number: ')
n = '5' #test
print(int(n)+int(n+n))

'''4. Создайте переменную со значением 46 и переменную со значением "string".
- Последнюю переменную умножьте на 5.
- Выведите на экран обе переменные.'''
print('* 4 *******************************')
n = 46
s = 's'
print(n, 5*s)

'''5. Напишите программу, которая будет разделять число с четырьмя цифрами на отдельные цифры. Пример:
Число 5934
Результат 5, 9, 3, 4'''
print('* 5 *******************************')
s = 5934
print(str(s)[0]+', '+str(s)[1]+', '+str(s)[2]+', '+str(s)[3])

'''7. Создайте программу, которая выяснит сколько семерок в числе 136.'''
print('* 7 *******************************')
print(136//7)

'''15. Из двух чисел с разной четностью вывести на экран четное число. a, b - данные числа.'''
print('* 15 *******************************')
a,b = 15,10
print(a if a%2==0 else b)