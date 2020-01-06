# Uses python3
import sys

class Number:
    def __init__(self, moves=None, states=None):
        self.moves = moves
        self.states = states


def optimal_sequence(n):
    min_moves = [0]

    min_moves.append(Number(0,[1]))
    min_moves.append(Number(1,[1,2]))
    min_moves.append(Number(1,[1,3]))

    if n <=3:
        return min_moves[n]

    for num in range(4, n + 1):
        thr, two, idx_3, idx_2, idx_1 = n + 1, n + 1, num//3, num//2, num - 1

        if num%3 == 0:
            thr = min_moves[idx_3].moves + 1

        if num%2 == 0:
            two = min_moves[idx_2].moves + 1

        one = min_moves[idx_1].moves + 1

        key, moves = idx_3, thr

        if moves > two:
            key, moves = idx_2, two
        
        if moves > one:
            key, moves = idx_1, one

        optimal_idx_states = [ i for i in min_moves[key].states]
        optimal_idx_states.append(num)
        min_moves.append(Number(moves,optimal_idx_states))
        

    return min_moves[n]


# input = sys.stdin.read()
# n = int(input)
# assert n >= 1

# res  = optimal_sequence(n)
# print(res.moves)
# for x in res.states:
#     print(x, end=' ')


# ------> Debug driver code <-------- #

n = int(input("??:  "))
res  = optimal_sequence(n)
print(res.moves)
for x in res.states:
    print(x, end=" ")





# ----> Starter code that was replaced <---- #

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)