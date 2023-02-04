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
list_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_7[0])
print(list_7[1])
print(list_7[len(list_7) - 1])
print(list_7[-1])
print(list_7[-5])
print(list_7[:])
print(list_7[:2])
print(list_7[len(list_7) - 2:])
print(list_7[2:9])
print(list_7[6:-18])
print(list_7[0:len(list_7):6]) # от начала до конца с шагом 6
print(list_7[::6])             # от начала до конца с шагом 6
