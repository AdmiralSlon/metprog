class CompanyEmployee:  # класс сотрудник
    fio: str
    department: str
    position: str
    date: str

    def __init__(self, line: str):  # инициализация
        fio, department, position, date = line.split(', ')
        self.fio = fio
        self.department = department
        self.position = position
        self.date = date

    def __lt__(self, other):  # Перегрузка оперптора <
        if isinstance(other, str):
            if self.fio < other:
                return True
            else:
                return False
        else:
            if self.fio < other.fio:
                return True
            else:
                return False

    def __le__(self, other):  # Перегрузка оператора <=
        if isinstance(other, str):
            if self.fio <= other:
                return True
            else:
                return False
        else:
            if self.fio <= other.fio:
                return True
            else:
                return False

    def __gt__(self, other):  # Перегрузка оператора >
        if isinstance(other, str):
            if self.fio > other:
                return True
            else:
                return False
        else:
            if self.fio > other.fio:
                return True
            else:
                return False

    def __ge__(self, other):  # Перегрузка оператора >=
        if isinstance(other, str):
            if self.fio >= other:
                return True
            else:
                return False
        else:
            if self.fio >= other.fio:
                return True
            else:
                return False

    def __eq__(self, other):  # Перегрузка оператора ==
        if isinstance(other, str):
            if self.fio == other:
                return True
            else:
                return False
        else:
            if self.fio == other:
                return True
            else:
                return False


def merge_sort(array):  # слиянием
    if len(array) >= 2:
        middle = int(len(array) / 2)
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1
        return array
    return array


def simple_find(array, find_key):
    res = 0
    for i in range(len(array)):
        if array[i].fio == find_key:
            res = i
            break
    return res


def binary_find(array, find_key):
    md = len(array) // 2
    mn = 0
    mx = len(array) - 1

    while array[md].fio != find_key and mn <= mx:
        if array[md].fio < find_key:
            mn = md + 1
        else:
            mx = md - 1
        md = (mn + mx) // 2
    if mn <= mx:
        return md
    else:
        return 'элемент не найден'


class MultimapEmployee:
    key: list
    value: list

    def __init__(self, array):  # инициализация
        self.key = []
        self.value = []

        for employee in array:
            self.key.append(employee.fio)
            self.value.append(employee)

    def insert(self, employee):
        self.key.insert(self.find(employee.fio), employee.fio)
        self.value.insert(self.find(employee), employee)

    def find(self, find_key):
        md = len(self.key) // 2
        mn = 0
        mx = len(self.key) - 1

        while self.key[md] != find_key and mn <= mx:
            if self.key[md] < find_key:
                mn = md + 1
            else:
                mx = md - 1
            md = (mn + mx) // 2
        if mn <= mx:
            return md
        else:
            return 'элемент не найден'
