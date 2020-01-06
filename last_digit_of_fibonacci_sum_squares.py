# find the last digit of the nth sum of squares 
# till the nth fibonacci number

# solution uses greedy approach

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    arr = []
    arr.append(0)
    arr.append(1)
    
    for j in range(2, 60):
        arr.append((arr[j - 1] + arr[j - 2])%10)
    
    for k in range(1,60):
        krr = arr[k] * arr[k]
        arr[k] = krr%10 + arr[k-1]
    
    return arr[n%60]%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
