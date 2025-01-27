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

# ================================== TEXTO =====================================

def p_comando_texto(p):
    """ comando : ADICIONAR TEXTO STRING """

    texto = p[3]
    html_output.append(f'''
        <p id={convert_to_id(texto)}>{clear(texto)}</p>
    '''.strip())

def p_comando_colorir_texto(p):
    """comando : COLORIR TEXTO STRING PARA STRING """

    texto = p[3]
    cor = clear(p[5])
    cor = cores.get(cor, cor)
    css_output.append("#{id}{{color: {cor}}}".format(id=convert_to_id(texto), cor=clear(cor)))


# ================================== CONTAINER =====================================


def p_comando_abrir_container(p):
    """ comando : ABRIR CONTAINER STRING NUMERO X NUMERO"""

    id, largura, altura = p[3], p[4], p[6]
    html_output.append(f'''
        <div style="display:flex; width: {altura}px; height: {largura}px;" class="container" id={id}>
    '''.strip())


def p_comando_fechar_container(p):
    """ comando : FECHAR CONTAINER """
    html_output.append("</div>")


def p_alinhar_items_container(p):
    """ comando : ALINHAR ITEMS CONTAINER STRING STRING """

    container_id, alinhamento = p[4], p[5]

    container_id = clear(container_id)
    alinhamento = alinhamentos[clear(alinhamento)]

    css_output.append("#{id}{{align-items: {alinhamento}}}".format(id=container_id, alinhamento=alinhamento))


def p_justificar_items_container(p):
    """ comando : JUSTIFICAR ITEMS CONTAINER STRING STRING """

    container_id, alinhamento = p[4], p[5]

    container_id = clear(container_id)
    alinhamento = alinhamentos[clear(alinhamento)]

    css_output.append("#{id}{{justify-content: {alinhamento}}}".format(id=container_id, alinhamento=alinhamento))


def p_comando_colorir_container(p):
    """comando : COLORIR CONTAINER STRING PARA STRING """

    container_id = clear(p[3])
    cor = clear(p[5])
    cor = cores.get(cor, cor)
    css_output.append("#{id}{{background-color: {cor}}}".format(id=container_id, cor=cor))


def p_error(p):
    print(f"Erro sintático: {p.value if p else 'final inesperado'}")
