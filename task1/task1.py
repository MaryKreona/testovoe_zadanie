def find_path(num_arr, step):
    arr = list(range(1, num_arr + 1))
    path = []
    current = 0

    while True:
        path.append(arr[current])
        current = (current + step - 1) % num_arr
        if current == 0:
            break
    return path


n, m = map(int, input().split())
print(*find_path(n, m))
