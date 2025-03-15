import sys
import math

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline())
    return (x, y, radius)

def read_points(file_path):
    with open(file_path, 'r') as file:
        points = [tuple(map(float, line.split())) for line in file]
    return points

def point_position(circle, point):
    x_c, y_c, radius = circle
    x_p, y_p = point
    distance_squared = (x_p - x_c)**2 + (y_p - y_c)**2
    radius_squared = radius**2

    if math.isclose(distance_squared, radius_squared, rel_tol=1e-9):
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <circle_file> <points_file>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle = read_circle_data(circle_file)
    points = read_points(points_file)

    for point in points:
        position = point_position(circle, point)
        print(position)

if __name__ == "__main__":
    main()