# compilador.py
from lexico import lexer
from sintatico import parser

def compile_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            parser.parse(data, lexer=lexer)
            # print(data)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except SyntaxError as e:
        print(e)

compile_file(r'C:\Users\Samsung\OneDrive\Área de Trabalho\VsCode_Projects\R\compilador\compiler_file.txt')
