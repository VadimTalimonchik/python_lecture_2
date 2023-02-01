colors = ['red ', 'green ', 'blue2 ']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей небудет
data.close()