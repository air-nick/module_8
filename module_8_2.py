# Функция для подсчёта суммы чисел в коллекции
def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            # Пытаемся добавить число, если это не число, будет исключение
            result += item
        except TypeError:
            # Если ошибка, увеличиваем счётчик некорректных данных
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {item}")

    return result, incorrect_data


# Функция для подсчёта среднего арифметического
def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией (например, списком или кортежем)
        if not isinstance(numbers, (list, tuple)):
            raise TypeError

        # Получаем сумму и количество некорректных данных
        total, incorrect_data = personal_sum(numbers)

        # Если коллекция пустая, обработаем исключение ZeroDivisionError
        if len(numbers) == 0:
            return 0

        # Возвращаем среднее значение
        return total / (len(numbers) - incorrect_data)

    except ZeroDivisionError:
        # Если деление на ноль, возвращаем 0
        return 0
    except TypeError:
        # Если передан некорректный тип данных, выводим сообщение и возвращаем None
        print("В numbers записан некорректный тип данных")
        return None


# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
