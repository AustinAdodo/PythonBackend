import textwrap


# from itertools import accumulate

# for i in range(1, n + 1):
# print(i, end='')
def triangle_solution():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(l)
    # s = "qbcde"
    # a = s.__len__()
    # arr = {1, 2, 3, 5, 6}


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


def convert_roman(*numbers):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    ans = []
    j = 12
    str1 = ""
    div = 0
    for number in numbers:
        while number > 0:
            # get symbol occurrences (integer floor division)
            div = number // num[j]
            # and the remainder after they are handled
            number = number % num[j]
            # handle occurrences of the symbol
        while div > 0:
            str1 += sym[j]
            div -= 1
            j -= 1
    ans.append(str1)
    return ans


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    # We store the number of factors in this variable
    factors = 0
    # This will loop from 1 to n
    for i in range(1, n + 1):
        # Check if `i` divides `n`, if yes then we increment the factors
        if n % i == 0:
            factors += 1
    # If total factors are exactly 2
    if factors == 2:
        return True
    return False


def is_prime2(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False
    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i * i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True
# test
# for x in xrange(1, 11):
# print '%d: %s' % (x, is_prime(x))
