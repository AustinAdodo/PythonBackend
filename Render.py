import textwrap

n = 20
for i in range(1, n + 1):
    print(i, end='')
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(l)
s = "qbcde"
a = s.__len__()
arr = {1, 2, 3, 5, 6}


# arr = list(set(arr))#
# def wrap(string, max_width): return textwrap.fill(string,max_width)#
# print(f"Hello {first_name} {last_name}! You just delved into python.")#
def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    if year % 100 != 0 and year % 4 == 0:
        leap = True
    return leap


def minion_game(string):
    inp_str = string
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    len_str = len(inp_str)
    total_poss_score = int((len_str * (len_str + 1)) / 2)

    for i in range(len_str):
        if inp_str[i] in vowels:
            kevin_score += len_str - i
            stuart_score = total_poss_score - kevin_score

    if stuart_score > kevin_score:
        print('Stuart', stuart_score)

        if kevin_score == 0:
            print('Stuart', total_poss_score)

    elif kevin_score > stuart_score:
        print('Kevin', kevin_score)
    else:
        print('Draw')
    return


def split_and_join(line):
    return "-".join(line.split())


def merge_the_tools(string, k):
    li = textwrap.wrap(string, k)
    for i in li:
        print(''.join(sorted(set(i), key=i.index)))
