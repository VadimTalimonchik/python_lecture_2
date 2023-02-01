# colors = ['red ', 'green ', 'blue2 ']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей небудет
# data.close()

# colors = ['red ', 'green ', 'blue2 ']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей небудет
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close()

with open('file.txt', 'a') as data:
    data.write('line 12\n')
    data.write('line 22\n')