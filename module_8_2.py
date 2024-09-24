def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {number}')
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        return result[0] / (len(numbers) - result[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')