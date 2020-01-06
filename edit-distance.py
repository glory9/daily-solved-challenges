# edit distance is a concept that attempts to measure how much work
# is required to make one string an exact copy of the other.


def edit_distance(s, t):

    s = [letter for letter in s]
    t = [l for l in t]

    d = []

    l_s, l_t = len(s) + 1, len(t) + 1

    for j in range(l_s):
        d.append([0] * (l_t))

    for k in range(l_t):
        d[0][k] = k

    for m in range(l_s):
        d[m][0] = m

    for q in range(1, l_t):
        for p in range(1, l_s):
            ins = d[p][q - 1] + 1
            delet = d[p - 1][q] + 1

            dist = min(ins, delet)

            match = d[p - 1][q - 1]

            if s[p - 1] == t[q - 1]:
                d[p][q] = min(dist, match)

            else:
                d[p][q] = min(dist, match + 1)

    return d[p][q]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
