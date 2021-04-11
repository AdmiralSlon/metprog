import copy
from datetime import datetime
from employee_class import CompanyEmployee
import random
from gendata import gen_data
from sorts import merge_sort, heap_sort, bubble_sort

data_size = [100, 200, 500, 1000, 5000, 10000, 15000, 25000, 50000, 100000]

for size in data_size:
    data_emp = []
    gen_data(size)  # создаем файл с данными нужного размера
    with open(f'./database/emp_data_{size}.txt', mode='r', encoding='UTF-8') as database:
        for one_data in database:
            data_emp.append(CompanyEmployee(one_data.strip()))  # переносим данные из файла в массив

# копируем массив в 3 других, с которыми будем работать

    data_bubble_sort = copy.deepcopy(data_emp)
    data_heap_sort = copy.deepcopy(data_emp)
    data_merge_sort = copy.deepcopy(data_emp)

    start1 = datetime.now()
    # bubble_sort(data_bubble_sort)  # сортируем пузырьком
    end1 = datetime.now()

    start2 = datetime.now()
    heap_sort(data_heap_sort)  # сортируем кучей
    end2 = datetime.now()

    start3 = datetime.now()
    merge_sort(data_merge_sort)  # сортируем слиянием
    end3 = datetime.now()
    with open('./results/res_time.txt', mode='a', encoding='UTF-8') as result:
        result.write(f"size: {size} bubble sort: {str(end1 - start1)}" + '\n' +
                     f"size: {size} heap sort: {str(end2 - start2)}" + '\n' +
                     f"size: {size} merge sort: {str(end3 - start3)}" + '\n')  # записываем время работы