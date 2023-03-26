# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os


path = '/home/a2/tat/files'

files_with_path = []
for file_name in os.listdir(path):
    if file_name.endswith('.csv'):
        files_with_path.append(f'{path}{os.sep}{file_name}')

result = []
for file_name in files_with_path:
    for line in open(file_name):
        if line.startswith('Группировка по документу'):
            spllited = line.split()
            _3, _5 = spllited[3], spllited[5]
        if line.startswith('Назначение платежа'):
            spllited = line.split()
            _15 = spllited[15]
            result.append(f'"{_3.encode().decode("utf-8")}"|{_5}|{_15}\n')

with open('result.csv', 'w') as result_file:
    for line in result:
        result_file.write(line)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
