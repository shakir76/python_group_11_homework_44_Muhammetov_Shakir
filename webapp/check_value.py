class ErrorValueRange(Exception):
    pass


class ErrorValueSet(Exception):
    pass


class ErrorValueDeficiency(Exception):
    pass


class Check:
    @staticmethod
    def check_values(value):
        for i in value:
            if i not in range(1, 9 + 1):
                raise ErrorValueRange()
            return value

    @staticmethod
    def check_int(value):
        a = value.split()
        b = []
        for i in a:
            b.append(int(i))
        return b

    @staticmethod
    def check_set(value):
        set_value = set(value)
        if len(value) == len(set_value):
            return value
        else:
            raise ErrorValueSet()

    @staticmethod
    def check_num(value, secret_nums):
        count = 0
        for i in value:
            if i > 0:
                count += 1
        if count > len(secret_nums) or count < len(secret_nums):
            raise ErrorValueDeficiency()

    @staticmethod
    def sum_bulls(value, secret_nums):
        cont = 0
        cont2 = 0
        for id_num, val in enumerate(secret_nums):
            for x, y in enumerate(value):
                if id_num == x and y == val:
                    cont += 1
                elif y == val:
                    cont2 += 1
        return cont, cont2
