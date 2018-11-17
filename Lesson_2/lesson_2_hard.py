
__author__ = 'Ильясов Исмаил Ильясович'


# Hard
#
# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?
# import re

def hard_1():
    txt = input("input text: ")
    print('Всего букв:', len(txt)) # punkt 1
    i = 0
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','k','r','s','t','u','v','w','x','y','z')
    latin = 0
    ii = 0
    word = 0
    while i < len(txt):
        word = txt[i]
        ii = 0
        while ii < len(alphabet):
            if alphabet[ii] == word.lower():
                latin +=1
                # print('iiiiff',ii, word, alphabet[ii], i)
            ii +=1
        i += 1
    # print (i)
    print('Латинских букв:', latin)

# hard_1()

#
# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра
def del_dupl_words(l):
    n = []
    for i in l.split():
        if i not in n:
            n.append(i)
    return n
def hard_2():
    txt_1 = input("Введите текст: ")
    txt_2 = input("Введите другой текст: ")
    # txt_1 = txt_1.split()
    txt_1 = del_dupl_words(txt_1)
    txt_2 = txt_2.split()
    i = 0
    samewords = ''
    while i < len(txt_1):
        ii = 0
        while ii < len(txt_2):
            # print(txt_1[i], txt_2[ii])
            if txt_1[i].lower() == txt_2[ii].lower():
                samewords = samewords + ", " + txt_2[ii]
                ii = len(txt_2)
                # print(txt_2[ii], samewords)
            ii += 1
        i += 1
    print("Слова присутствующие в обоих текстах:", samewords)


# hard_2()

answer = ''
while answer.lower() != 'n':
    # print('rrrr')
    answer = input("Потестим задачи? (Y/N)")
    if answer.lower() =='y':
        print("OK, выберите задачу для запуска")
        print("[1] - первая задача hard из второго урока")
        print("[2] - вторая задача hard из второго урока")

        do = int(input("Укажите номер задачи: "))

        if do == 1:
            hard_1()
        elif do == 2:
            hard_2()
        else:
            print("Пожалуйста, выберите 1 или 2!")