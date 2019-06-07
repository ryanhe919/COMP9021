# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

# Replace this comment with your code
L = list()
integral_part = numerator // denominator
remainder = numerator % denominator
while True:
	if remainder == 0:
		has_finite_expansion = True
		break
	else:
#		L.append(remainder)
		if remainder in L:
			break
		else:
			L.append(remainder)
			remainder *= 10
			sigma += str(remainder//denominator)
			remainder %= denominator

#print(remainder)
#print(L)

for i in range(0, len(L)):
	if L[i] == remainder:
		tau = sigma[i: len(L)]
		sigma = sigma[0: i]

#print(sigma)
#print(tau)
#print(L)


if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

