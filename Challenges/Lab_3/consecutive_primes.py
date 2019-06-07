from math import sqrt

def is_prime(n):
    # Only used to test odd numbers.
    return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))

prime_list = []

for i in range(10001, 100000, 2):
    if is_prime(i):
        prime_list.append(i)

for i in range(10001, 100000 - 30, 2):
    if i in prime_list and i + 2 in prime_list and i + 6 in prime_list and i + 12 in prime_list and i + 20 in prime_list and i + 30 in prime_list:
        if all(not is_prime(x) for x in range(i + 4, i + 6, 2))\
           and all(not is_prime(x) for x in range(i + 8, i + 12, 2))\
           and all(not is_prime(x) for x in range(i + 14, i + 20, 2))\
           and all(not is_prime(x) for x in range(i + 22, i + 30, 2)):
            print(f'{i} {i+2} {i+6} {i+12} {i+20} {i+30}')
