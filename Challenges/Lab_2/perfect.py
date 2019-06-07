import sys

def input_integer():
    try:
        x = int(input('Input an integer: '))
        if x < 0:
            raise ValueError
    except ValueError:
        print('Input Error!')
        sys.exit()
    return x

def is_perfect_number(x):
    sum = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            sum += i
    if sum == x:
        return True
    else:
        return False

if __name__ == '__main__':
    number = input_integer()
    for i in range(1, number + 1):
        if is_perfect_number(i):
            print(f'{i} is a perfect number.')
