# -*- coding: utf-8 -*-
"""
    Additive Homomorphic Property of Shamir Secret Sharing
"""

import string
import numpy as np

from primes import get_large_enough_prime
from polynomials import random_polynomial, \
    get_polynomial_points, modular_lagrange_interpolation
from sharing import secret_int_to_points_given_prime, points_to_secret_int

secret1 = 123
secret2 = -556
num_points = 7
threshold = 3

prime = get_large_enough_prime([max(abs(secret1), abs(secret2)), num_points])

shares1 = secret_int_to_points_given_prime(secret1, threshold, num_points, prime)
print shares1
shares2 = secret_int_to_points_given_prime(secret2, threshold, num_points, prime)
print shares2

shares3 = []
for i in range(1,num_points+1):
	shares3.append((i, (shares1[i-1][1] + shares2[i-1][1]) % prime))
print shares3

recovered_sum = points_to_secret_int(shares3[1:7])

if recovered_sum > prime/2:
	recovered_sum -= prime

print 'Recovered Sum is', recovered_sum
