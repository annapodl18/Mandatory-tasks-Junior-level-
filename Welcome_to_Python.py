#Дано: имя и фамилия.
#Задание: написать программу, которая будет приветствовать нового человека в мире Python.
#Текст приветсвия: Hello NAME SURNAME! You just delved into Python. Great start!


print('Enter your name:')
name= str(input())
print('Enter your surname:')
surname= str(input())


# Prefered format
print('Задание 1')
print(f"Hello {name} {surname}! You just delved into Python. Great start!")