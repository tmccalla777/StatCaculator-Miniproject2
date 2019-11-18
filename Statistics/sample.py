import random


def Sample(list, size):
    random_values = random.choices(list, k=size - 1)
    return random_values
