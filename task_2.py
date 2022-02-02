#Задание 1
#Создать список и заполнить  его различными элементами.
#Реализовать скрипт проверки типа данных каждого элемента.
#Использовать функцию type() для проверки типа.

my_str = "Hello,world"
my_float = 8.5
my_tuple = (2, 3, 4, 5)

list = [my_str, my_float, my_tuple]
for i in list:
    print(f'{i} is {type(i)}')

#Задание 2
#Для списка реализовать обмен значений соседних элементов.
#Значениями обмениваются элементы с индексами 0 и 1,2 и 3 и т.д.
#При нечетном количестве элементы последний сохранить на своем месте.
#Для заполнения списка элементов нужно использовать функцию input().

my_list = list(input("Введите элемент: "))
l = 0
for i in range(int(len(my_list)/2)):
    my_list[l], my_list[l+1] = my_list[l+1],  my_list[l]
    l += 2
print(my_list)


#Задание 3
#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить, к какому времени года относится месяц(зима, весна, лето, осень)
#Напишите решение через list и dict

season_list = ['winter', 'spring', 'summer', 'autumn']
season_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Введите номер месяца: "))

if month == 1 or month == 2 or month == 3:
    print(season_dict.get(1))

elif month == 4 or month == 5 or month == 6:
    print(season_dict.get(2))

elif month == 7 or month == 8 or month == 9:
    print(season_dict.get(3))

elif month == 10 or month == 11 or month == 12:
    print(season_dict.get(4))


#Задание 4
#Пользователь вводит строку из нескольких слов, разделенных пробелами.
#Вывести каждое слово с новой строки.
#Строки нужно пронумеровать.
#Если слово длинное, выводить только первые 10 букв в слове.

my_str = input("Введите слова: ")
a = my_str.split(' ')

for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

#Задание 5
#Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,который не возрастает.
#У пользователя нужно запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

number = int(input("Введите натуральное число: "))
my_list = [7, 5, 4, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

#Задание 6
#Реализовать структуру данных «Товары».
#Она должна представлять собой список кортежей.
#Каждый кортеж хранит информацию об отдельном товаре.
#В кортеже должно быть два элемента — номер товара и словарь с параметрами,
#то есть характеристиками товара: название, цена, количество, единица измерения.
#Структуру нужно сформировать программно, запросив все данные у пользователя.

#Нужно собрать аналитику о товарах.
#Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
#Тогда значение — список значений-характеристик, например, список названий товаров.


goods = []
features = {'наименование': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'наименование': [],
             'цена': [],
             'количество': [],
             'единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))

goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("Введите название "),
                    'цена': input("Введите цену "),
                    'количество': input('Введите количество '),
                    'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict({'название': my_dict.get('название'),
                      'цена': my_dict.get('цена'),
                      'количество': my_dict.get('количество'),
                      'ед': my_dict.get('ед')})
    print(my_list)
print(my_analys)
