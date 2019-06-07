from math import factorial
import sys
def input_number():
    try:
        x = int(input('Input a nonnegative integer: '))
        if x < 0:
            raise ValueError
    except ValueError:
        print('Incorrect input, giving up. ')
        sys.exit()
    return x

def compute_by_dividing_by_10(number):
    result = 0
    while True:
        if number % 10 == 0:
            number //= 10
            result += 1
        else:
            break
    return result

def compute_by_converting_to_string(number):
    number = str(number)
    result = 0
    for i in number[len(number)-1: 0: -1]:
        if i == '0':
            result += 1
        else:
            break
    return result

def compute_by_the_smart_way(x):
    n = 0
    result = 0
    while 5 ** n <= x:
        n += 1
    for i in range(1, x+1):
        for j in range(1, n):
            if i % (5 ** j) == 0:
                result += 1
    return result
if __name__ == '__main__':
    x = input_number()
    number = factorial(x)
    result_1 = compute_by_dividing_by_10(number)
    result_2 = compute_by_converting_to_string(number)
    result_3 = compute_by_the_smart_way(x)
    print(f'Computing the number of trailing 0s in {x}! by dividing by 10 for long enough: {result_1}')
    print(f'Computing the number of trailing 0s in {x}! by converting it into a string: {result_2}')
    print(f'Computing the number of trailing 0s in {x}! the smart way: {result_3}')
