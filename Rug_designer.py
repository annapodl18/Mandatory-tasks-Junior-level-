#Дизайнер составил шаблон домашних ковриков.
#Для массового выпуска ковриков ему нужно уметь быстро составлять макет произвольного размера.
#Известно, что длина коврика всегда больше в 3 раза чем его ширина (W = 3 * H).

#Дано: ширина коврика.

#Задание: написать программу, которая будет составлять макет коврика для его дальнейшего производства.
print('Задание 5')
print('Enter height  :')
height = int(input())
width = height * 3

for stick_count in range(1, height, 2):
    print(('||' * stick_count).center(width, '*'))

print(' Welcome to my swamp '.center(width, '*'))

for stick_count in range(height-11, 0, -11):
    print(('||' * stick_count).center(width, '*'))

