'''
displays a conversion table from Celsius degrees to Fahrenheit degrees, with the former ranging from 0 to 100 in steps of 10.

'''

min_temperature = 0
max_temperature = 100
step = 10


def celsius_to_fahrenheit():
    print('Celsius\tFahrenheit')
    for celsius in range(min_temperature, max_temperature + 1, step):
        fahrenheit = celsius * 9 / 5 + 32
        print(f'{celsius:7d}\t{fahrenheit:10.0f}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    celsius_to_fahrenheit()
