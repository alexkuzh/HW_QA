'''
1. Create 2 (int) variables with different values
- Print a message based on whether the condition is True or False:
print "b is greater than a" if b > a, or print "b is not greater than a" if b < a.
'''

a = 10
b = 20
print('Task 1')
print('b is greater than a' if b > a else 'b is not greater than a')
print('-' * 30)

'''
2. Create 2 (int), (str) variables
- evaluate two variables using "bool()" method.
- print result
'''
a = 10
st = 'a'
print('Task 2')
print('a to bool = ', bool(a),'; st to bool = ',bool(st))
print('-' * 30)

'''
3. Create 3 (int), (str), (list) variables with different values which is returning "True" value
- print result
- change existing variables to returning "False" for all of them
- print result
'''
l = ['a']
print('Task 3')
print('a to bool = ', bool(a),'; st to bool = ',bool(st), '; list to bool = ', bool(l))
a = 0
st = ''
l = []
print('after change: a to bool = ', bool(a),'; st to bool = ',bool(st), '; list to bool = ', bool(l))
print('-' * 30)

'''
4. Create 1 (int) variable with value = 5
- print True if 5 is greater than 3 AND 5 is less than 10
'''
a = 5
print('Task 4')
print(True if (a > 3) & (5 < 10) else False)
print('-' * 30)

'''
5. Create 1 (int) variable with value = 5
- print True if one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
'''
a = 5
print('Task 5')
print(True if (a > 3) | (5 > 4) else False)
print('-' * 30)

'''
6. Create 1 (int) variable with value = 5
use "not" to make this statement False:
"True if 5 is greater than 3 AND 5 is less than 10"
'''
a = 5
print('Task 6')
print(not(True if (a > 3) & (5 < 10) else False))
print('-' * 30)

'''
7. Create new object like a list with 3 values
- print True if a sequence with the one of specified value is present in the object
- change this list to get False with the same print
- print new result and expect False there
'''
l = [1,2,3]
a = 1
print('Task 7')
print(True if a in l else False)
l = [0,2,3]
print('changed list: ',True if a in l else False)
print('-' * 30)

'''
8. Create new list with 3 different values
- print new list
- print the second item of the list
- print the last item of the list
'''
l = [1,2,3]
print('Task 8')
print(l)
print(l[1])
print(l[-1])
print('-' * 30)

'''
9. Create new list with 7 different values
- print the third, fourth, and fifth item
- print the items from index -4 (included) to index -1 (excluded)
- change the value of the second item
- print new result
'''
l = [1,2,3,4,5,6,7]
print('Task 9')
print(l[2:5])
print(l[-4:-1])
l[1] = 10
print(l)
print('-' * 30)

'''
10. Create new list with 5 different values
- print all items in the list, one by one, using "for" loop
- print the number of items in the list, using "len()" method
- add new item to the end of the list, using the "append()" method
- print new list
- Insert new item as the second position, using "insert()" method
- print new list
- remove second item from list, using "remove()" method
- print new list
- remove last item from list, using "pop()" method
- print new list
- remove item with index "1" from list, using "pop()" method
- print new list
- remove item with index "0" from list, using "del" method
- print new list
- empty list using "clear()" method
- print new list
- delete entire list using "del" method
- print result, you should get an error
'''
print('Task 10')
l = [1,2,3,4,5]
for x in l: print(x)
print('len = ',len(l))
l.append('10')
print('append ',l)
l.insert(1, 11)
print('insert ', l)
l.remove(11)
print('remove ', l)
l.pop()
print('pop ', l)
l.pop(1)
print('pop(1) ', l)
del l[0]
print('del 0 ', l)
l.clear()
print(l)
del l
#print(l)  # l has deleted

'''
11. Create new list with 5 different values
- make a copy of a list with the "copy()" method
- print new list
- make a copy of a new list with the "list()" method:
- print new list
'''
l = [1, 2, 3, 4, 5]
l2 = l.copy()
print('Task 11')
print(l2)
l3 = list(l)
print(l3)
print('-' * 30)

'''
12. Create 2 new list with 3 different values each
- join this two list using the "+" operator.
- print new list
'''
l = [1, 2, 3]
l1 = [4, 5, 6]
print('Task 12')
print(l + l1)
print('-' * 30)

'''
13. Create 2 new list with 3 different values each
- join this two list using the "append()" method.
- print new list
'''
l = ["a", "b", "c"]
l1 = [1, 2, 3]
for x in l:
    l1.append(x)
