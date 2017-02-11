from expression_parser import Expression_Parser

parser = Expression_Parser()

while True:
    expression = raw_input('Expression:')
    expression = expression.split()
    print('Result:', parser.evaluate_tree(parser.build_tree(expression, ['*', '/'])))