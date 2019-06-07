min_i, max_i, max_j, max_k = 10, 99, 99, 99
for i in range(min_i, max_i + 1):
    for j in range(i, max_j + 1):
        for k in range(j, max_k + 1):
            if len(set(str(i)+ str(j)+ str(k))) == 6:
                if set(str(i)+ str(j)+ str(k)) == set(str(i*j*k)):
                    print(f'{i} x {j} x {k} = {i * j * k}')
