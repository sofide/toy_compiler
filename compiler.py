import sys


PLUS = 'plus'
MINUS = 'minus'
PRODUCT = 'product'
DIVISION = 'division'


deeper_step = {
    PLUS: MINUS,
    MINUS: PRODUCT,
    PRODUCT: DIVISION,
}


def plus(a, b):
    return(a + b)

def minus(a, b):
    return (a - b)

def product(a, b):
    return (a * b)

def division(a, b):
    return (a / b)


function_map = {
    PLUS: plus,
    MINUS: minus,
    PRODUCT: product,
    DIVISION: division
}

operator_map = {
    PLUS: '+',
    MINUS: '-',
    PRODUCT: '*',
    DIVISION: '/'
}

def compute_string(string, operation=PLUS):
    terms = string.split(operator_map[operation])
    next_step = deeper_step.get(operation)
    if not next_step:
        number_terms = [float(number) for number in terms]
    else:
        number_terms = [compute_string(term, next_step) for term in terms]

    for i, number in enumerate(number_terms):
        if i == 0:
            result = number
        else:
            result = function_map[operation](result, number)

    return result


if __name__ == '__main__':
    string = sys.argv[1]

    result = compute_string(string)

    print(result)
