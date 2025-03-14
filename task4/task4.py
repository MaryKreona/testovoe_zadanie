import sys


# Функция для чтения массива из файла
def read_array_from_file(filename):
    with open(filename, 'r') as file:
        return list(map(int, file.read().split()))


# Основная функция
def min_moves_to_equalize(nums):
    # Сортируем массив
    sorted_nums = sorted(nums)

    # Находим медиану
    n = len(sorted_nums)
    if n % 2 == 1:
        median = sorted_nums[n // 2]
    else:
        # В случае четного количества элементов выбираем любой из двух средних значений
        median = sorted_nums[(n // 2) - 1]

    # Вычисляем сумму разниц до медианы
    total_moves = sum(abs(num - median) for num in nums)

    return total_moves


if __name__ == "__main__":
    # Получение имени файла из командной строки
    filename = sys.argv[1]
    # Чтение массива из файла
    nums = read_array_from_file(filename)

    # Вычисление минимального количества ходов
    result = min_moves_to_equalize(nums)

    print(f"Минимальное количество ходов: {result}")

