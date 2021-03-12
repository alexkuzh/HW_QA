'''1. Выведите столбец чисел от 34 до 67 с выводом только четных чисел. Используйте цикл “while” для этой задачи.'''
print('--Task 1 -----------------------')
i = 34
while i<67:
    print(i)
    i +=2
'''2. Выведите числа от 1 до 100 с пропуском чисел 50 и 99 (continue). Создайте вывод при помощи цикла “for”, а также цикла “while”.'''
print('--Task 2 -----------------------')
print([x for x in range(1,101) if (x != 50) & (x != 99)])
i = 0
x = []
while i < 100:
    i += 1
    if (i != 50) & (i != 99):
        x.append(i)
    else:
        continue
print(x)
'''3. Попросите пользователя ввести какое-либо слово, а также число. При помощи циклов "for" выведите каждый символ строки, при этом символ должен повторяться количество раз равным числу, что ввел пользователь. Каждый последующий новый символ необходимо выводить с новой строки. Мы просто перебираем все слово по каждому символу и умножаем этот символ на число, введенное пользователем.'''
print('--Task 3 -----------------------')
#txt = input('Input word ')
#num = input('Input number ')
txt = 'sdfasdf' #test 1
num = 2         #test 1
for x in txt: print(x*int(num))
'''Создайте список при помощи цикла "for", который будет состоять из 5 элементов (int).
Создайте второй пустой список и выполните над ним операции:
- добавьте в него число 5 и -6
- добавьте в него целиком весь первый список
- выполните сортировку списка
- выведите на экран оба списка без использования циклов.'''
print('--Task 4 -----------------------')
l1 = [1,2,3,4,5]
l2 = [5,-6]
l2 = l2 + l1
l2.sort()
print(l1, l2)
'''5. В программе получите строку введенную пользователем с клавиатуры.
При помощи цикла разбейте строку на символы (отдельные буквы) и каждую отдельную букву добавьте как новый элемент списка.'''
print('--Task 5 -----------------------')
#txt = input('Input string ')
txt = 'sdfsdfa afasfdawe safdf'#test 1
l = []
for x in txt: l.append(x)
print(l)
'''6. У вас есть список:
lis = ["Андрей", "Иван", "Василий", "Петро", "Максим", "Дима"]
- при помощи цикла "for" Вам необходимо вывести каждое слово из списка, после чего вывести каждую букву из каждого слова, например:
Андрей // Сначала слово целиком
А // Потом
н // каждая
д // буква
р // из этого
е // слова
й // отдельно'''
print('--Task 6 -----------------------')
lis = ["Андрей", "Иван", "Василий", "Петро", "Максим", "Дима"]
for i in lis:
    print(i)
    for x in i: print(x)
'''7. Есть список чисел:
lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
Найдите самый маленький элемент списка и переместите его в зависимости от условия:
- если найденный элемент меньше за ноль, то поместите его в конец списка
- если найденный элемент больше или равен нулю, то поместите его в начало списка.'''
print('--Task 7 -----------------------')
lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]  #test 1
#lis = [1, 34, 8, 0, 5, 7, 32, 74, 59, 92, 41, 10, 2]    #test2
min = min(lis)
lis.remove(min)
print(lis + [min] if min < 0 else [min] + lis)
'''8. Попросите пользователя ввести число в переменную N.
Добавьте в список some N количество новых элементов. Каждый элемент также должен вводить пользователь с клавиатуры. Используйте цикл “while” для этой задачи и метод "extend()".'''
print('--Task 8 -----------------------')
num = 2
some = []
output_list = []
i = 0
while i < 2:
    #txt = input()
    txt = 'asdf' #test1
    some.append(txt)
    i += 1
output_list.extend(some)
print(output_list)
'''9. Создайте функцию, принимающую два параметра: a и b. Функция должна выводить каждый параметр с новой строки.'''
print('--Task 9 -----------------------')
def foo(a,b):
    print(a)
    print(b)

