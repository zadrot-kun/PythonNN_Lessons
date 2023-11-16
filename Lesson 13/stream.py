import sys

txt_file = open('stream.txt', 'w')
sys.stdout = txt_file

print('Начало')
print('Пример вывода в консоль')
print('Конец')
