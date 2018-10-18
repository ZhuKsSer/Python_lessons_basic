# EASY
# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
 a = [1,2,3]
b = a
 def get_square(arr):
    new_arr = arr.copy()
    
    for idx, itm in enumerate(arr):
        new_arr[idx] = itm ** 2
    
    return new_arr
 c = get_square(a)
 print(a,c)
 # Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
 lst1 = ['яблоко', 'апельсин', 'киви']
lst2 = ['киви', 'груша', 'яблоко']
 def overal(lst1, lst2):
    result = [x for x in lst1 if x in lst2]
    return result
  
a = overal(list(lst1), list(lst2))
print(lst1, lst2, '\n', '\nСписок фруктов, присутствующих в обоих списках: ', a)
 # Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
 import numpy as np
 lst = np.random.randint(-10, 10, 10)
#lst = [-1,0,6,-2,3,4,18, 9, 5,6,7,-8,9]
b = lst
 def multiplicity(lst):
    #new_lst = []
    new_list = [el for el in lst if el % 3 == 0 and el >=0 and el % 4 !=0]
    return new_list
    print(new_list)
            
c = multiplicity(lst)
print(lst, '\n', c)
 #NORMAL
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
 # Решение с re
 import re
 string = 'mtMmEZUOmcq'
print(re.findall(r'[a-z]+', string)) 
 # Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
 # Решение с re
import re
 string = 'GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'
print(re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', string))
