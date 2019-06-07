import random
import sys
import math
from statistics import mean, median, pstdev
def input_seed_and_nb_of_elements():
    try:
        seed = input('Input a seed for the random number generator: ')
        seed = int(seed)
    except ValueError:
        print('Input Error!')
        sys.exit()

    try:
        nb_of_elements = input('How many elements do you want to generate? ')
        nb_of_elements = int(nb_of_elements)
        if nb_of_elements < 0:
            raise ValueError
    except ValueError:
        print('Input Error!')
        sys.exit()
    return seed, nb_of_elements


def generate_random_list(seed, nb_of_elements):
    random.seed(seed)
    L = [random.randrange(-50, 50) for _ in range(nb_of_elements)]
    return L

def compute_without_builtin_function(L):
    mean = sum(L) / len(L)
    L = sorted(L)
    if len(L) % 2 == 0:
        median = (L[len(L) // 2] + L[len(L) // 2 - 1]) / 2
    else:
        median = L[len(L) // 2]
    standard_deviation = 0
    for i in range(len(L)):
        standard_deviation += (L[i] - mean) ** 2
    standard_deviation = math.sqrt(standard_deviation / len(L))
    return mean, median, standard_deviation

def compute_with_builtin_function(L):
    return mean(L), median(L), pstdev(L)


if __name__ == '__main__':
    seed, nb_of_elements = input_seed_and_nb_of_elements()
    L = generate_random_list(seed, nb_of_elements)
    print()
    print(f'The list is: {L}')
    print()
    mean1, median1, standard_deviation1 = compute_without_builtin_function(L)
    mean2, median2, standard_deviation2 = compute_with_builtin_function(L)

    print(f'The mean is {mean1:1.2f}.')
    print(f'The median is {median1:1.2f}.')
    print(f'The standard deviation is {standard_deviation1:1.2f}.')
    print()
    print('Confirming with function from the statistics module: ')
    print(f'The mean is {mean2:1.2f}.')
    print(f'The median is {median2:1.2f}.')
    print(f'The standard deviation is {standard_deviation2:1.2f}.')

