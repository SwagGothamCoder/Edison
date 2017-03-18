from __future__ import division

import numpy as np
from linear_algebra import evaluate_polynomial

def derivative(coefficient_vector):
    ''' Returns the derivative of the polynomial represented by the coefficient vector '''
    derivative = np.array(coefficient_vector[1:])
    for idx, value in enumerate(derivative):
        derivative[idx] = value*(idx+1)
    return derivative

def indefinite_integral(coefficient_vector):
    ''' Returns the indefinite integral of the polynomial represented by the coefficient vector '''
    integral = np.array(np.append(np.zeros((1,1)), coefficient_vector, axis=0))
    for idx, value in enumerate(integral):
        value = value[0]
        integral[idx] = value / idx
    integral = [e[0] for e in integral]
    integral[0] = 'c'
    return integral

def definite_integral(coefficient_vector, alpha, beta):
    ''' Returns the definite integral of the polynomial represented by the coefficient vector and bounded by alpha and beta '''
    integral = indefinite_integral(coefficient_vector)
    integral[0] = 0.0
    integral = np.array(integral, dtype=float)
    return evaluate_polynomial(integral, beta) - evaluate_polynomial(integral, alpha)