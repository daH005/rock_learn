def function(command, array):
    command = command.replace('Получить элемент по ', 'get-')
    command = command.replace('Получить элементы с ', 'get_many-')
    command = command.replace('Получить ', 'get_from_end-')

    command = command.replace(' индексу', '')
    command = command.replace(' по ', '-')
    command = command.replace(' с шагом ', '-')
    command = command.replace(' элемент с конца массива', '')

    elements = command.split('-')

    if 'get' in elements:
        n = int(elements[1])
        return array[n]

    elif 'get_many' in elements:
        a, b, v = map(int, elements[1:])
        result = []
        for i in range(a, b, v):
            result.append(array[i])
        return result

    elif 'get_from_end' in elements:
        n = -int(elements[1])
        return array[n]

    else:
        print('Некорректная команда!')


if __name__ == '__main__':
    array = [1, 3, 5, 7, 9, 11]

    print(function('Получить элемент по 2 индексу', array))
    print(function('Получить элементы с 0 по 6 с шагом 2', array))
    print(function('Получить 3 элемент с конца массива', array))
    print(function('Ошибочная команда', array))