print('Task 13')
print(l1)
print('-' * 30)

'''
14. Create 2 new list with 3 different values each
- join this two list using the "extend()" method.
- print new list
'''
l = ["a", "b", "c"]
l1 = [1, 2, 3]
l.extend(l1)
print('Task 14')
print(l)
print('-' * 30)

'''
15. Create new list using the "list()" constructor.
- print new list
'''
l = list(("a", "b", "c"))
print('Task 15')
print(l)
print('-' * 30)

'''
16. Create new list using the "list()" constructor.
- add 8 new values, 4 of them is the same and has "rain" value
- print the number of times the value "rain" appears int this list, using "count()" method
'''
l = list(("sky", "sky", "cloud", "cloud", "rain", "rain", "rain", "rain"))
print('Task 16')
print(l.count("rain"))
print('-' * 30)

'''
17. Create new list with 3 different values
- reverse the order of this list, using "reverse()" method
- print reversed list
'''
l = [1, 2, 3]
print('Task 17')
l.reverse()
print(l)
print('-' * 30)

'''
18. Create new Tuple with 3 different values
- print new tuple
- print the second item of the tuple
- print the last item of the tuple
- print the second item from the end using (-) indexing
'''
t = (1, 2, 3)
print('Task 18')
print(t)
print(t[1])
print(t[-1])
print(t[-2])
print('-' * 30)

'''
19. Create new Tuple with 7 different values
- print new tuple with third, fourth, and fifth item only, using "range" indexing [ : : ]
- print new tuple with items from index -4 (included) to index -1 (excluded)
'''
t = (1, 2, 3, 4, 5, 6, 7)
print('Task 19')
print(t[2:5])
print(t[-4:-1])
print('-' * 30)

'''
20. Create new Tuple with 3 different values
- convert the tuple into a list to be able to change it, using "list()" method
- change second value
- convert it back from list to tuple, using "tuple()" method
'''
t = (1, 2, 3)
print('Task 20')
l = list(t)
l[1] = 5
print(tuple(l))
print('-' * 30)

'''
21. Create new Tuple with 5 different values
- loop through the tuple items by using a "for" loop
- print result
'''
t = (1, 2, 3, 4, 5)
print('Task 21')
print(tuple([x for x in t]))
print('-' * 30)

'''
22. Create new Tuple with 5 different values with one of then has value "gold"
- check if "gold" is present in the tuple, using "in" keyword
- print result
'''
t = (1, 2, 'gold', 4, 5)
print('Task 22')
print(True if 'gold' in t else False)
print('-' * 30)

'''
23. Create new Tuple with 5 different values
- Print the number of items in the tuple using "len()" method
'''
t = (1, 2, 'gold', 4, 5)
print('Task 23')
print(len(t))
print('-' * 30)

'''24. Create new Tuple with 2 different values
- try to add a new item to the tuple using "yourtuple[ ]" method, (you should get an error)
'''
t = (1, 2)
print('Task 24')
# t[3] = 3 #raise error
print(t)
print('-' * 30)

'''25. Create Tuple With One Item using "newtuple(*,)" method
- print new tuple
'''
print('Task 25')
t = (1, 2, 3,)
print(t)
print('-' * 30)

'''26. Create new Tuple with 2 different values
- delete this tuple completely using "del" method
'''
print('Task 26')
t = (1, 2)
del t
print('Tuple has been deleted')
print('-' * 30)

'''
27. Create 2 new tuples with 3 different values each
- join this tuples using "+" operator
- print result
'''
print('Task 27')
t = (1, 2, 3)
t1 = (4, 5, 6)
print(t + t1)
print('-' * 30)

'''
28. Make a new tuple using "tuple()" method with 3 different and 2 the same values
- print result
- print the number of times the same values appears in the tuple, using "count()" method
'''
print('Task 28')
t = tuple([1, 2, 3, 4, 4])
print(t)
print(t.count(4))
print('-' * 30)

'''
29. Create new Tuple with 5 different values (int) from 1 to 5
- search for the first occurrence of the value 3, and print its position
'''
print('Task 29')
t = (1, 2, 3, 4, 5)
print(t.index(3))
print('-' * 30)

'''
30. Create new Set with 3 different values 1, 3 and 6
- print result
- loop through the set, and print the values, using "for" loop
- check if "3" is present in the set using "in" method
'''
print('Task 30')
s = {1, 3, 6}
print(s)
print({x for x in s})
print(True if 3 in s else False)
print('-' * 30)

