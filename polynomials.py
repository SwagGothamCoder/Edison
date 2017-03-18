import numpy as np
from linear_algebra import companion_matrix

def roots(coefficient_vector):
    ''' Returns all the roots of the polynomial represented in the coefficient vector '''
    # Coefficient vector should contain all coefficients in order of the lowest power to the highest
    # The vector should also be vertical
    C = companion_matrix(coefficient_vector)
    solutions = np.linalg.eig(C)
    return list(solutions[0])

def real_roots(coefficient_vector):
    ''' Returns only real valued roots of the polynomial represented in the coefficient vector '''
    # Coefficient vector should contain all coefficients in order of the lowest power to the highest
    # The vector should also be vertical
    solutions = roots(coefficient_vector)
    real_solutions = []
    for solution in solutions:
        if str(solution)[-4:-1] == '+0j':
            real_solutions += [float(str(solution)[1:-4])]
    return real_solutions

def imaginary_roots(coefficient_vector):
    ''' Returns only imaginary roots of the polynomial represented in the coefficient vector '''
    # Coefficient vector should contain all coefficients in order of the lowest power to the highest
    # The vector should also be vertical
    solutions = roots(coefficient_vector)
    imaginary_solutions = []
    for solution in solutions:
        if str(solution)[-4:-1] != '+0j':
            imaginary_solutions += [str(solution)[1:-4]]
    return imaginary_solutions

def evaluate_polynomial(coefficient_vector, value):
    solution = np.array(coefficient_vector)
    for idx, element in enumerate(solution):
        solution[idx] = element * (value ** idx)
    return sum(solution)