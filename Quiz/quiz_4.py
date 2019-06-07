# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by *** and Eric Martin for COMP9021


import os
import sys

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

# Replace this comment with your code
if not os.path.exists(directory):
    print(f'There is no directory named {directory}, giving up...')
    sys.exit()
male_list = []
female_list = []
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3:7])
    with open(directory + '/' + filename) as file:
        total_male = 0
        total_female = 0
        male_first_name_number = 0
        female_first_name_number = 0
        popularity_male_name = 0
        for line in file:
            name, gender,number = line.split(',')
            if gender == 'M':
                total_male += int(number)
                if name == first_name:
                    male_first_name_number = int(number)
            if gender == 'F':
                total_female += int(number)
                if name == first_name:
                    female_first_name_number = int(number)
        popularity_male_name = male_first_name_number / total_male * 100
        popularity_female_name = female_first_name_number / total_female * 100
        male_list.append((popularity_male_name, year))
        female_list.append((popularity_female_name, year))
male_list = sorted(male_list, reverse = True)
female_list = sorted(female_list, reverse = True)

if male_list[0][0] != 0:
    male_first_year = male_list[0][1]
    min_male_frequency = round(male_list[0][0],2)
if female_list[0][0] != 0:
    female_first_year = female_list[0][1]
    min_female_frequency = round(female_list[0][0],2)

if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )


