from math import factorial #Импортируем функцию факториал из библиотеки math
n = int(input("Введите число: "))
sum = 0 
for i in range(n+1): #Для i от 0 до n включительно
    if i == 0: #Если i равно 0, то добавляет 1 к sum
        sum += 1
    else: #Иначе, добавляем 1/i! к sum
        sum += 1 / factorial(i)
print("{:.5f}".format(sum)) #"{:.5f}".format используется для того, чтобы в ответе выводилось 5 цифр после запятой и не более
