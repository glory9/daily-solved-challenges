# python3



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




# n = open("week2_priority_queues_and_disjoint_sets\\1_make_heap\\tests\\04")
# n = list(map(int, n.read().split()))
# assert len(n) - 1 == n[0]

# n = n[1:]

# a = open("week2_priority_queues_and_disjoint_sets\\1_make_heap\\tests\\04.a")

# ans = buildHeap(n)

# print(len(ans), "\n\n")
# hh = 0
# for i in range(25006):
#     hh = i

#     h = a.readline()

#     if hh in range(1, 11):
#         print(h.strip(), ans[hh -1], "\n")

#     if hh == 10:
#         print("----------b-r-e-a-k---------\n\n\n")

#     if hh > 24996:
#         print(h.strip(), ans[hh -1], "\n")