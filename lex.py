from ply import lex

tokens = (
    # SQL COMMANDS
    'ALTER', # alter table
    'TABLE',
    'AND',
    'AS',
    'AVG',
    'BETWEEN',
    'CASE',
    'COUNT',
    'CREATE', # create table
    'DELETE',
    'GROUP', # Group by
    'BY',
    'HAVING',
    'INNER', # Inner join
    'JOIN',
    'INSERT',
    'IS', # is null / is not null
    'NOT',
    'NULL',
    'LIKE',
    'LIMIT',
    'MAX',
    'MIN',
    'OR',
    'ORDER', # Order by
    'OUTER', # Outer join
    'ROUND',
    'SELECT',
    'DISTINCT', # Select distinct
    'SUM',
    'UPDATE',
    'WHERE',
    'WITH',

    # VARS AND OPERATORS
    'NUMBER',
    'NAME',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'COMMA',
)


# SQL COMMANDS
t_ALTER = r'ALTER'
t_TABLE = r'TABLE'
t_AND = r'AND'
t_AS = r'AS'
t_AVG = r'AVG'
t_BETWEEN = r'BETWEEN'
t_CASE = r'CASE'
t_COUNT = r'COUNT'
t_CREATE = r'CREATE'
t_DELETE = r'DELETE'
t_GROUP = r'GROUP'
t_BY = r'BY'
t_HAVING = r'HAVING'
t_INNER = r'INNER'
t_JOIN = r'JOIN'
t_INSERT = r'INSERT'
t_IS = r'IS'
t_NOT = r'NOT'
t_NULL = r'NULL'
t_LIKE = r'LIKE'
t_LIMIT = r'LIMIT'
t_MAX = r'MAX'
t_MIN = r'MIN'
t_OR = r'OR'
t_ORDER = r'ORDER'
t_OUTER = r'OUTER'
t_ROUND = r'ROUND'
t_SELECT = r'SELECT'
t_DISTINCT = r'DISTINCT'
t_SUM = r'SUM'
t_UPDATE = r'UPDATE'
t_WHERE = r'WHERE'
t_WITH = r'WITH'

# VARS AND OPERATORS
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','


def t_NUMBER(t):
    r'\d+(.\d+)?'
    t.value = float(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


while True:
    expression = input("Expression to evaluate: ")
    lexer.input(expression)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
