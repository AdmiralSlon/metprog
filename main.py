import random
from time import time, sleep
from gendata import gen_data
from finds import *
from collections import defaultdict

data_size = [10000, 20000, 50000, 100000, 150000, 250000, 500000, 800000, 1000000]

# md = defaultdict(list)
# md[1].append("zxc1")
# md[1].append("zxc2")
# md[2].append("zxc3")
# print(md[1])
# for i in md[1]:
#     print(i)

for size in data_size:
    data_emp = []
    data_multimap_emp = []
    # gen_data(size)  # создаем файл с данными нужного размера
    with open(f'./database/emp_data_{size}.txt', mode='r', encoding='UTF-8') as database:
        for one_data in database:
            data_multimap_emp.append(one_data.strip())
            data_emp.append(CompanyEmployee(one_data.strip()))  # переносим данные из файла в массив
    key = "Бурова Авдотья Андреевна"

    md = defaultdict(list)
    j = 0
    for i in data_emp:
        md[i.fio].append(data_multimap_emp[j])
        j += 1


    start = time()
    simple_find(data_emp, key)
    sleep(0.001)
    end = time()
    time_simple_find = str(end - start - 0.001)

    start = time()
    merge_sort(data_emp)
    binary_find(data_emp, key)
    sleep(0.001)
    end = time()
    time_binary_find = str(end - start - 0.001)

    data_multimap = MultimapEmployee(data_emp)
    start = time()
    data_multimap.find(key)
    sleep(0.001)
    end = time()
    time_multimap = str(end - start - 0.001)

    start = time()
    binary_find(data_emp, key)
    sleep(0.001)
    end = time()
    time_binary_find_after_sort = str(end - start - 0.001)

    # start = time()
    # zxc = md[key]
    # sleep(0.001)
    # end = time()
    # time_multimap = str(end - start - 0.001)

    # start = time()
    # sleep(0.001)
    # end = time()
    # timezxc = str(end - start - 0.001)
    # print(timezxc)

    print("size = " + str(size))
    print("время прямого поиска = " + time_simple_find)
    print("время сортировки массива слиянием и бинарный поиск в нем = " + time_binary_find)
    print("время бинарного поиска для заранее отсортированного массива = " + time_binary_find_after_sort)
    print("время поиска в multimap = " + time_multimap)

    # with open('./results/res_time_find.txt', mode='a', encoding='UTF-8') as result:
    #     result.write(
    #         f"size = {size} " + '\n'
    #         + "время прямого поиска = " + time_simple_find + '\n'
    #         + "время сортировки массива слиянием и бинарный поиск в нем = " + time_binary_find + '\n'
    #         + "время бинарного поиска в заранее отсортированном массиве = " + time_binary_find_after_sort + '\n'
    #         + "время поиска в multimap = " + time_multimap + '\n')
    with open('./results/res_time_find.txt', mode='a', encoding='UTF-8') as result:
        result.write(
            f"size = {size} " + '\n'
            + time_simple_find + '\n'
            + time_binary_find + '\n'
            + time_binary_find_after_sort + '\n'
            + time_multimap + '\n')
