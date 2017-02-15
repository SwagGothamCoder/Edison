import math

from solver import Solver
from binary_tree import BinaryTree
from expression_parser import Expression_Parser

def run_edison_interface():
    parser = Expression_Parser()
    #equation = '78 / 3 * 2 = 100 * x'
    #equation = '78 / 3 * 2 - 10.5656 / x = 100 * 27.235425'
    equation = raw_input('Enter equation:')
    equation = equation.replace('pi', str(math.pi))
    equation = equation.replace('e', str(math.e))
    equation = equation.split('=')
    ex1 = parser.build_tree(equation[0].split(), ['*', '/'])
    ex2 = parser.build_tree(equation[1].split(), ['*', '/'])
    s = Solver(ex1, ex2)
    
    var = raw_input('Solve for:')
    s.equation.left = parser.evaluate_tree(s.equation.left)
    s.equation.right = parser.evaluate_tree(s.equation.right)
    solved = False
    while not solved:
        if s.apply_inverse(var, [s.equation.left, s.equation.right]) == 'ERROR':
            if s.apply_inverse(var, [s.equation.right, s.equation.left]) == 'ERROR':
                print('ERROR')
            else:
                s.equation.right, s.equation.left = s.apply_inverse(var, [s.equation.right, s.equation.left])
        else:
            if s.apply_inverse(var, [s.equation.left, s.equation.right]) == 'Variable not on the left':
                s.equation.left, s.equation.right = s.apply_inverse(var, [s.equation.right, s.equation.left])
            else:
                s.equation.left, s.equation.right = s.apply_inverse(var, [s.equation.left, s.equation.right])
        if type(s.equation.left) == BinaryTree:
            s.equation.left = parser.evaluate_tree(s.equation.left)
        if type(s.equation.right) == BinaryTree:
            s.equation.right = parser.evaluate_tree(s.equation.right)
        if s.equation.right == var or s.equation.left == var:
            solved = True
    
    if s.equation.right == var:
        answer = s.equation.left
    else:
        answer = s.equation.right
    if type(answer) == BinaryTree:
        answer = parser.tree_to_string(answer)
    print(var, '=', answer)