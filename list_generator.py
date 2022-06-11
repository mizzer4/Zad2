import random

def generate_random_list(length):
    new_list = []

    for i in range(length):
        new_list.append(i)

    random.shuffle(new_list)

    return new_list

