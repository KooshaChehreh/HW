import argparse

parser = argparse.ArgumentParser()
g = parser.add_argument_group()
g.add_argument('-g', '--grade', type=int, nargs='+', required=True)
parser.add_argument('-f', '--float', type=int)
args = parser.parse_args()


def avg(argument: list, dec_num):
    sum_num = 0
    if len(argument) == 0:
        return 'At least one script is needed!'

    else:
        for script in argument:
            sum_num += float(script)
        average = round(sum_num / len(argument), dec_num)
        return f'Your scripts average is {average}'


print(avg(args.grade, args.float))
