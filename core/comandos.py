from .constants import *
from .utils import *


html_output = []
css_output = []


def p_comandos(p):
    """ comandos : comando
                | comandos comando """

def p_comando_tela(p):
    """ comando : CRIAR TELA NUMERO X NUMERO
                | CRIAR TELA
    """

    suffix = 'px'
    print(len(p))
    if len(p) > 3:
        largura, altura = p[3], p[5]
    else:
        largura, altura = 100, 100
        suffix = '%'

    html_output.append(f'''
        <body style="width: {altura}{suffix}; height: {largura}{suffix}; justify-items: center;" class="tela">
    '''.strip())

# ================================== TEXTO =====================================

def p_comando_texto(p):
    """ comando : ADICIONAR TEXTO STRING """

    texto = p[3]
    html_output.append(f'''
        <p id={convert_to_id(texto)}>{texto}</p>
    '''.strip())

def p_comando_colorir_texto(p):
    """comando : COLORIR TEXTO STRING PARA STRING """

    texto = p[3]
    cor = p[5]
    cor = cores.get(cor, cor)
    css_output.append("#{id}{{color: {cor}}}".format(id=convert_to_id(texto), cor=cor))

def p_adicionar_cabecalho(p):
    """ comando : ADICIONAR CABECALHO COM TEXTO STRING """
    texto = p[5]
    html_output.append(f'''
            <h1 id={convert_to_id(texto)}>{texto}</h1>
        '''.strip())

def p_adicionar_cabecalho_secundario(p):
    """ comando : ADICIONAR CABECALHO SECUNDARIO COM TEXTO STRING """

    texto = p[6]
    html_output.append(f'''
        <h3 id={convert_to_id(texto)}>{texto}</h3>
    '''.strip())

def p_comando_adicionar_ajuda(p):
    """ comando : ADICIONAR AJUDA PARA ITEM STRING COM TEXTO STRING """
    elemento_id = p[5]
    tooltip_texto = p[8]
    css_output.append(f"#{convert_to_id(elemento_id)}::after {{ content: '{tooltip_texto}'; position: absolute; visibility: hidden; background-color: black; color: white; padding: 5px; border-radius: 4px; }}")
    css_output.append(f"#{convert_to_id(elemento_id)}:hover::after {{ visibility: visible; }}")

# ================================== CONTAINER =====================================

def p_comando_abrir_container(p):
    """ comando : ABRIR CONTAINER STRING NUMERO X NUMERO
                | ABRIR CONTAINER STRING
    """

    id = p[3]
    suffix = 'px'
    if len(p) > 4:
        largura, altura = p[4], p[6]
    else:
        largura, altura = 100, 100
        suffix = '%'

    html_output.append(f'''
        <div style="display:flex; width: {altura}{suffix}; height: {largura}{suffix}; padding:15px;" class="container" id={id}>
    '''.strip())

def p_comando_fechar_container(p):
    """ comando : FECHAR CONTAINER """
    html_output.append("</div>")


def p_comando_adicionar_imagem_fundo(p):
    """ comando : ADICIONAR IMAGEM STRING COMO FUNDO NO CONTAINER STRING """

    imagem_fundo = p[3]
    container_id = p[8]
    
    css_output.append(f"#{convert_to_id(container_id)} {{ background-image: url('{imagem_fundo}'); background-size: cover; }}")


def p_alinhar_items(p):
    """ comando : ALINHAR ITENS STRING STRING """

    container_id, alinhamento = p[3], p[4]

    container_id = container_id
    alinhamento = alinhamentos[alinhamento]

    css_output.append("#{id}{{align-items: {alinhamento}}}".format(id=container_id, alinhamento=alinhamento))

def p_justificar_items(p):
    """ comando : JUSTIFICAR ITENS STRING STRING """

    container_id, alinhamento = p[3], p[4]

    container_id = container_id
    alinhamento = alinhamentos[alinhamento]

    css_output.append("#{id}{{justify-content: {alinhamento}}}".format(id=container_id, alinhamento=alinhamento))

def p_organizar(p):
    """ comando : ORGANIZAR STRING STRING """
    container_id, direcao = p[2], p[3]
    container_id = container_id
    direcao = direcoes_config.get(direcao, direcao)
    css_output.append("#{id}{{flex-direction: {direcao}}}".format(id=container_id, direcao=direcao))

def p_arredondar(p):
    """ comando : ARREDONDAR STRING STRING """

    container_id, intensidade = p[2], p[3]
    container_id = container_id
    intensidade = arredondar_config.get(intensidade, intensidade)  # Busca no dicionário
    css_output.append("#{id}{{border-radius: {raio}}}".format(id=container_id, raio=intensidade))

def p_comando_adicionar_botao(p):
    """ comando : ADICIONAR BOTAO COM ROTULO STRING"""

    rotulo = p[5]
    rotulo = rotulo

    html_output.append(f'''
        <button id="{convert_to_id(rotulo)}">{rotulo}</button>        
    '''.strip())

# ================================== FORM =====================================

def p_comando_adicionar_entrada(p):
    """ comando : ADICIONAR ENTRADA TIPO STRING COM ROTULO STRING """

    tipo_entrada = entradas.get(p[4])
    rotulo = p[7]
    rotulo_id = convert_to_id(rotulo)
    gap = "5px"
    width = "100%"

    flex_direction = "column"
    if tipo_entrada == "checkbox":
        flex_direction = "row"
        gap = "10px"
        width = ""

    html_output.append(f"""
        <label id={rotulo_id} style="display: flex; flex-direction: {flex_direction}; padding: 10px 0 10px 0; width:{width}; gap: {gap};">{rotulo}<input type="{tipo_entrada}"/></label>
    """.strip())

# ================================== OUTROS =====================================

def p_aplicar_sombra(p):
    """ comando : APLICAR SOMBRA STRING NO STRING """
    container_id, intensidade = p[5], p[3]
    container_id = container_id
    intensidade = sombras_config.get(intensidade, intensidade)
    css_output.append("#{id}{{box-shadow: {sombra}}}".format(id=container_id, sombra=intensidade))

def p_comando_colorir(p):
    """comando : COLORIR STRING PARA STRING """

    container_id = p[2]
    cor = p[4]
    cor = cores.get(cor, cor)
    css_output.append("#{id}{{background-color: {cor}}}".format(id=container_id, cor=cor))

def p_comando_criar_lista(p):
    """ comando : CRIAR LISTA STRING COM ITENS LISTAGEM """
    titulo = p[3]
    items = p[6]
    html_output.append(gerar_lista_html(titulo, items, tipo_lista="ul"))

def p_comando_criar_lista_ordenada(p):
    """ comando : CRIAR LISTA ORDENADA STRING COM ITENS LISTAGEM """
    titulo = p[4]
    items = p[7]
    html_output.append(gerar_lista_html(titulo, items, tipo_lista="ol"))


def p_error(p):
    print(f"Erro sintático: {p.value if p else 'final inesperado'}")
