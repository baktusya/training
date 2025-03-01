def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {num}")
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        if not isinstance(numbers, (str, list, tuple, set)):
            print('В numbers записан некорректный тип данных')
            return None

        total_sum, incorrect_data = personal_sum(numbers)
        correct_data_count = len(numbers) - incorrect_data
        average = total_sum / correct_data_count

    except ZeroDivisionError:
        return 0

    except TypeError as exc:
        print(exc)
        return None

    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать