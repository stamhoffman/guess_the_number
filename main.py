import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Угадывает загаданное число методом бинарного поиска.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток, потребовавшихся для нахождения числа.
    """
    # Создаём отсортированный массив от 1 до 100
    arr = list(range(1, 101))

    # Инициализируем границы поиска и счётчик попыток
    left, right = 0, len(arr) - 1
    count = 0

    # Бинарный поиск
    while left <= right:
        mid = left + (right - left) // 2  # Серединный индекс
        count += 1  # Учитываем текущее сравнение

        if arr[mid] == number:
            return count  # Число найдено, возвращаем количество попыток
        if arr[mid] < number:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине

    return count  # Число не найдено (хотя в данном диапазоне это невозможно)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

# Пример использования
if __name__ == '__main__':
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)
