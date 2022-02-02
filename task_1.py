# задание 1

a = 4
b = 5
print(a + b)
c = 5
d = 2
print(c - d)
number_1 = int(input("Введите первое число: "))
print(number_1)
number_2 = int(input("Введите второе число: "))
print(number_2)
print(number_1 - number_2)

# задание 2

time = int(input("Введите время в секундах: "))
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
print(f"Время в формате чч:мм:сс {hour} : {minutes} : {time}")

#задание 3

n = int(input("Введите число: "))
temp = str(n)
n1 = temp + temp
n2 = temp + temp + temp
comp = n + int(n1) + int(n2)
print("Сумма чисел n + nn + nnn: " , comp)

#задание 4

n = int(input("Введите целое положительное число: "))
max = 0
while n > 0:
    a = n% 10
    if a >= max: max = a
    n //= 10
    print(max)


#задание 5$6

profit = int(input("Введите выручку: "))
outlay = int(input("Введите издержки : "))
if profit > outlay:
    profitability = profit - outlay
    print(f"Выручка больше издержек. Прибыльность составляет: {profitability}")
    workers = int(input("Введите количество сорудников фирмы: "))
    print(f"Прибыль в расчете на одного сотрудника составляет: {profit / workers}")
elif profit < outlay:
    losses = outlay - profit
    print(f"Издержки больше выручки. Убытки составляет: {losses}")
else:
    print(f"Прибыль равна издержкам")

#задание 7

a = int(input("Введите результат в км: "))
b = int(input("Введите желаемый результат в км: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + 0,1 * a
    day += 1
print(f"Результат будет достигнут на {day} день" )






