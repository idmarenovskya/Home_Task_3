def read_from_file(path):
    with open(path, 'r') as f:
        data = f.read()

    data = data.split()
    data = list(map(int, data))
    return data


def find_min(list_of_numbers):
    if type(list_of_numbers) is not list:
        raise TypeError
    if len(list_of_numbers) == 0:
        return None
    _min = float('inf')
    for i in list_of_numbers:
        if i < _min:
            _min = i
    return _min


def find_max(list_of_numbers):
    if type(list_of_numbers) is not list:
        raise TypeError
    if len(list_of_numbers) == 0:
        return None
    _max = -float('inf')
    for i in list_of_numbers:
        if i > _max:
            _max = i
    return _max


def calc_sum(list_of_numbers):
    if type(list_of_numbers) is not list:
        raise TypeError
    _sum = 0
    for i in list_of_numbers:
        _sum += i
    return _sum


def calc_mult(list_of_numbers):
    if type(list_of_numbers) is not list:
        raise TypeError
    if len(list_of_numbers) == 0:
        return 0
    mult = 1
    try:
        for i in list_of_numbers:
            mult *= i
        return mult
    except OverflowError:
        return float('inf')


if __name__ == "__main__":
    print('Введите путь к файлу с данными')
    path = input()
    data = read_from_file(path)
    _min = find_min(data)
    _max = find_max(data)
    _sum = calc_sum(data)
    mult = calc_mult(data)
    print('Минимальное', _min)
    print('Максимальное', _max)
    print('Сумма', _sum)
    print('Произведение', mult)
