def find_path(n, m):
    # Создаем массив от 1 до n
    array = list(range(1, n + 1))
    # Создаем пустой список
    path = []
    # Начинаем с первого элемента
    current = 0

    while True:
        # Добавляем текущий элемент в путь
        path.append(array[current])
        # Вычисляем следующий элемент, двигаясь на m шагов
        current = (current + m - 1) % n
        # Если вернулись к первому элементу, завершаем цикл
        if current == 0:
            break

    return path


# Пример использования
n, m = map(int, input().split())
print(*find_path(n, m))
