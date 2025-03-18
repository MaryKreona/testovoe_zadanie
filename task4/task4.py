import sys


def read_from_file(filename):
    with open(filename, 'r') as file:
        return list(map(int, file.read().split()))


def min_moves(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 1:
        median = sorted_nums[n // 2]
    else:
        median = sorted_nums[(n // 2) - 1]
    moves = sum(abs(num - median) for num in nums)
    return moves


arr = sys.argv[1]
nums = read_from_file(arr)
result = min_moves(nums)
print(result)
