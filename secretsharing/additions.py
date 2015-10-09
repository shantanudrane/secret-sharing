# -*- coding: utf-8 -*-
"""
    Testing the Additive Homomorphic Property of Shamir Secret Sharing
    Testing the ability to compute linear combinations using Shamir Secret Sharing
    To test additive homomorphism, just use coeff1 = coeff2 = 1
"""

import string
import numpy as np
import sys

from primes import get_large_enough_prime
from polynomials import random_polynomial, \
    get_polynomial_points, modular_lagrange_interpolation
from sharing import secret_int_to_points_given_prime, points_to_secret_int

if len(sys.argv) != 7 :
	print '---'
	print 'The arguments to this script are as follows: '
	print 'Argument 1: Total number of shares that each secret will be split into (n).'
	print 'Argument 2: Number of shares needed to reconstruct the secret (k).'
	print 'Argument 3: The first secret (any integer).'
	print 'Argument 4: The second secret (any integer).'
	print 'Argument 5: The first coefficient (any integer).'
	print 'Argument 6: The second ciefficient (any integer).'
	print '---'
	print 'Example: python additions.py 7 3 123 -556 3 -4'
	print '---'
 	sys.exit()	


# Get inputs. Just trying this for 2 secrets and 2 coefficients
num_points = int(sys.argv[1])
threshold = int(sys.argv[2])
secret1 = int(sys.argv[3])
secret2 = int(sys.argv[4])
coeff1 = int(sys.argv[5])
coeff2 = int(sys.argv[6])

# Determine a large-enough prime number
prime = get_large_enough_prime([max(abs(secret1), abs(secret2))*max(abs(coeff1), abs(coeff2)), num_points])

# Compute shares of each secret
shares1 = secret_int_to_points_given_prime(secret1, threshold, num_points, prime)
print shares1
shares2 = secret_int_to_points_given_prime(secret2, threshold, num_points, prime)
print shares2

# Reconstruct the shares of the linear combination of the secret
shares3 = []
for i in range(1,num_points+1):
	shares3.append((i, (coeff1*shares1[i-1][1] + coeff2*shares2[i-1][1]) % prime))
print shares3

recovered_sum = points_to_secret_int(shares3[1:1+threshold])

if recovered_sum > prime/2:
	recovered_sum -= prime

print 'Recovered Sum is', recovered_sum
print 'Verification: The answer should be', coeff1*secret1 + coeff2*secret2

