from functools import reduce


def coded_task_01(a, b):
    return list(set(a + b))


def coded_task_02(s):
    return s.count('a')


def coded_task_03(num):
    while (num % 3 == 0):
        num /= 3
    return num == 1


def coded_task_04(num):
    digits_list = lambda num: [int(x) for x in str(num)]
    res = sum(digits_list(num))
    while res >= 10:
        res = sum(digits_list(res))
    return res


def coded_task_05(input_list):
    return [x for x in input_list if x != 0] + [x for x in input_list if x == 0]


def coded_task_06(input_list):
    if len(input_list) <= 2:
        return True

    for i, k in enumerate(range(len(input_list) - 2)):
        d1 = input_list[i + 1] - input_list[i]
        d2 = input_list[i + 2] - input_list[i + 1]
        if d1 != d2:
            return False

    return True


def coded_task_07(input_list):
    res_list = [[y for y in input_list if y == x] for x in input_list]
    return [f for f in res_list if len(f) == 1][0][0]


def coded_task_08(input_list):
    complete_list = list(range(min(input_list), max(input_list)))
    return [x for x in complete_list if x not in input_list][0]


def coded_task_09(input_list):
    aux_list = [type(val) for idx, val in enumerate(input_list)]
    if (tuple in aux_list) and (aux_list.index(tuple) >= 1):
        return input_list[aux_list.index(tuple) - 1]


def coded_task_10(input_string):
    return input_string[::-1]


def coded_task_11(num):
    return f'{num // 60}:{num % 60}'


def coded_task_12(input_string):
    return input_string.split()[-1]


def coded_task_13(input_string):
    return ' '.join(input_string.split()[::-1])


def coded_task_14(num_fib):
    if isinstance(num_fib, int) and (num_fib > 0):
        fib_list_aux = [0, 1]
        for i in (range(num_fib - 1)):
            fib_list_aux.append(fib_list_aux[i] + fib_list_aux[i + 1])
        return fib_list_aux[1:]


def coded_task_15(input_list):
    return [x for x in input_list if x % 2 == 1]


def coded_task_16(input_num):
    return sum(x for x in range(1, input_num + 1))


def coded_task_17(input_num):
    return reduce(lambda x, y: x * y, range(1, input_num + 1))


def coded_task_18(input_str):
    new_string = ''.join([chr((ord(x) - 97 + 1) % 26 + 97) for x in input_str])
    new_string = ''.join(x.upper() if x in 'aeiou' else x for x in new_string)
    return new_string


def coded_task_19(input_str):
    return ''.join([chr(y) for y in sorted(ord(x) for x in input_str)])


def coded_task_20(num1, num2):
    return True if num2 > num1 else (False if num2 < num1 else '-1')
