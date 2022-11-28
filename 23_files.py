file = open('./text.txt')
# print(file.read()) #lee tpdo el archivo
# print(file.readline()) #lee de linea a linea

for line in file:
    print(line)

file.close() #cierra el archivo

with open('./text.txt') as file:
    for line in file:
        print(line)