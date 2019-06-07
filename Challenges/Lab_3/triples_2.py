from math import sqrt
for i in range(100, 997):
    for a in range(0, int(sqrt(999))):
        flag = [[0],[0],[0]]
        for b in range(a, int(sqrt(999))):
            if i == a**2 + b**2:
                flag[0][0] = 1
                flag[0].append(a)
                flag[0].append(b)
                
            if i + 1 == a ** 2 + b ** 2:
                flag[1][0] = 1
                flag[1].append(a)
                flag[1].append(b)
            if i + 2 == a ** 2 + b ** 2:
                flag[2][0] = 1
                flag[2].append(a)
                flag[2].append(b)
    
    if flag[0][0] == 1 and flag[1][0] == 1 and flag[2][0] == 1:
        print(f'({i}, {i+1}, {i+2}),({flag[0][1]}^2 + {flag[0][2]}^2, {flag[1][1]}^2 + {flag[1][2]}^2, {flag[2][1]}^2 + {flag[2][2]}^2)')
