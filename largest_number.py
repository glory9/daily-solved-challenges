#Uses python3
import sys

def largest_number(a):
    res, c, dic = "", [], {}
    
    a = sorted(a, reverse = True)

    for i in a:
        if i in dic:
            dic[i].append(i)
        else:
            dic[i] = [i]
            c.append(i)

    prev = c[0]

    for number in range(1, len(c)):

        first = int(prev + c[number])
        second = int(c[number] + prev)

        if first > second:
            f = "".join(dic[prev])
            res += f
            prev = c[number]

        elif second > first:
            f = "".join(dic[c[number]])
            res += f

        else:
            f = "".join(dic[prev])
            res += f
            prev = c[number] 

    s = "".join(dic[prev])
    res += s

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

'''
print('\ndic', dic, '\n')
print('number is', number, 'res is', res, '\n')
print(first, second)
print('dic[prev]', dic[prev])
print('Yes!', dic[c[number]])
print(res)
'''