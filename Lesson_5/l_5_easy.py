

__author__ = 'Ильясов Исмаил Ильясович'

# EASY
import os
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def create_script(path_='.'):
        try:
            os.mkdir(path_)
            print ("folder dir_" + path_ + " is created")
        except:
            print ("folder dir_" + path_ + " is not created")

# for fol in range(1,10):
#     create_script(str('dir_' + str(fol)))

def delete_script(path_='.'):
        try:
            os.rmdir(path_)
            print("folder " + path_ + " is deleted")
        except:
            print("folder " + path_ + " is not deleted")
def the_and():
    exit()

# for fol in range(1,10):
#     delete_script(str('dir_' + str(fol)))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def in_folder(path_ = '.'):
    try:
        for file in os.listdir():
            # if not os.path.isfile(os.path.join(path_, file)):
            print(file)

    except:
        print("folder not found")


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_itself():
    try:
        shutil.copy(__file__,__file__ + '.backup')
        print('created backup files: ' +__file__+ '.backup')
    except:
        print('backup files not created ')


