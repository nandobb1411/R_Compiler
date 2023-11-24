# sintatico.py
from ply import yacc
from lexico import tokens


symbol_table = {}
# Print
def p_statement_print(p):
    'statement : PRINT expression'
    print(p[2])


# Aritimeticas
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_string(p):
    'factor : STRING'
    p[0] = p[1]

def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Erro para sintaxe
def p_error(p):
    print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")

# Build the parser
parser = yacc.yacc()

# Add a start rule to resolve the unreachable symbol warning
# Função start para resolver unreachable symbol warning
def p_start(p):
    'start : statement'
    pass