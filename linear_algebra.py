import numpy as np

def companion_matrix(vector):
    ''' Returns the companion matrix of the vector '''
    # Coefficient vector should contain all coefficients in order of the lowest power to the highest
    # The vector should also be vertical
    n = len(vector)-1
    C = np.identity(n-1)
    C = np.append(np.zeros((1, n-1)), C, axis=0)
    C = np.append(C, -vector[:n], axis=1)
    return C

def vector_to_string(vector, var):
    ''' Returns the polynomial equivalent of the given vector '''
    expression = []
    for idx, element in enumerate(vector):
        element = element[0]
        if element != 0:
            if element == 1 and idx != 0:
                element = ''
            else:
                element = str(element)
            
            if idx == 0:
                expression += [element]
            elif idx == 1:
                expression += [element + var]
            else:
                expression += [element + var + '^' + str(idx)]
    return ''.join(e+' + ' for e in expression)[:-3]

def string_to_vector(string, var):
    ''' Returns the vector of the polynomial given in the string '''
    # First split the expression
    expression = string.split(' + ')
    # Then find the value of the highest order
    max_n = 0
    for element in expression:
        if var in element:
            if '^' in element:
                if float(element[element.index('^')+1:]) > max_n:
                    max_n = int(element[element.index('^')+1:])
            else:
                if 1 > max_n:
                    max_n = 1
    vector = np.zeros((max_n+1, 1))
    # Now fill in the vector in order
    for element in expression:
        if var in element:
            if '^' in element:
                idx = int(element[element.index('^')+1:])
                coefficient = element[:element.index(var)]
                if coefficient == '':
                    vector[idx] = 1.0
                else:
                    vector[idx] = float(coefficient)
            else:
                coefficient = element[:element.index(var)]
                if coefficient == '':
                    vector[1] = 1.0
                elif coefficient == '-':
                    vector[1] = -1.0
                else:
                    vector[1] = float(coefficient)
        else:
            vector[0] = float(element)
    return vector