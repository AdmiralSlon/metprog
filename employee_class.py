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

    def __gt__(self, other):  # перегрузка '>'
        if self.department > other.department:
            return True
        elif self.department == other.department:
            if self.fio > other.fio:
                return True
            elif self.fio == other.fio:
                if self.date > other.date:
                    return True
                elif self.date == other.date:
                    if self.position > other.position:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __lt__(self, other):  # перегрузка '<'
        if self.department < other.department:
            return True
        elif self.department == other.department:
            if self.fio < other.fio:
                return True
            elif self.fio == other.fio:
                if self.date < other.date:
                    return True
                elif self.date == other.date:
                    if self.position < other.position:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ge__(self, other):  # перегрузка '>='
        if self.department > other.department:
            return True
        elif self.department == other.department:
            if self.fio > other.fio:
                return True
            elif self.fio == other.fio:
                if self.date > other.date:
                    return True
                elif self.date == other.date:
                    if self.position > other.position:
                        return True
                    elif self.position == other.position:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __le__(self, other):  # перегрузка '<='
        if self.department < other.department:
            return True
        elif self.department == other.department:
            if self.fio < other.fio:
                return True
            elif self.fio == other.fio:
                if self.date < other.date:
                    return True
                elif self.date == other.date:
                    if self.position < other.position:
                        return True
                    elif self.position == other.position:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
