import sys


def calculate_position(x, y, center_x, center_y, radius):
    distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
    if abs(distance - radius) <= 1e-9:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def main():
    with open(sys.argv[1], 'r') as file1:
        lines = file1.readlines()
        center_x, center_y = map(float, lines[0].split())
        radius = float(lines[1])

    with open(sys.argv[2], 'r') as file2:
        points = file2.readlines()
        for point in points:
            x, y = map(float, point.split())
            position = calculate_position(x, y, center_x, center_y, radius)
            print(position)


main()