'''
31. Create new Set with 3 different values
- print result
- add a new item to a set, using the "add()" method
- print new Set
- add multiple items to a set, using the "update()" method
- print new Set
- get the number of items in a set using "len()" method
- print result
- remove any one item from Set by using the "remove()" method
- print result
- remove any one item from Set by using the "discard()" method
- print result
- remove last item from Set by using the "pop()" method
- print result
- empty your Set using "clear()" method
- print result
- delete the set completely using "del" keyword
- print result
'''
print('Task 31')
s = {1, 3, 6}
print(s)
s.add(4)
print('add ', s)
s.update([5, 7, 8])
print('update ', s)
print('len = ', len(s))
s.remove(6)
print('remove ', s)
s.discard(4)
print('discard ', s)
s.pop()
print('pop ', s)
s.clear()
print('clear ', s)
del s
# print('del ', s) #raise error
print('-' * 30)

'''
32. Create 2 new Sets with 3 different values each
- Join Two Sets using "union()" method and assign new result to the new variable "newSet"
- print result
- create one more set, using "set()" constructor, and join this set and "newSet" using "update()" method
- print new result'''
print('Task 32')
s = {1, 3, 6}
s1 = {2, 4, 5}
newSet = s.union(s1)
print(newSet)
s2 = set([8, 9, 10])
newSet.update(s2)
print(newSet)
print('-' * 30)

'''
33. Create new Set with 3 different values
- make a copy of this Set using "copy()" method'''
print('Task 33')
s = {1, 3, 6}
s1 = s.copy()
print(s1)
print('-' * 30)

'''
34. Create 2 new Sets with 3 different values each and 2 same values
- print a set that contains the items that only exist in set one, and not in set two, using "difference()" method
- remove the items that exist in both sets using "difference_update()" method
- print result'''
print('Task 34')
s = {1, 2, 3, 4, 5}
s1 = {4, 5, 6, 7, 8}
print(s.difference(s1))
s.difference_update(s1)
print(s)
print('-' * 30)

'''
35. Create and print a dictionary with 3 different "keys : values"
- get the value of the first key
- print result
- get the value of the second key using "get()" method
- print result
- change your first key value
- print new result
- print all KEY NAMES in the dictionary, one by one using "for" loop
- print all VALUES in the dictionary, one by one using "for" loop
- print values of a dictionary using "values()" function
- loop through both keys and values, by using the "items()" function:'''
print('Task 35')
d = {
    'name': 'John',
    'car': 'BMW',
    'height': 180
}
print(d.get('name'))
print(d.get('car'))
d['name'] = 'Mark'
print(d.get('name'))
print([x for x in d])
print([x for x in d.values()])
print(d.values())
print([[x, y] for x, y in d.items()])
print('-' * 30)

'''
36. Create new dictionary with 5 different "keys : values"
- print result
- check if specified key is present in a dictionary use the "in" keyword
- print result
- print the number of items in the dictionary using "len()" method
- add new item to the dictionary by using a new index key and assigning a value to it
- print result
- remove item with the specified key name from dictionary using "pop()" method
- print result
- remove last item from dictionary using "popitem()" method
- print result
- delete item with the specified key name from dictionary using "del" keyword
- print result
- empties the dictionary using "clear()" keyword
- print result
- delete the dictionary completely using "del" keyword
'''
print('Task 36')
d = {
    'name': 'John',
    'car': 'BMW',
    'height': 180,
    'color': 'white',
    'weight': 80
}
print(d)
print(True if 'name' in d else False)
d.pop('color')
print(d)
d.popitem()
print(d)
del d['name']
print(d)
d.clear()
print(d)
del d
print('-' * 30)

'''
37. Create and print a dictionary with 3 different "keys : values"
- make a copy of a dictionary with the "copy()" method
- print result
- make a copy of a dictionary with the "dict()" method
- print result'''
print('Task 37')
d = {
    'name': 'John',
    'car': 'BMW',
    'height': 180
}
d1 = d.copy()
print(d1)
d2 = dict(d)
print(d2)
print('-' * 30)

'''
38. Create a dictionary that contain three dictionaries
- print result'''
print('Task 38')
d = {
    "man1": {
        "name": "John",
        "height": 180
    },
    "man2": {
        "name": "Mark",
        "height": 170
    },
    "man3": {
        "name": "Bill",
        "height": 190
    }
}
print(d)
print('-' * 30)

