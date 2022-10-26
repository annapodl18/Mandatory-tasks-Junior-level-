#Дано: маркер (символ) и толщина фигуры.
#Задание: написать программу, которая будет отображать заданную фигуру.

print('Задание 2')

print('Enter figure thickness :')
figure_thickness = int(input())


item_signl = ''
item_empty = ''

for i in range(0, figure_thickness):
  item_signl += 'ш'
  item_empty += ' '


horizontal_empty = item_signl + item_empty + item_signl + item_empty + item_signl
horizontal = item_signl + item_signl + item_signl + item_signl + item_signl


for i in range(0, 5):
 print(horizontal_empty)
for i in range(0, 2):
 print(horizontal)