foo(1,2)
'''10. Создайте функцию деления чисел, которая будет принимать три параметра. Сделайте последний параметр со значением по-умолчанию.
Вызовите функцию два раза:
- с передачей третьего параметра
- без передачи третьего параметра'''
print('--Task 10 -----------------------')
def div(a, b, c = 2):
    return (a / b / c)

print(div(18, 3, 3))
print(div(18, 3))

'''11. Создайте функцию, которая принимает заранее не установленное количество параметров. Выведите сумму всех переданных параметров.'''
print('-- Task 11 -----------------------')
def foo(l):
    return sum(l)
print(foo([1,2,3,4]))

'''12. Импортируйте модуль datetime. Он отвечает за работу с датой и временем.
Выведите на экран полную дату. Для этого используйте объект datetime и его метод now.
Из модуля импортируйте только объект datetime и добавьте к нему псевдоним.'''
print('-- Task 12 -----------------------')
from datetime import datetime as d
print(d.now().date())
'''13. Создайте случайное число в диапазоне от 0 до 20, используя модуль random и функцию randint.
Просите пользователя угадать число до тех пор, пока он его не угадает.'''
print('-- Task 13 -----------------------')
import random
a = random.randint(0,20)
print(a) #hint
while True:
    t = int(input())
    #t = a #test
    if t == a: break

'''14. Create new function with default parameter value.
Call this function to get result with default value.'''
print('-- Task 14 -----------------------')
def foo1(a=1):
    return a
print(foo1())
'''15. Create new function with passing a List as a Parameter. Call this function using "for" loop.'''
print('-- Task 15 -----------------------')
def foo2(l):
    return l
print([x for x in foo2([1,2,3,4])])
'''16. Create new function which is return result of multiplication of two any numbers and to let a function return a value, use the "return" statement.'''
print('-- Task 16 -----------------------')
def foo3(a,b):
    return(a * b)
print(foo3(2,3))
'''17. Create new function with using "Keyword Arguments". (send arguments with the key = value syntax). Call this function using this arguments.'''
print('-- Task 17 -----------------------')
def foo4(a = 3):
    return a
print(foo4(a = 4))
'''18. Create new function with unknown arguments, adding a * before the parameter name. Call this function.'''
print('-- Task 18 -----------------------')
def foo5(* a):
    return a
print(foo5(1,2,3,4,'kkjh'))
'''19. Create new function with unknown arguments, adding a ** before the parameter name. Call this function to get using Dictionary as argument.'''
print('-- Task 19 ----------------------')
def foo6(** a):
    return a
print([x for x in foo6(a = 1,b=2,c =3).values()])
'''20. Create a lambda function that adds 20 to the number passed in as an argument, and print the result.'''
print('-- Task 20 ----------------------')
x = lambda a : a + 20
print(x(1))
'''21. Create a lambda function that multiplies argument with argument b and print the result.'''
print('-- Task 21 ----------------------')
f = lambda a,b : a * b
print(f(2,3))
'''22. Create a lambda function that sums argument a, b, and c and print the result.'''
print('-- Task 22 ----------------------')
f = lambda a,b,c : a + b + c
print(f(2,3,4))
'''23. Create a lambda function inside another function that doubles the number you send in and print the result.'''
print('-- Task 23 ----------------------')
def foo7(n):
    return lambda a : a * n
double = foo7(2)
print(double(3))
'''24. Create two "int" variables, one of them == 0. Using division by zero catch this Error with "try: except" statement.'''
print('-- Task 24 ----------------------')
a = 10
b = 0
try:
    print(a / b)
except:
    print("Division by zero")
'''25. Create two "int" variables, one of them == 0.
- Using division by zero catch this Error with "try: except" statement.
- Using division by "string" catch this Error with "try: except" statement.
- add "else" statement, try to get result from "else", changing your variables.
- add "finally" statement, try to get result from "finally", changing your variables.'''
print('-- Task 25 ----------------------')
a = 10
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    print("Division by zero")
except:
    print("Division by string")
else:
    print("Changing your variables")
finally:
    print("Game over")












