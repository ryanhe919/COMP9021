import sys
from copy import deepcopy

class Cable_car:
    def __init__(self, file_name):
        self.file_name = file_name
        self.open_file()
        self.verify_file_content()
        self.is_perfect()
        self.longest_good_ride()
        self.remove_number()

    def open_file(self):
        try:
            with open(self.file_name, 'r') as file:
                self.file_content = file.read()
                self.file_content = self.file_content.replace('\n', '').split()

        except FileNotFoundError:
            print('Sorry, there is no such file. ')
            sys.exit()

    def verify_file_content(self):
        try:
            self.file_content = [int(_) for _ in self.file_content]
            if len(self.file_content) < 2:
                print('Sorry, input file does not store valid data.')
                sys.exit()
            for i in range(len(self.file_content) - 1):
                if self.file_content[i + 1] - self.file_content[i] < 1 or self.file_content[i] == 0:
                    print('Sorry, input file does not store valid data.')
                    sys.exit()

        except ValueError:
            print('Sorry, input file does not store valid data.')
            sys.exit()

    def is_perfect(self):
        difference = self.file_content[1] - self.file_content[0]
        for i in range(1, len(self.file_content) - 1):
            if self.file_content[i + 1] - self.file_content[i] != difference:
                print('The ride could be better...')
                return
        print('The ride is perfect!')
        return

    def longest_good_ride(self):
        temp = self.file_content[1] - self.file_content[0]
        result_list = []
        count = 1
        for i in range(1, len(self.file_content) - 1):
            if self.file_content[i + 1] - self.file_content[i] == temp:
                count += 1
            else:
                result_list.append(count)
                temp = self.file_content[i + 1] - self.file_content[i]
                count = 1
        result_list.append(count)
        print(f'The longest good ride has a length of: {sorted(result_list)[-1]}')
        return

    def remove_number(self):
        max_diff = self.file_content[-1] - self.file_content[0]
        dp = [[1 for _ in range(len(self.file_content))] for e in range(max_diff + 1)]
        count = 1
        for i in range(1, len(self.file_content)):
            for j in range(i):
                diff = self.file_content[i] - self.file_content[j]
                dp[diff][i] = dp[diff][j] + 1
                if dp[diff][i] > count:
                    count = dp[diff][i]
        print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {len(self.file_content) - count}')



if __name__ == '__main__':
    file_name = input('Please enter the name of the file you want to get data from: ')
    car = Cable_car(file_name)
