#Дано: денежная сумма (amount > 0).
#Задание: написать программу, которая распечатает число в принятом денежном формате XXX,XXX.XX.
#Пример: amount = 100500.157; результат = 100,500.16
print('Задание 4')
print('Enter amount, for example 189.258436:')
sum= float(input())
print("Rounded amount =", '{0:,.2f}'.format(sum))