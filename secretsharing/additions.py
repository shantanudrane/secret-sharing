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
from sharing import secret_int_to_points, points_to_secret_int

secret1 = 123L
secret2 = 456L

shares1 = secret_int_to_points(secret1, 2, 5)
print shares1
shares2 = secret_int_to_points(secret2, 2, 5)
print shares2



