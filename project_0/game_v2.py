"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def half_division_predict(number: int = 1) -> int:
    """Угадываем (на самом деле подбираем) число методом половинного деления

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    left_limit = 1
    right_limit = 101

    while True:
        count += 1
        predict_number = (left_limit + right_limit) // 2 # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            left_limit = predict_number # сдвигаем левую границу интервала
        else:
            right_limit = predict_number # сдвигаем правую границу интервала
    return count


def random_with_comparison_predict(number: int = 1) -> int:
    """Рандомно угадываем число, уменшая интервал для выбора случайного числа,
    в зависимости от того больше или меньше предполагаемое число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    left_limit = 1
    right_limit = 101

    while True:
        count += 1
        predict_number = np.random.randint(left_limit, right_limit)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            left_limit = predict_number # сдвигаем левую границу интервала
        else:
            right_limit = predict_number # сдвигаем правую границу интервала
    return count


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(random_with_comparison_predict)
    score_game(half_division_predict)