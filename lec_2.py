# запись в файл 1
# colors = ['red ', 'green ', 'blue2 ']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей небудет
# data.close()

# запись в файл 2
# colors = ['red ', 'green ', 'blue2 ']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей небудет
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close()

# запись в файл 3
# with open('file.txt', 'a') as data:
#     data.write('line 12\n')
#     data.write('line 22\n')

# чтение из файла
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()