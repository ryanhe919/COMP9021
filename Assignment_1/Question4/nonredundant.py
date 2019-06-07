import sys
import copy
def isredundant(i, dic):
    L1 = copy.deepcopy(dic[i[1]])
    L1.remove(i[0])
    for x in L1:
        if i[0] in dic[x]:
            return True
    return False
file_name = input('which data file do you want to use? ')
try:
    with open(f'{file_name}', 'r') as file:
        relation = file.readlines()
    file.closed
except FileNotFoundError:
    print('Dont\'t find file. ')
    sys.exit()

print(relation)
for i in range(len(relation)):
    relation[i] = relation[i].replace('R', '')
    relation[i] = relation[i].replace('(', '')
    relation[i] = relation[i].replace(')', '')
    relation[i] = relation[i].replace('\n', '')
    relation[i] = relation[i].split(',')
    for j in range(len(relation[i])):
       relation[i][j] = int(relation[i][j])
print(relation)

dic = {}
for i in range(len(relation)):
    for j in range(len(relation[i])):
        if relation[i][j] not in dic:
            dic.update({relation[i][j]:[]})
for i in range(len(relation)):
    dic[relation[i][1]].append(relation[i][0])

for i in dic:
    for j in dic:
        if i in dic[j]:
            for z in dic[i]:
                dic[j].append(z)
for i in dic:
    dic[i] = set(dic[i])
print(dic)

redundant_relation = []
for i in relation:
    if isredundant(i, dic):
        redundant_relation.append(i)
for i in redundant_relation:
    relation.remove(i)
print(relation)
print('The nonredundant facts are:')
for i in relation:
    print(f'R({i[0]},{i[1]})')

