def find_path(n, m):
    arr = list(range(1, n + 1))
    path = []
    current = 0

    while True:
        path.append(arr[current])
        current = (current + m - 1) % n
        if current == 0:
            break
    return path


n, m = map(int, input().split())
print(*find_path(n, m))
