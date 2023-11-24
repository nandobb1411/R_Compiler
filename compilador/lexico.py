# lexer.py
from ply import lex

# Definição dos tokens
tokens = (
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'PRINT',  
)

# Expressões regulares para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PRINT = r'print'



# Token de ignorar
t_ignore = ' \t\n'

# Gestão de tokens
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^\\"]|\\.)*"|(\d+)'
    if t.value[0] == '"':
        t.value = t.value[1:-1]  # Remover as aspas
    else:
        t.value = int(t.value)   # Converter para numeros
    return t



# Função de erro
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Analisador léxico
lexer = lex.lex()