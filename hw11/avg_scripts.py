import sys

num = sys.argv


def avg(alist: list):
    sum_num = 0
    if len(alist) < 2:
        return 'At least one argument needed!'

    else:
        for arg in range(1, len(alist)):
            if float(alist[arg]):
                sum_num += float(alist[arg])
            return 'arguments must be integer!'
    average = sum_num / (len(alist) - 1)
    return f'Average of scripts is {average}'


print(avg(num))
