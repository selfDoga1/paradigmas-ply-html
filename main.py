import ply.lex as lex
import ply.yacc as yacc

from core.tokens import *
from core.comandos import *
from core.utils import gerar_arquivos


lexer = lex.lex()
parser = yacc.yacc()


if __name__ == "__main__":
    arquivo_entrada = 'input.txt'
    with open(arquivo_entrada, 'r') as file:
        codigo = file.read()

    parser.parse(codigo)
    gerar_arquivos(html_output, css_output)
