import sys
import random
def input_seed_and_nb_of_elements():
    try:
        seed = int(input('Input a seed for the random number generator: '))
        nb_of_elements = int(input('How many elements do you want to generate? '))
        if nb_of_elements < 0:
            raise ValueError
    except ValueError:
        print('Input Error!!')
        sys.exit()

    return seed, nb_of_elements

def generate_random_list(seed, nb_of_elements):
    random.seed(seed)
    L = [random.randint(0, 20) for _ in range(nb_of_elements)]
    return L

def classify_list(L):
    L1 = [0] * 4
    for i in L:
        if i >= 0 and i <= 4:
            L1[0] += 1
        elif i >= 5 and i <= 9:
            L1[1] += 1
        elif i >= 10 and i <= 14:
            L1[2] += 1
        else:
            L1[3] += 1
    return L1


if __name__ == '__main__':
    seed, nb_of_elements = input_seed_and_nb_of_elements()
    L = generate_random_list(seed, nb_of_elements)
    L1 = classify_list(L)
    print()
    print(f'The list is: {L}')
    print()
    for i in range(len(L1)):
        if L1[i] == 1:
            print(f'There are {L1[i]} element between {i * 5} and {i * 5 + 4}')
        elif L1[i] == 0:
            print(f'There are no element between {i * 5} and {i * 5 + 4}')
        else:
            print(f'There are {L1[i]} elements between {i * 5} and {i * 5 + 4}')
