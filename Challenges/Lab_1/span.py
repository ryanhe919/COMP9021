import random
import sys
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
    L = [random.randrange(0, 100) for _ in range(nb_of_elements)]
    return L

def compute_with_builtin_function(L):
    return max(L) - min(L)

def compute_without_builtin_function(L):
    max_element = L[0]
    min_element = L[0]
    for i in range(1, len(L)):
        if L[i] > max_element:
            max_element = L[i]
        if L[i] < min_element:
            min_element = L[i]
    return max_element - min_element
if __name__ == '__main__':
    seed, nb_of_elements = input_seed_and_nb_of_elements()
    L = generate_random_list(seed, nb_of_elements)
    print()
    print(f'This list is: {L}')
    result_2 = compute_with_builtin_function(L)
    result_1 = compute_without_builtin_function(L)
    print()
    print(f'The maximum difference between largest and smallest values in this list is: {result_1}')
    print(f'Confirming with builtin operations: {result_2}')

