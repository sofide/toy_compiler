import itertools
import sys

CUSTOM_NEGATIVE_OPERATOR = 'This is ugly, I know, sorry for that.'

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
        number_terms = [float(number.replace(CUSTOM_NEGATIVE_OPERATOR, '-'))
                        for number in terms]
    else:
        number_terms = [compute_string(term, next_step) for term in terms]

    for i, number in enumerate(number_terms):
        if i == 0:
            result = number
        else:
            result = function_map[operation](result, number)

    return result


def solve_parenthesis(string):
    open_parenthesis_position = string.find('(')
    if open_parenthesis_position == -1:
        return string
    after_open_parenthesis = string[open_parenthesis_position + 1:]

    # solve inner parenthesis
    after_open_parenthesis = solve_parenthesis(after_open_parenthesis)

    close_parenthesis_position = after_open_parenthesis.find(')')

    if close_parenthesis_position == -1:
        raise SyntaxError('you forgot to close a parenthesis ")"')

    inside_parenthesis = after_open_parenthesis[:close_parenthesis_position]

    parenthesis_result = str(compute_string(inside_parenthesis))

    if parenthesis_result[0] == '-':
        parenthesis_result = CUSTOM_NEGATIVE_OPERATOR + parenthesis_result[1:]

    pre_parenthesis = string[:open_parenthesis_position]
    post_parenthesis = after_open_parenthesis[close_parenthesis_position+1:]

    string_with_solved_parenthesis = pre_parenthesis + parenthesis_result + post_parenthesis

    return string_with_solved_parenthesis


def handle_negative_numbers(string):
    operators = list(operator_map.values())
    operators.append('(')

    for operator in operators:
        original_negative = '{}-'.format(operator)
        custom_negative = '{}{}'.format(operator, CUSTOM_NEGATIVE_OPERATOR)

        string = string.replace(original_negative, custom_negative)

    if string[0] == '-':
        string = CUSTOM_NEGATIVE_OPERATOR + string[1:]

    return string



def validate_syntax(string):
    def hunt_invalid_syntax(error_message, valid_stuff=None, invalid_stuff=None, q_characters=1):
        invalid_characters = []
        if valid_stuff is not None:
            invalid_characters.extend([(pos, string[pos:pos+q_characters])
                                       for pos in range(len(string))
                                       if string[pos:pos+q_characters] not in valid_stuff])
        if invalid_stuff is not None:
            invalid_characters.extend([(pos, string[pos:pos+q_characters])
                                       for pos in range(len(string))
                                       if string[pos:pos+q_characters] in invalid_stuff])

        if invalid_characters:
            for position, character in invalid_characters:
                error_message = error_message  + '\n-"{}" (character #{})'.format(character,
                                                                                  position+1)

                error_message = error_message + "\n\nNote: blank spaces don't count as characters"

            raise SyntaxError(error_message)


    non_numeric_valid_characters = list(operator_map.values())
    non_numeric_valid_characters.extend(('(', ')', '.'))
    valid_characters = non_numeric_valid_characters + [str(n) for n in range(10)]


    hunt_invalid_syntax("I don't understand the following characters:",
                        valid_stuff=valid_characters)

    non_numeric_valid_characters.remove(')')
    if string[-1] in non_numeric_valid_characters:
        error_message = "The expression cannot end with {}".format(string[-1])
        raise SyntaxError(error_message)

    non_numeric_valid_characters.remove('-')
    non_numeric_valid_characters.remove('(')
    invalid_character_combination = itertools.product(non_numeric_valid_characters, repeat=2)
    invalid_character_combination = [a + b for a, b in invalid_character_combination]
    invalid_character_combination.extend([
        '.-', '-.', '-)',
        '+)', '*)', '/)', '.)', ').',
        '(+', '(*', '(/', '.(', '(.',
    ])

    hunt_invalid_syntax("The following characters combinations are not allowed:",
                        invalid_stuff=invalid_character_combination,
                        q_characters=2)



def compile(string):
    string = string.replace(' ', '')
    validate_syntax(string)
    string = handle_negative_numbers(string)
    string = solve_parenthesis(string)
    result = compute_string(string)

    return result

if __name__ == '__main__':
    def execute(string):
        try:
            result = compile(string)
        except SyntaxError as error:
            result = error

        print('{}\n\n'.format(result))


    if len(sys.argv) > 1:
        string_to_compute = sys.argv[1]
        execute(string_to_compute)

    while True:
        string_to_compute = input("Type an expression to compute: ")
        execute(string_to_compute)
