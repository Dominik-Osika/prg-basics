print(7+4)
print((30+10)/2)
print(2**3)
print(7>5)



r=4
area=3.14159 *r * r
print(area)
area=round(area,2)



first_name = "Mary"
last_name = "Brown"
full_name = first_name + ' ' + last_name
print(full_name)
print(len(full_name))


#Pole trojkata
bok=5
wysokosc=4
pole=5*4/2
print(pole)


srednia= round((7+12+31)/3,2)
print(srednia)




number1 = 71
number2 = 14
number3 = 3
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)




x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

x,y=y,x

    # swap the values
print("After swapping: x=", x, "y=", y)


speed_kmh = 70
speed_ms = speed_kmh/3.6
print(speed_kmh, "km/h = ", speed_ms, "m/s")

import math
h=int(input("Podaj H:"))
d=3.57 * math.sqrt(h)
print(d)


import math
a = 5
b = 3
diagonal = math.sqrt(a**2 + b**2)
print(diagonal)


total = 8000000000
north = 7200000000
south = total-north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("liczba osob w south", south)
print("procent:", south/total*100)





mathematics = 5
art = 4
music = 5
history = 3
average = mathematics + art - music + history / 4
print("Average grade is", average)


father_income = 5450
mother_income = 4920
family_members = 5
total_income =  father_income + mother_income
income_per_person = total_income/5
print(f'Total family income is {total_income}, and income per person is {income_per_person}')


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')







bok1=int(input("bok1:"))
bok2=int(input("bok2:"))
bok3=int(input("bok3:"))
objetosc=bok1*bok2*bok3
print(objetosc)


name = 'Dominik'   # replace Anna with your name
surname = 'Osika' # replace May with your surname
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has ... {len(surname)} ...')
print(f'Your full name has {len(surname) + len(name)}') 


name="Dominik"
surname="Osika"
print(name[0]+surname[0])



university = "Krakow University of Economics"
print(university[0]+university[7]+university[21])


employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[-10:]}')
print(f'Initials: {employee[4]+employee[9]}')



phone=(input("Podaj numer:"))

print(phone[0:3]+ "-"+ phone[3:6] + "-" + phone[6:9])




liczby=["a", "b", "z", "A", "B", "Z", "1", "=", "+", "€"]
for i in liczby:
    i=ord(i)
    print(i)









