import random

NUMBERS_PER_PICK = 6
MINIMUM_AMOUNT = 1
MAXIMUM_AMOUNT = 45
def main():
    """Funciton for asking number of quick picks"""
    quick_pick_number = int(input("How many quick picks?: "))
    while quick_pick_number < 0:
        print("Pick amount cannot be less than zero")
        quick_pick_number = int(input("How many quick picks?: "))
    for i in range(quick_pick_number):
        quick_pick = []
        for j in range(NUMBERS_PER_PICK):
            number = random.randint(MINIMUM_AMOUNT, MAXIMUM_AMOUNT)
            while number in quick_pick:
                number = random.randint(MINIMUM_AMOUNT, MAXIMUM_AMOUNT)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))
main()