import sys

def point_in_rectangle(x, y, rectangle):
    for i in range(len(rectangle)):
        if x < rectangle[i][2] and x > rectangle[i][0] and y < rectangle[i][3] and y > rectangle[i][1]:
            return False
    return True



file_name = input('Which data file do you want to use? ')
try:
    with open(f'{file_name}', 'r') as file:
        rectangle = file.readlines()
    file.closed
except FileNotFoundError:
    print('Dont\'t find file. ')
    sys.exit()

for i in range(len(rectangle)):
    rectangle[i] = rectangle[i].replace('\n','')
    rectangle[i] = rectangle[i].split()
    for j in range(len(rectangle[i])):
        rectangle[i][j] = int(rectangle[i][j])

perimeter = 0
for i in range(len(rectangle)):
    for y in range(rectangle[i][1], rectangle[i][3]):
        if point_in_rectangle(rectangle[i][0], y, rectangle):
            if point_in_rectangle(rectangle[i][0], y+1, rectangle):
                perimeter += 1
    for x in range(rectangle[i][0], rectangle[i][2]):
        if point_in_rectangle(x, rectangle[i][3], rectangle):
            if point_in_rectangle(x+1, rectangle[i][3], rectangle):
                perimeter += 1
    for x in range(rectangle[i][0], rectangle[i][2]):
        if point_in_rectangle(x, rectangle[i][1],rectangle):
            if point_in_rectangle(x + 1, rectangle[i][1], rectangle):
                perimeter += 1
    for y in range(rectangle[i][1], rectangle[i][3]):
        if point_in_rectangle(rectangle[i][2], y, rectangle):
            if point_in_rectangle(rectangle[i][2], y + 1, rectangle):
                perimeter += 1
print(f'The perimeter is: {perimeter}')


