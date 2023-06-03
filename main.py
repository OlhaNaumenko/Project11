"""mult = lambda a, b, c: a*b*c
print(mult(5, 2, 9))
res = mult(5, 2, 9)
print(res)

def mulddef(a,b,c):
    return a*b*c

print(mulddef(5,2,9))
result = mulddef(5, 2, 9)
print(result)"""

import math

# ads = lambda a, b: math.sqrt(a*a + b*b)
# res = ads(3,4)
#
# def ads_def(a,b):
#     return math.sqrt(a*a + b*b)
# res_def = ads_def(9,7)
#
# print(res)
# print(res_def)


# discr = lambda a,b,c:b*b -4*a*c
# print(discr(3,4,5))
#
# def discr_def(a,b,c):
#     return b*b - 4*a*c
# print(discr_def(3,4,4))

"""import random

spysok = [lambda :random.random(),
          lambda :random.random(),
          lambda :random.random()]
for i in spysok:
    print(i())"""

# cort = (lambda x: x*2,
#         lambda x : x*3,
#         lambda x : x*5)
# for i in cort:
#         print(i(2))
# for i in cort:
#         print(i('qwerty'))

"""slovnyk={1:(lambda : print('ponedilok')), 2:(lambda : print('vivtorok')),
         3:(lambda : print('sereda')), 4:(lambda : print('chetver')),
         5:(lambda : print('pyatniza'))}
answer = int(input('chyslo vid 1 do 5 -> '))
try:
        slovnyk[answer]()
except KeyError:
        print('incorrect value')"""

# area = {'circle': (lambda  r: math.pi*r*r),
#         'rectangle': (lambda  a,b: a*b),
#         'trapezoid': (lambda a,b,h: (a+b)*h/2)}
# answer = input('Enter figure -> ')
# if answer.lower()=='circle':
#         answer1 = int(input('enter r -> '))
#         print('Площа круга = ', area['circle'](answer1))
# elif answer.lower()=='rectangle':
#         answer1 = int(input('enter a -> '))
#         answer2 = int(input('enter b -> '))
#         print('Площа трикутника = ',area['rectangle'](answer1,answer2))
# elif answer.lower()=='trapezoid':
#         answer1 = int(input('enter a -> '))
#         answer2 = int(input('enter b -> '))
#         answer3 = int(input('enter h -> '))
#         print('Площа трапеції = ', area['trapezoid'](answer1, answer2, answer3))

"""summ = lambda a=1, b=2, c=3: a+b+c
print(summ())
print(summ(5))
print(summ(10,20))
print(summ(10,20,25))"""

import random
"""def randNum():
        n = random.random()
        res = lambda : int(n*100)
        return res()

print(randNum())"""

"""calc = {'+': (lambda  a,b: a+b),
        '-': (lambda  a,b: a-b),
        '*': (lambda  a,b: a*b),
        '/': (lambda  a,b: a/b),
        '^2': (lambda  a: a*a)}
answer = input('Введіть дію +, -, *, /, ^2 -> ')
if answer == '+':
        a = int(input('enter a -> '))
        b = int(input('enter b -> '))
        print(a, ' + ', b, ' = ', calc['+'](a,b))
elif answer == '-':
        a = int(input('enter a -> '))
        b = int(input('enter b -> '))
        print(a, ' - ', b, ' = ', calc['-'](a,b))
elif answer == '*':
        a = int(input('enter a -> '))
        b = int(input('enter b -> '))
        print(a, ' * ', b, ' = ', calc['*'](a,b))
elif answer == '/':
        a = int(input('enter a -> '))
        b = int(input('enter b -> '))
        print(a, ' / ', b, ' = ', calc['/'](a,b))
elif answer == '^2':
        a = int(input('enter a -> '))
        print(a, '^2 ', ' = ', calc['^2'](a))"""

# max = (lambda a,b: a if a>b else b)
# print(max(23,70))
# print(max(21,4))

"""minimum = (lambda  a,b,c: a if (a<=b) and (b<=c) else (b if (b<=a) and (b<=c) else c ))
print(minimum(21,34,56))
print(minimum(34,21,56))
print(minimum(3,2,1))"""

"""def mnoj_dva(x):
        return x*2

spysok = [6,1,2,3,4,5,7,8]

spysok2 = list(map(mnoj_dva, spysok))
print(spysok2)

spysok3 = list(map((lambda x:x*2), spysok))
print(spysok3)"""

# cort = (2.88, -5.97, 9.78)
# cort2 = tuple(map((lambda x: int(x)), cort))
# print(cort2)

"""cort = ('qwerty', 'hello', 'abc', 'qwe', 'jkl', 'word')
cort2 = tuple(filter((lambda x:len(x)==3), cort))
print(cort2)"""

"""spysok = [3,5,2,12,15,25,57,150,3,1,9,60,56,45,98]
spysok2 = list(filter((lambda  x: (x>=10) and (x<=60)), spysok))
spysok3 = list(filter((lambda  x: (x<=10) or (x>=60)) or (x == 25), spysok))
print(spysok2)
print(spysok3)

def vid10do30(x):
        return (x>=10) and (x<=30)
spysok4 = list(filter(vid10do30, spysok))
print(spysok4)"""

import re
"""spysok1 = 'Bob Anna Alice Alex Gena bBob aBob'
spysok2 = 'abc qwe rty gfd'
vyraz = re.compile('Bob') # compile - створення рядку який шукаєм
vyraz2 = re.compile('qwe')
match1 = vyraz.search(spysok1) # search - позиція першого входження елементу
print(match1)
match2 = vyraz.search(spysok2) # якщо елемент не знайдено - None
print(match2)

match3 = vyraz.finditer(spysok1) # finditer - знайти усі збіги і їх позиції
print(match3)
for i in match3:
        print(f'match1 - {i}')

match4 = vyraz.findall(spysok1) # findall - знайти усі збіги і помістити їх у список
print(match4)
print(len(match4))

poshuk = re.compile('rty')
new = poshuk.sub('hello World', spysok2) # sub - заміна патерну на інше значення
print(new)
"""

# rechennya = 'по всім питанням писати на пошту qwerty_1@gmail.com, або на newaddress@ukr.net, або на itstep-123@outlook.com'
# emails = re.findall(r'[\w]+@[\w\.-]', rechennya) # \w - цифри, букви і _
# for i in emails:
#         print(i)

import tkinter as tk
import re
# ^ - початок рядка
# $ - рядок закінчився
login_pattern = re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
password_pattern = re.compile(r'^\w{8,16}$')
root = tk.Tk()
root.geometry('400x250+700+500')
root.resizable(False, False)
def logining():
        pass
login_label = tk.Label(root, text='Login', font=('Arial',14), padx=50)
password_label = tk.Label(root, text='Password', font=('Arial',14), padx=50)
root.grid_columnconfigure(0,minsize=150)
login_label.grid(column=0, row=0)
root.mainloop()







