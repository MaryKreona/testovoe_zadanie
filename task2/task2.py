import sys
import math

def calculate_position(x, y, center_x, center_y, radius):
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    if abs(distance - radius) <= 1e-9:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Ошибка: неверное количество аргументов.")


    with open(sys.argv[1], 'r') as file1:
        lines = file1.read().splitlines()
        center_x, center_y = map(float, lines[0].strip().split())
        radius = float(lines[1].strip())


    with open(sys.argv[2], 'r') as file2:
        points = file2.read().splitlines()
        for point in points:
            x, y = map(float, point.strip().split())
            position = calculate_position(x, y, center_x, center_y, radius)
            print(position)


main()