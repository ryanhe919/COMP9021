# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers at most equal to a given upper bound,
of a given length, all controlled by user input.

Outputs four lists:
- elements_to_keep, consisting of L's smallest element, L's third smallest element,
  L's fifth smallest element, ...
  Hint: use sorted(), list slices, and set()
- L_1, consisting of all members of L which are part of elements_to_keep, preserving
  the original order
- L_2, consisting of the leftmost occurrences of the members of L which are part of
  elements_to_keep, preserving the original order
- L_3, consisting of the LONGEST, and in case there are more than one candidate, the
  LEFTMOST LONGEST sequence of CONSECUTIVE members of L that reduced to a set,
  is a set of integers without gaps.
'''


import sys
from random import seed, randint


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []

# Replace this comment with your code
x = 0
L_order_set = set(L)
L_order_list = list(L_order_set)
L_order_list = sorted(L_order_list)

#print(L_order_set,L_order_list,L_order_list_2)
elements_to_keep = L_order_list[0:len(L_order_set):2]

for i in range(0,len(L)):
    for j in range(0,len(elements_to_keep)):
        if L[i] == elements_to_keep[j]:
            L_1.append(L[i])

for i in L_1:
    if i not in L_2:
        L_2.append(i)
x, y = 0, 0
for y in range(1, len(L)):
	for x in range(y,len(L)):
		L1 = L[x-y:x]
		L2 = sorted(L1)
		if list(set(L1)) == range(L2[0],L2[y-1]):
			L_3 = L1
			continue

for y in range(0,len(L)):
    for x in range(len(L)-y):
        L3 =[]
        L1 = L[x:x+y+1]
        L2 = sorted(L1)
        for z in range(L2[0],L2[len(L2)-1]+1):
            L3.append(z)
        S2 = set(L2)
        S3 = set(L3)
        if S2 == S3:
            L_3 = L1
            break
'''
S1 = {}
for x in range(len(L),0,-1):
    if S1 == {}:
        for y in range(len(L)-x):
            L1 = L[y:x+y+1]
            #print(L1)
            L2 = sorted(L1)
            S1 = set(range(L2[0], L2[len(L2)-1]+1))
            if set(L2) == S1:
                L_3 = L1
                break
            else:
                S1={}
    else:
        break
'''
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)
print('\nHere is L_1:')
print('  ', L_1)
print('\nHere is L_2:')
print('  ', L_2)
print('\nHere is L_3:')
print('  ', L_3)


