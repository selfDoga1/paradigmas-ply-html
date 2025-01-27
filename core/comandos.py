from .utils import *


html_output = []
css_output = []


def p_comandos(p):
    """ comandos : comando
                | comandos comando """


def p_comando_tela(p):
    """ comando : CRIAR TELA NUMERO X NUMERO"""
    largura, altura = p[3], p[5]
    html_output.append(f'''
        <body style="width: {altura}px; height: {largura}px;" class="tela">
    '''.strip())


def p_comando_texto(p):
    """ comando : ADICIONAR TEXTO STRING """
    texto = p[3]
    html_output.append(f'''
        <p id={convert_to_id(texto)}>{texto.replace('"', "")}</p>
    ''')

def p_comando_colorir_texto(p):
    """comando : COLORIR TEXTO STRING PARA STRING """
    texto = p[3]
    cor = p[5]
    css_output.append("#{id}{{color: {cor}}}".format(id=convert_to_id(texto), cor=clear(cor)))


def p_comando_container(p):
    """ comando : CRIAR CONTAINER NUMERO X NUMERO"""
    html_output.append(f'''
        <div>
    ''')


def p_fechar_container(p):
    """ comando : FECHAR_CONTAINER"""
    html_output.append(f'''
        </div>
    ''')


def p_error(p):
    print(f"Erro sintático: {p.value if p else 'final inesperado'}")
