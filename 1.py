n = int(input("Введите число не меньше 2: ")) 
i = 2 
for i in range(2, int(n**0.5) + 1): # проходим цикл для i от 2 до корня из n включительно
    if n % i == 0: # если остаток от деления n на i равен 0, то выводим i
        print(i)
        break

if n % i != 0: # если остаток от деления n на i не равен нулю, то число n - простое, соответственно, выводим именно его
    print(n)
