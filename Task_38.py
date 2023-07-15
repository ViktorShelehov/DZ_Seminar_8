# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных



from pathlib import Path
import os

current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'phonebook.txt')

FILE_PATH = Path(file_path)
print(FILE_PATH)

def add_contakt():                                                     #функция ввода контакта
    with open(FILE_PATH, 'a', encoding='utf8') as file:
        info = input('Введите данные: ')
        file.write(f'\n{info}')



def open_contakt():                                                    #функция вывода контакта
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        print(*[line for line in file])
        #print(file.readlines())


def find_contakt():                                                    #функция поиска контакта
    list_1 = []
    serch = input('Введите искомое: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contackt in file:
            if serch in contackt:
                 list_1.append(contackt)
        print(*[line for line in list_1])

def update_contact():                                                   # Функция изменения контакта
    search = input('Введите имя или фамилию контакта для изменения: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        lines = file.readlines()
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        updated = False
        for line in lines:
            if search in line:
                new_data = input(f'Введите новые данные для контакта "{line.strip()}": ')
                file.write(f'{new_data}\n')
                updated = True
            else:
                file.write(line)
        if not updated:
            print('Контакт не найден.')

def delete_contact():                                                    # Функция удаления контакта
    search = input('Введите имя или фамилию контакта для удаления: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        lines = file.readlines()
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        deleted = False
        for line in lines:
            if search in line:
                print(f'Удален контакт: {line.strip()}')
                deleted = True
            else:
                file.write(line)
        if not deleted:
            print('Контакт не найден.')

def choouse():                                                         # кейс
    flag = True
    while flag:
        n = input('Введите действие: ')
        match n:
            case '1':
                add_contakt()
            case '2':
                open_contakt()
            case '3':
                find_contakt()
            case '4':
                update_contact()
            case '5':
                delete_contact()
            case '6':
                flag = False

choouse()