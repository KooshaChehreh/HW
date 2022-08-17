import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', type=int, help='start number')
parser.add_argument('-e', type=int, help='end number')
parser.add_argument('-g', type=int, help='attempts')
args = parser.parse_args()

n = random.randint(args.s, args.e)


def run_guess_game_script():
    for attempt in range(args.g):

        if attempt == args.g - 1:
            print('This is your last chance!')
            guess = int(input(f"Enter an integer from {args.s} to {args.e}: "))
            if guess == n:
                print("Congrats! you guessed it!")
            else:
                print(f'You missed the game\nThe number was {n}')
        else:
            guess = int(input(f"Enter an integer from {args.s} to {args.e}: "))
            if guess < n:
                print("guess is low, enter Higher Number")
            elif guess > n:
                print("guess is high, enter Lower Number")
            else:
                print("you guessed it!")
                break


run_guess_game_script()

