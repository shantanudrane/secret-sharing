# -*- coding: utf-8 -*-
"""
    Secret Sharing
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import string

from primes import get_large_enough_prime
from polynomials import random_polynomial, \
    get_polynomial_points, modular_lagrange_interpolation
from sharing import secret_int_to_points_given_prime, points_to_secret_int

secret1 = 123L
secret2 = 456L
num_points = 7
threshold = 3

prime = get_large_enough_prime([max(secret1, secret2), num_points])

shares1 = secret_int_to_points_given_prime(secret1, threshold, num_points, prime)
print shares1
shares2 = secret_int_to_points_given_prime(secret2, threshold, num_points, prime)
print shares2



