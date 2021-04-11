import random

data_objects = ['mname', 'wname', 'msurname', 'wsurname', 'mpatronymic',
                'wpatronymic', 'department', 'position', 'date']

data_mname, data_wname, data_msurname, data_wsurname, data_mpatronymic, data_wpatronymic, data_department, \
            data_position, data_date = [], [], [], [], [], [], [], [], []

empty_data = [data_mname, data_wname, data_msurname, data_wsurname, data_mpatronymic, data_wpatronymic, data_department,
              data_position, data_date]

for one_data_object in range(len(data_objects)):
    with open(f'./mass/{data_objects[one_data_object]}.txt', mode='r', encoding='UTF-8') as database:
        for one_data in database:
            empty_data[one_data_object].append(one_data.strip())  # считываем данные для групп


def gen_data(size):
    res = []
    for i in range(size):
        employee = ''
        if random.randint(0, 1) == 0:
            employee += data_msurname[random.randint(0, len(data_msurname) - 1)] + ' '
            employee += data_mname[random.randint(0, len(data_mname) - 1)] + ' '
            employee += data_mpatronymic[random.randint(0, len(data_mpatronymic) - 1)] + ', '
        else:
            employee += data_wsurname[random.randint(0, len(data_wsurname) - 1)] + ' '
            employee += data_wname[random.randint(0, len(data_wname) - 1)] + ' '
            employee += data_wpatronymic[random.randint(0, len(data_wpatronymic) - 1)] + ', '
        employee += data_department[random.randint(0, len(data_department) - 1)] + ', '
        employee += data_position[random.randint(0, len(data_position) - 1)] + ', '
        employee += data_date[random.randint(0, len(data_date) - 1)]
        res.append(employee)
    with open(f'./database/emp_data_{size}.txt', mode='w', encoding='UTF-8') as employee_result:
        for one_employee in res:
            employee_result.write(f"{one_employee}" + '\n')  # записываемодин элемент в файл
