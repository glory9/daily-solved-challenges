# Uses python3
import sys

def gcd_naive(a, b):
    
    rem = a%b
    a = b

    while rem != 0:
        temp = rem
        rem = a%rem
        a = temp
        
    return a

if __name__ == "__main__":
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
