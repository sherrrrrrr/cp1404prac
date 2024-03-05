import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6
QUICK_PICKS_COLUMN_WIDTH = 3


def main():
    number_of_picks = get_number_of_picks()
    display_quick_picks(number_of_picks)


def generate_lotto_numbers():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def generate_quick_pick():
    line = set()
    while len(line) < NUMBERS_PER_LINE:
        line.add(generate_lotto_numbers())
    return sorted(line)


def display_quick_picks(number_of_picks):
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def get_number_of_picks():
    return int(input("How many quick picks? "))


if __name__ == '__main__':
    main()
