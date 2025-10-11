import random

NUMBERS_PER_PICK = 6
MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45

def main():
    number_of_picks = int(input("How many quick picks?: "))
    generate_quick_picks(number_of_picks)


def generate_quick_picks(number_of_picks):
    for i in range(number_of_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_PICK:
            random_number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
            if not(random_number in quick_pick):
                quick_pick.append(random_number)

        for k in range(len(quick_pick)):
            minimum_index = k
            for j in range(k+1, len(quick_pick)):
                if quick_pick[j] < quick_pick[minimum_index]:
                    minimum_index = j
            quick_pick[k], quick_pick[minimum_index] = quick_pick[minimum_index], quick_pick[k]

        print(quick_pick)

main()