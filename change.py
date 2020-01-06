# Uses python3

def get_change(m):
    tens = m//10
    m = m%10

    fives = m//5
    m = m%5

    return m + fives + tens

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
