import os
import sys
import csv

def open_file(filename):
    if not os.path.exists(filename):
        print(f'There is no file named {filename} in the working directory, giving up...')
        sys.exit()


def input_indicator():
    indicator_contents = input('Enter an Indicator Name: ')
    return indicator_contents

    
if __name__ == '__main__':
    filename = 'HNP_Data.csv'
    open_file(filename)

   # indicator_contents = input_indicator()
    with open(filename)  as f:
        file = csv.reader(f)
    print(list(file))
