# Напишите программу, удаляющую из текста все слова, содержащие "abc".
# Примечание Текст находится в файле. Его надо считать, текст исправить, исправленный текст записать в новый файл.
# Использовать вложенный менеджер контекста

with open('data_imp.txt', 'r') as f:
    imp_data = f.read()
change_data = imp_data.split()
new_data = [i for i in change_data if 'abc' not in i]

result_data = ''
for i in new_data:
    result_data += i+' '

with open('new.txt', 'w') as f:
    f.writelines(result_data)