# !usr/bin/env python3

OPERATORS = ['+', '-', '*', '/']


def get_input():
    """Obtain input from user"""
    operation = input()

    return operation


def clean_input(operation):
    """Handle whitespace, convert numbers to floats, and append to list"""
    num = ''
    statement = []
    
    for element in operation:
        if element.isnumeric():
            num += element
        elif element in OPERATORS:
            statement.append(float(num))
            statement.append(element)
            num = ''
    statement.append(float(num))

    return statement


def initialize_total(statement):
    """Inititalize total based on operators"""
    if '*' in statement or '/' in statement:
        total = 1
    else:
        total = 0

    return total


def find_operands(statement, index):
    op1 = float(statement[index - 1])
    op2 = float(statement[index + 1])
    return op1, op2


def remove_and_replace(statement, index, result):
    """Remove the operator and the operands, then insert result of operation"""
    del statement[index - 1: index + 2]
    statement.insert(index - 1, result)

    return statement


def multiply_divide(statement):
    """Perform multiplication and division then simplify statement"""

    # Filter for * and / in the statement and find the first element's index
    operators = list(filter(lambda x: x in ('*', '/'), statement))
    index = statement.index(operators[0])

    # Find operands
    op1, op2 = find_operands(statement, index)

    # Perform operation
    if operators[0] == '*':
        result = op1 * op2
    elif operators[0] == '/':
        result = op1 / op2

    # Replace operators and operands with result
    remove_and_replace(statement, index, result)

    return statement


def add_subtract(statement):
    """Perform addition and subtraction then simplify statement"""
    operators = list(filter(lambda x: x in ('+', '-'), statement))
    index = statement.index(operators[0])

    # Find operands
    op1, op2 = find_operands(statement, index)

    # Perform operation
    if operators[0] == '+':
        result = op1 + op2
    elif operators[0] == '-':
        result = op1 - op2

    # Replace operator and operands with result
    remove_and_replace(statement, index, result)

    return statement


def perform_operations(statement):
    """Evaluate the statement"""
    while statement.count('*') >= 1 or statement.count('/') >= 1:
        statement = multiply_divide(statement)

    while statement.count('+') >= 1 or statement.count('-') >= 1:
        statement = add_subtract(statement)
        

    return statement[0]


def main():
    # statement = get_input()
    statement = "6 + 3 * 4 - 9"
    statement = clean_input(statement)
    result = perform_operations(statement)
    print(result)


if __name__ == "__main__":
    # pass
    main()