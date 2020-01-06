# last digit of nth fibonacci number

import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    arr = []
    arr.append(0)
    arr.append(1)
    
    for j in range(2, 60):
        arr.append((arr[j - 1] + arr[j - 2])%14)
    print(arr)
    return arr[n%60]

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
