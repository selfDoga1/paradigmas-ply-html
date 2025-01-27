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
    css_output.append("#{id}{{color: {cor}}}".format(id=convert_to_id(texto), cor=cor))

def p_adicionar_cabecalho(p):
    """ comando : ADICIONAR CABECALHO COM TEXTO STRING """
    texto = p[5]
    html_output.append(f'''
            <h1 id={convert_to_id(texto)}>{clear(texto)}</h1>
        '''.strip())

# ================================== CONTAINER =====================================

def p_comando_abrir_container(p):
    """ comando : ABRIR CONTAINER STRING NUMERO X NUMERO"""

    id, largura, altura = p[3], p[4], p[6]
    html_output.append(f'''
        <div style="display:flex; width: {altura}px; height: {largura}px; padding:5px;" class="container" id={id}>
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

def p_organizar_container(p):
    """ comando : ORGANIZAR CONTAINER STRING STRING """
    container_id, direcao = p[3], p[4]
    container_id = clear(container_id)
    direcao = direcoes_config.get(clear(direcao), direcao)
    css_output.append("#{id}{{flex-direction: {direcao}}}".format(id=container_id, direcao=direcao))

def p_arredondar_container(p):
    """ comando : ARRENDONDAR CONTAINER STRING STRING """

    container_id, intensidade = p[3], p[4]
    container_id = clear(container_id)
    intensidade = arredondar_config.get(clear(intensidade), intensidade)  # Busca no dicionário
    css_output.append("#{id}{{border-radius: {raio}}}".format(id=container_id, raio=intensidade))

def p_comando_adicionar_botao(p):
    """ comando : ADICIONAR BOTAO COM ROTULO STRING"""

    rotulo = p[5]
    rotulo = clear(rotulo)

    html_output.append(f'''
        <button>{rotulo}</button>        
    '''.strip())

# ================================== FORM =====================================

def p_comando_adicionar_entrada(p):
    """ comando : ADICIONAR ENTRADA TIPO STRING COM ROTULO STRING """

    tipo_entrada = entradas.get(clear(p[4]))
    rotulo = clear(p[7])
    rotulo_id = convert_to_id(rotulo)

    html_output.append(f"""
        <label id={rotulo_id} style="display: flex; flex-direction: column; padding: 10px 0 10px 0; width:100%">
            {rotulo}
            <input type="{tipo_entrada}"/>
        </label>
    """.strip())

# ================================== OUTROS =====================================

def p_aplicar_sombra(p):
    """ comando : APLICAR SOMBRA STRING NO STRING """
    container_id, intensidade = p[5], p[3]
    container_id = clear(container_id)
    intensidade = sombras_config.get(clear(intensidade), intensidade)
    css_output.append("#{id}{{box-shadow: {sombra}}}".format(id=container_id, sombra=intensidade))

def p_comando_colorir(p):
    """comando : COLORIR STRING PARA STRING """

    container_id = clear(p[2])
    cor = clear(p[4])
    cor = cores.get(cor, cor)
    css_output.append("#{id}{{background-color: {cor}}}".format(id=container_id, cor=cor))

def p_error(p):
    print(f"Erro sintático: {p.value if p else 'final inesperado'}")
