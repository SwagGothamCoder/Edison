import operator
import string
from binary_tree import BinaryTree

class Expression_Parser(object):
    def __init__(self):
        self.operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
    
    def build_tree(self, expression, ops):
        while not all([type(b) == BinaryTree for b in expression]):
            if '^' in expression:
                ops = ['^']
            elif '*' in expression or '/' in expression:
                ops = ['*', '/']
            else:
                ops = ['+', '-']
            for idx, element in enumerate(expression):
                if element in ops:
                    left = expression[idx-1]
                    right = expression[idx+1]
                    expression = expression[:idx] + expression[idx+2:]
                    if type(left) == BinaryTree and type(right) == BinaryTree:
                        expression[idx-1] = BinaryTree(str(element), left, right)
                    elif type(left) == BinaryTree:
                        if ' ' in right:
                            if '^' in right:
                                right = self.build_tree(list(right), ['^'])
                            elif '*' in right or '/' in right:
                                right = self.build_tree(list(right), ['*', '/'])
                            else:
                                right = self.build_tree(list(right), ['+', '-'])
                        if any([char in string.letters for char in right]):
                            expression[idx-1] = BinaryTree(str(element), left, str(right))
                        elif type(right) == BinaryTree:
                            expression[idx-1] = BinaryTree(str(element), left, right)
                        else:
                            expression[idx-1] = BinaryTree(str(element), left, float(right))
                    elif type(right) == BinaryTree:
                        if ' ' in left:
                            if '^' in left:
                                left = self.build_tree(list(left), ['^'])
                            elif '*' in left or '/' in left:
                                left = self.build_tree(list(left), ['*', '/'])
                            else:
                                left = self.build_tree(list(left), ['+', '-'])
                        if any([char in string.letters for char in left]):
                            expression[idx-1] = BinaryTree(str(element), str(left), right)
                        elif type(left) == BinaryTree:
                            expression[idx-1] = BinaryTree(str(element), left, right)
                        else:
                            expression[idx-1] = BinaryTree(str(element), float(left), right)
                    else:
                        if ' ' in right:
                            if '^' in right:
                                right = self.build_tree(list(right), ['^'])
                            elif '*' in right or '/' in right:
                                right = self.build_tree(list(right), ['*', '/'])
                            else:
                                right = self.build_tree(list(right), ['+', '-'])
                        if ' ' in left:
                            if '^' in left:
                                left = self.build_tree(list(left), ['^'])
                            elif '*' in left or '/' in left:
                                left = self.build_tree(list(left), ['*', '/'])
                            else:
                                left = self.build_tree(list(left), ['+', '-'])
                        if type(left) == BinaryTree and type(right) == BinaryTree:
                            expression[idx-1] = BinaryTree(str(element), left, right)
                        elif type(left) == BinaryTree:
                            if any([char in string.letters for char in right]):
                                expression[idx-1] = BinaryTree(str(element), left, str(right))
                            else:
                                expression[idx-1] = BinaryTree(str(element), left, float(right))
                        elif type(right) == BinaryTree:
                            if any([char in string.letters for char in left]):
                                expression[idx-1] = BinaryTree(str(element), str(left), right)
                            else:
                                expression[idx-1] = BinaryTree(str(element), float(left), right)
                        else:
                            if any([char in string.letters for char in left]) and any([char in string.letters for char in right]):
                                expression[idx-1] = BinaryTree(str(element), str(left), str(right))
                            elif any([char in string.letters for char in left]):
                                expression[idx-1] = BinaryTree(str(element), str(left), float(right))
                            elif any([char in string.letters for char in right]):
                                expression[idx-1] = BinaryTree(str(element), float(left), str(right))
                            else:
                                expression[idx-1] = BinaryTree(str(element), float(left), float(right))
                    break
        return expression[0]
    
    def evaluate_tree(self, tree):
        if type(tree.left) == BinaryTree:
            tree.left = self.evaluate_tree(tree.left)
        if type(tree.right) == BinaryTree:
            tree.right = self.evaluate_tree(tree.right)
        if type(tree.right) in [int, float] and type(tree.left) in [int, float]:
            return self.operations[tree.root](tree.left, tree.right)
        else:
            return tree
    
    def tree_to_string(self, tree):
        left = tree.left
        right = tree.right
        if type(tree.left) == BinaryTree:
            left = self.tree_to_string(tree.left)
        if type(tree.right) == BinaryTree:
            right = self.tree_to_string(tree.right)
        return str(left)+' '+tree.root+' '+str(right)