'''39. Create three dictionaries, than create one dictionary that will contain the other three dictionaries
- print result'''
print('Task 39')
man1 = {"name": "John", "height": 180}
man2 = {"name": "Mark", "height": 170}
man3 = {"name": "Bill", "height": 190}
d = {"man1": man1, "man2": man2, "man3": man3}
print(d)
print('-' * 30)

'''40. Create and print a dictionary with 3 different "keys : values" using "dict()" constructor
- print result'''
print('Task 40')
d = dict(name='John', car='BMW', height=180)
print(d)
print('-' * 30)

'''41. Create two new variables "a" and "b" (int) with different values
- using "if" statement, compare the values of these variables
- print result with conditions "b is greater than a" (if any), don't forget to put space before "print"'''
print('Task 41')
a = 10
b = 20
print("b is greater than a" if b > a else None)
print('-' * 30)

'''
42. Create two new variables "a" and "b" (int) with different values
- using "if" statement, compare the values of these variables
- print result with conditions "b is greater than a" (if any), don't forget to put space before "print"
- add one more condition "elif" to compare is variables are equal (==)
- print new results with new conditions "a and b are equal" (if any), don't forget to put space before "print"
- add new condition "else"
- print new result with the statement "a is greater than b"
- remove "elif" statement and print line related to "elif"
- print updated statement'''
print('Task 42')
a = 20
b = 10
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a  is greater than b")
print('-' * 30)

'''43. Create two new variables "a" and "b" (int) with different values
- print it with One line "if" statement'''
print('Task 43')
a = 10
b = 20
if b > a: print("b is greater than a")
print('-' * 30)

'''
44. Create two new variables "a" and "b" (int) with different values
- print it with One line "if" - "else" statement'''
print('Task 44')
a = 10
b = 20
print("b is greater than a" if b > a else "b is greater than a")
print('-' * 30)

'''
45. Create 3 new variables "a", "b" and "c" (int) with different values
- using "if" and "AND" keyword as a logical operator, combine conditional statements and compare all your variable's values'''
print('Task 45')
a = 20
b = 10
c = 30
if (a > b) and (c > a):
    print("Both conditions are True")
print('-' * 30)

'''
46. Create 3 new variables "a", "b" and "c" (int) with different values
- using "if" and "OR" keyword as a logical operator, combine conditional statements and compare all your variable's values
'''
print('Task 46')
a = 20
b = 10
c = 30
if a > b or a > c:
    print("At least one of the conditions is True")
print('-' * 30)

'''
47. Create 3 new variables "a", "b" and "c" (int) with different values
- create nested "if" statements, using "if" statements inside of another "if" statements'''
print('Task 47')
x = 15
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
print('-' * 30)

'''
48. Create one new variable (int) with value == 6
- print i as long as i is less than 6
- exit the loop when i is 3 using "break" keyword
- continue to the next iteration if i is 3 using "continue" keyword
- print a message once the condition is "false" - "i is no longer less than 6"'''
print('Task 48')
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print('-' * 30)

'''49. Create new list with 3 different values: "apple", "banana", "cherry"
- print new list
- exit the loop when x is "banana", using "if" and "break"
- exit the loop when x is "banana", but this time the break comes before the print
- don't print "banana"'''
print('Task 49')
l = ["apple", "banana", "cherry"]
for x in l:
    print(x)
    if x == "banana":
        break
for x in l:
    if x == "banana":
        break
    print(x)
print('-' * 30)

'''50. Using the "range()" function:
- print x in range(6)
- using the start parameter print numbers from 2 to 5
- increment the sequence with 3 (default is 1)'''
print('Task 50')
print([x for x in range(6)])
print([x for x in range(2, 5)])
print([x for x in range(3, 12, 3)])
print('-' * 30)

'''
51. Using "else" keyword in a "for" loop:
- print all numbers from 0 to 5, and print a message when the loop has ended "Finally finished!"'''
print('Task 51')
for x in range(6):
    print(x)
else:
    print("Finally finished!")
print('-' * 30)

'''
52. Create two new lists with 3 different values each
- create "inner loop" which is will be executed one time for each iteration of the "outer loop"

example: adj = ["red", "big", "tasty"], fruits = ["apple", "banana", "cherry"]
result is:
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry'''
print('Task 51')
l = ["red", "big", "tasty"]
l1 = ["apple", "banana", "cherry"]

for x in l:
    for y in l1:
        print(x, y)
print('-' * 30)

