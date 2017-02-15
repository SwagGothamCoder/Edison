from binary_tree import BinaryTree

class Solver(object):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
        self.equation = BinaryTree('=', self.expression1, self.expression2)
        self.inverses = {'+': '-', '-': '+', '*': '/', '/': '*', '^': '^'}
    
    def contains_var(self, tree, var):
        var_present = False
        if type(tree.left) == BinaryTree:
            if self.contains_var(tree.left, var):
                var_present = True
        else:
            if tree.left == var:
                var_present = True
        if type(tree.right) == BinaryTree:
            if self.contains_var(tree.right, var):
                var_present = True
        else:
            if tree.right == var:
                var_present = True
        return var_present
    
    def apply_inverse(self, var, left_right_list):
        special_ops = ['-', '/', '^']
        left = left_right_list[0]
        right = left_right_list[1]
        if type(left) == float:
            return 'ERROR'
        op_to_undo = left.root
        op_inverse = self.inverses[op_to_undo]
        if type(left.left) == BinaryTree and type(left.right) == BinaryTree:
            if self.contains_var(left.left, var) and self.contains_var(left.right, var):
                return 'Cannot undo any more'
            elif self.contains_var(left.left, var):
                if op_inverse == '^':
                    right = BinaryTree(op_inverse, right, BinaryTree('^', left.right, -1.0))
                else:
                    right = BinaryTree(op_inverse, right, left.right)
                left = left.left
            elif self.contains_var(left.right, var):
                if left.root in special_ops:
                    if op_inverse == '^':
                        right = BinaryTree(op_inverse, right, BinaryTree('^', left.right, -1.0))
                    else:
                        right = BinaryTree(op_inverse, right, left.right)
                    left = left.left
                else:
                    right = BinaryTree(op_inverse, right, left.left)
                    left = left.right
            else:
                return 'Variable not on the left'
        elif type(left.left) == BinaryTree:
            if left.right == var and self.contains_var(left.left, var):
                return 'Cannot undo any more'
            elif self.contains_var(left.left, var):
                if op_inverse == '^':
                    right = BinaryTree(op_inverse, right, BinaryTree('^', left.right, -1.0))
                else:
                    right = BinaryTree(op_inverse, right, left.right)
                left = left.left
            elif left.right == var:
                if left.root in special_ops:
                    if op_inverse == '^':
                        right = BinaryTree(op_inverse, right, BinaryTree('^', left.right, -1.0))
                    else:
                        right = BinaryTree(op_inverse, right, left.right)
                    left = left.left
                else:
                    right = BinaryTree(op_inverse, right, left.left)
                    left = left.right
            else:
                return 'Variable not on the left'
        elif type(left.right) == BinaryTree:
            if left.left == var and self.contains_var(left.right, var):
                return 'Cannot undo any more'
            elif self.contains_var(left.right, var):
                if left.root in special_ops:
                    if op_inverse == '^':
                        right = BinaryTree(op_inverse, right, BinaryTree('^', left.right, -1.0))
                    else:
                        right = BinaryTree(op_inverse, right, left.right)
                    left = left.left
                else:
                    right = BinaryTree(op_inverse, right, left.left)
                    left = left.right
            elif left.left == var:
                if op_inverse == '^':
                    right = BinaryTree(op_inverse, right, BinaryTree('^', left.right, -1.0))
                else:
                    right = BinaryTree(op_inverse, right, left.right)
                left = left.left
            else:
                return 'Variable not on the left'
        else:
            if left.left == var and left.right == var:
                return 'Cannot undo any more'
            elif left.left == var:
                if op_inverse == '^':
                    right = BinaryTree(op_inverse, right, BinaryTree('^', left.right, -1.0))
                else:
                    right = BinaryTree(op_inverse, right, left.right)
                left = left.left
            elif left.right == var:
                if left.root in special_ops:
                    if op_inverse == '^':
                        right = BinaryTree(op_inverse, right, BinaryTree('^', left.right, -1.0))
                    else:
                        right = BinaryTree(op_inverse, right, left.right)
                    left = left.left
                else:
                    right = BinaryTree(op_inverse, right, left.left)
                    left = left.right
            else:
                return 'Variable not on the left'
        return left, right