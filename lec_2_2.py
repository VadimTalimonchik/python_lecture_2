# СПИСКИ

# list_1 = []     # создание пустого списка
# list_2 = list() # создание пустого списка
# list_3 = [7, 9, 11, 13, 15, 17] # список со значениями
# print(list_1)
# print(list_2)
# print(list_3)
# print(*list_3)

# # с помощью цикла for можно перебирать значения списка
# for i in list_3:
#     print(i)

# можно узнать размер списка
# print(len(list_3))

# можно обращаться к списку поэлементно
# print(list_3[0])
# print(list_3[3])
# print(list_3[-1])

# добавление значения в список
# print(list_3)
# list_3.append(5) # добавление значения в конец списка
# print(list_3)

# # задачка
# list_4 = []
# print(list_4)
# for i in range(5): # i будет принимать значения от 0 до 4
#     list.append(i)
#     print(list_4)

# ещё функции применимые к списку

# удаление последнего элемента списка (функция pop)
# list_5 = [12, 7, -1, 21, 0]
# print(list_5)
# print('удаляет последний элемент: ', list_5.pop())
# print(list_5)
# print(list_5.pop())
# print(list_5)
# print(list_5.pop())
# print(list_5)
# a = list_5.pop()
# print('возвращает последний элемент: ', a)

# удаление конкретного элемента списка (функция pop)
# list_5 = [12, 7, -1, 21, 0]
# print(list_5.pop(0))
# print(list_5)

# добавление элемента на нужную позицию (функция insert)
# list_6 = [12, 7, -1, 21, 0]
# print(list_6)
# print(list_6.insert(2, 11)) # 1-й элемент - позиция на кот. надо вставить элемент
#                             # 2-й элемент - значение, которое надо вставить на указ. позицию
# print(list_6)

# Срезы в списках
# list_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_7[0])
# print(list_7[1])
# print(list_7[len(list_7) - 1])
# print(list_7[-1])
# print(list_7[-5])
# print(list_7[:])
# print(list_7[:2])
# print(list_7[len(list_7) - 2:])
# print(list_7[2:9])
# print(list_7[6:-18])
# print(list_7[0:len(list_7):6]) # от начала до конца с шагом 6
# print(list_7[::6])             # от начала до конца с шагом 6


# КОРТЕЖ - неизменяемый список

# t = () # создание пустого кортежа
# print(type(t))

# t = (1) # это НЕ кортеж
# print(type(t))

# t = (1,) # это кортеж
# print(type(t))

# преоброзование списка в кортеж
# v = [1, 8, 9] # список
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# # разделение кортежа на переменные (распаковка кортежа)
# a, b, c = v
# print(a, b, c)

# сходство кортежа и списка

# t = (1, 2, 3, 5,)

# # print(t[2]) # вывод элемента кортежа по индексу

# # for i in t: # с помощью цикла проходимся по всем элементам
# #     print(i)

# # следующий цикл работает как с кортежем так и со списком

# for i in range(len(t)):
#     print(t[i])

# СЛОВАРИ

# d = {}     # пустой словарь
# d = dict() # пустой словарь

# d['q'] = 'qwerty' # создание словаря
# print(d)          # вывод словаря

# d['w'] = 'werty'
# print(d)
# print(d['q']) # вывод значения по ключу

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)
# print(dictionary['left'])
# print(dictionary['up'])

# dictionary['down'] = '▼'
# print(dictionary['down'])

# # print(dictionary['type']) # KeyError: 'type'

# del dictionary['left']
# print(dictionary)

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
# # или
# # for(k, v) in dictionary.items():
# #     print('{}: {}'.format(k, v))

# for item in dictionary:
#     print(item) # вывод ключей

# вывод списка [...], где каждый элемент является кортежем из двух элементов,
# 1-й - это ключ из словаря, 2-й - это значение из словаря
# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary.items())

# МНОЖЕСТВА

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red') # добавление значения в множества, если уже есть, то не добавит
# print(colors)
# colors.add('gray') # добавление значения в множества
# print(colors)
# colors.remove('red')
# print(colors)
# # colors.remove('red') # удаление элемента из множества
# # print(colors) # KeyError: 'red', если такого значения нет, то выдаст ошибку
# colors.discard('red') # проверка, если элемента нет, то выводит имеющееся множество
# print(colors)
# colors.discard('green') # проверка, если элемент есть, то его удоляет
# print(colors)
# colors.clear() # удоляет все элементы множества
# print(colors)

# q = set() # создание множества

# операции со множествами

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # копирование одного множества в другое
# print(c)
# u = a.union(b) # объединение множеств a и b
# print(u)
# i = a.intersection(b) # пересечение множеств a и b
# print(i)
# dl = a.difference(b) # разность a из b
# print(dl)
# dr = b.difference(a) # разность b из a
# print(dr)

# q = a.union(b).difference(a.intersection(b))
# print(q)
# 1) находим пересечение a и b - (a.intersection(b))
# 2) объединяем a и b - a.union(b)
# 3) из полученного множества находим разность с этим
#    множеством - a.union(b).difference(a.intersection(b))

# создание "замороженного" множества, т.е. неизменяемое:
# 1) создаём обычное множество;
# 2) создаём замороженное множеста на основе созданного в 1-ом шаге.
# a = {1, 8, 6}
# b = frozenset(a)
# print(b)

