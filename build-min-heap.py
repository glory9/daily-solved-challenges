# implement-heap-using-an-array


def build_heap(data):
    swaps = []

    for i in range(len(data)//2 + 1, -1, -1):
        size = len(data)
        j = (2 * i) + 1

        while j < size:

            if j + 1 < size:
                if data[j] > data[j + 1]:
                   j += 1
            
            if data[i] > data[j]:

                swaps.append((i,j))
                data[i], data[j] = data[j], data[i]
                i  = j
                j = (2 * i) + 1
            
            else:
                break

    return swaps



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()


