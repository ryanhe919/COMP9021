import turtle


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

print(rectangle)
turtle.speed(9)
turtle.left(90)
for i in range(len(rectangle)):
    turtle.penup()
    turtle.setposition(rectangle[i][0]*0.2,rectangle[i][1]*0.2)
    turtle.pendown()
    turtle.forward((rectangle[i][3]- rectangle[i][1])*0.2)
    turtle.right(90) 
    turtle.forward((rectangle[i][2]- rectangle[i][0])*0.2)
    turtle.right(90)
    turtle.forward((rectangle[i][3]- rectangle[i][1])*0.2)
    turtle.right(90)
    turtle.forward((rectangle[i][2]- rectangle[i][0])*0.2)
    turtle.right(90)


