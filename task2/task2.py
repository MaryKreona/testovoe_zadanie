with open('circle.txt', 'r') as file:
    lines = file.read().splitlines()
    center_x, center_y = map(float, lines[0].strip().split())
    radius = float(lines[1].strip())

points = []
with open('dot.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.strip().split())
        points.append((x, y))


def calculate_position(cent_x, cent_y, rads, point_x, point_y):
    distance_squared = (point_x - cent_x)**2 + (point_y - cent_y)**2
    if abs(distance_squared - rads**2) < 1e-9:
        return 0
    elif distance_squared < rads**2:
        return 1
    else:
        return 2


for x, y in points:
    position = calculate_position(center_x, center_y, radius, x, y)
    print(position)
