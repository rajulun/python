
__author__ = 'Ильясов Исмаил Ильясович'

import os
import l_5_easy
# NORMAL

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотр указанной папки
# 3. Удалить папку
# 4. Создать папку
# При выборе любых пунктов печатается статус "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def goto_folder(path_='.'):
    try:
        path_ = input("input path to go: ")
        os.chdir(path_)
        print('directory changed to ' + path_)
    except:
        print('path not found')

def view_folder(path_='.'):
    path_ = input("input path to view: ")
    l_5_easy.in_folder(path_)

def delete_folder():
    path_ = input("input path to delete: ")
    l_5_easy.delete_script(path_)

def create_folder():
    path_ = input("input path to create: ")
    l_5_easy.create_script(path_)

def the_and():
    l_5_easy.the_and()
def print_menu(menu):
    for i, key in enumerate(menu, start=1):
        print(f'{i}. {key}')
def get_command(limit):
    command = int(input("input command: "))
    if 1 <= command <=limit:
        return command

menu = {
    "goto folder": goto_folder,
    "view folder": view_folder,
    "delete folder": delete_folder,
    "create folder": create_folder,
    "quit": the_and,
}

while True:
    print_menu(menu)
    command = get_command(len(menu))
    if command is not None:
        key = list(menu.keys())[command - 1]
        menu[key]()
    else:
        print('Wrong command!')