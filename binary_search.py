# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    while left < right:        
        mid = (left + right)//2

        if a[mid] == x:
            return mid

        if a[mid] < x:
            left = mid + 1

        else:
            right = mid

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = " ")

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a = a[1:]
# b = b[1:]
# for index in b:
#     print(binary_search(a,index))