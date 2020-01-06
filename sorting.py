# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j, k = l, l
    
    for i in range(l,r+1):
        if a[i] < x:
            j += 1
            k = j
            a[j], a[i] = a[i], a[j]
            break
    
    g = j
    for y in range(g + 1, r + 1):
        
        if a[y] == x:
            k += 1
            a[k], a[y] = a[y], a[k]

        elif a[y] < x:
            k += 1
            a[k], a[y] = a[y], a[k]

            j += 1
            a[j], a[k] = a[k], a[j]

    
    a[l], a[j] = a[j], a[l]
    
    return j,k
    


def partition2(a, l, r):
    x = a[l]
    j = l 
    for i in range(l + 1, r + 1):
        
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]    
    
    a[l], a[j] = a[j], a[l]

    print(a)
    
    return j

def randomized_quick_sort(a, l, r):
    
    if l >= r:
        return
    k = random.randint(l, r)
    
    a[l], a[k] = a[k], a[l]
    
    p,q = partition3(a, l, r)

    randomized_quick_sort(a, l, p - 1)
    randomized_quick_sort(a, q + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

# tests = [[6, 2, 7, 5, 4, 3, 8, 1], [2, 9, 2, 2, 9, 2, 7, 2], [9, 7, 4, 7, 8, 3, 8, 7]]

# for a in tests:
#     result = sorted(a)
#     randomized_quick_sort(a,0,7)
#     assert a == result, "Sorry Dude, there's another bug"

# print("\nWe made it baby!!!!!!\n\n")