
__author__ = 'Ильясов Исмаил Ильясович'

# HARD
# Задание-1
#
# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить

import os

def unpack():
    base_dir = r"C:\Users\Andrey\Downloads"
    files = os.listdir(base_dir)
    dirs = os.listdir(base_dir)
    for file in os.listdir(base_dir):
        if not os.path.isfile(os.path.join(base_dir, file)):
            for file1 in os.listdir(base_dir + '\\' + file):
                # print(file1)
                os.rename(base_dir + '\\' + file + '\\'+ file1, base_dir + '\\' + file1)
            os.rmdir(base_dir + '\\' + file)

def pack():
    BASE_DIR = r"C:\Users\Andrey\Downloads"
    files = os.listdir(BASE_DIR)

    extensions = set([os.path.splitext(file)[1] for file in files
                      if os.path.isfile(os.path.join(BASE_DIR, file))])

    for ext in extensions:
        if not os.path.exists(os.path.join(BASE_DIR, ext)):
            os.mkdir(os.path.join(BASE_DIR, ext))

    # for ext in extensions:
    #     for file in files:
    #         if file.endswith(ext):
    #             os.rename(os.path.join(BASE_DIR, file), os.path.join(BASE_DIR, ext, file))

    for file in files:
        if os.path.isfile(os.path.join(BASE_DIR, file)):
            ext = os.path.splitext(file)[1]
            os.rename(os.path.join(BASE_DIR, file), os.path.join(BASE_DIR, ext, file))
def the_and():
    exit()

def print_menu(menu):
    for i, key in enumerate(menu, start=1):
        print(f'{i}. {key}')
def get_command(limit):
    command = int(input("input command: "))
    if 1 <= command <=limit:
        return command

menu = {
    "pack": pack,
    "unpack": unpack,
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