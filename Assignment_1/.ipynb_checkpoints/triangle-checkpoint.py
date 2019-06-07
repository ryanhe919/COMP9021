import sys
def open_and_read_file():
    file_name = input('which data file do you want to use? ')
    try:
        with open(f'./{file_name}', 'r') as file:
            List = file.read()
        file.closed
    except FileNotFoundError:
        print('The file is not found.')
        sys.exit()
    return List

def analize_data(l):


if __name__ == '__main__':
    l = open_and_read_file()
    analize_data(l)