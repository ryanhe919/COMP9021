import sys
file_name = input('which data file do you want to use? ')
try:
    with open(f'{file_name}', 'r') as file:
        coast = file.readlines()
    file.closed
except FileNotFoundError:
    print('Dont\'t find file. ')
    sys.exit()


for i in range(len(coast)):
    coast[i] = coast[i].replace('\n','')
    coast[i] = coast[i].split(' ')
    for j in range(coast[i].count('')):
        coast[i].remove('')
    for j in range(len(coast[i])):
        coast[i][j] = int(coast[i][j])

min_fish = coast[0][1]
max_fish = coast[0][1]
for i in range(1,len(coast)):
    max_fish += coast[i][1]
    if coast[i][1] < min_fish:
        min_fish = coast[i][1]
max_fish /= len(coast)
max_fish = int(max_fish)
while(True):
    coast_1 = []
    for i in range(len(coast)):
        coast_1.append(coast[i][1])
    middle_fish = (max_fish + min_fish) / 2
    for i in range(len(coast_1) - 1):
        coast_1[i + 1] += (coast_1[i] - middle_fish) - (coast[i+1][0] - coast[i][0])
    if coast_1[len(coast_1) - 1] >= middle_fish:
        min_fish = middle_fish
    if coast_1[len(coast_1) -1] < middle_fish:
        max_fish = middle_fish
    if int(max_fish) == int(min_fish):
        break

print(f'The maximum quantity of fish that each town can have is {int(max_fish)}')
