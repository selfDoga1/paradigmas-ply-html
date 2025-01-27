html_output = []
css_output = []


def p_comandos(p):
    '''comandos : comando
                | comandos comando'''


def p_comando_tela(p):
    'comando : TELA NUMERO NUMERO'
    largura, altura = p[2], p[3]
    html_output.append(f'<div class="tela"></div>')
    css_output.append(f'.tela {{ width: {largura}px; height: {altura}px; margin: 0 auto; }}')


def p_comando_cabecalho(p):
    'comando : CABECALHO STRING TAMANHO ALINHAMENTO'
    texto, tamanho, alinhamento = p[2][1:-1], p[3], p[4]
    tamanhos = {'grande': '32px', 'medio': '24px', 'pequeno': '16px'}
    alinhamentos = {'centralizado': 'center', 'esquerdo': 'left', 'direito': 'right'}
    html_output.append(f'<h1 class="cabecalho">{texto}</h1>')
    css_output.append(f'.cabecalho {{ font-size: {tamanhos[tamanho]}; text-align: {alinhamentos[alinhamento]}; }}')


def p_comando_botao(p):
    'comando : BOTAO STRING NUMERO NUMERO'
    texto, largura, altura = p[2][1:-1], p[3], p[4]
    html_output.append(f'<button class="botao">{texto}</button>')
    css_output.append(f'.botao {{ width: {largura}px; height: {altura}px; }}')


def p_comando_imagem(p):
    'comando : IMAGEM STRING NUMERO NUMERO'
    src, largura, altura = p[2][1:-1], p[3], p[4]
    html_output.append(f'<img class="imagem" src="{src}" alt="Imagem" />')
    css_output.append(f'.imagem {{ width: {largura}px; height: {altura}px; }}')


def p_comando_texto(p):
    'comando : TEXTO STRING TAMANHO ALINHAMENTO'
    texto, tamanho, alinhamento = p[2][1:-1], p[3], p[4]
    tamanhos = {'grande': '20px', 'medio': '16px', 'pequeno': '12px'}
    alinhamentos = {'centralizado': 'center', 'esquerdo': 'left', 'direito': 'right'}
    html_output.append(f'<p class="texto">{texto}</p>')
    css_output.append(f'.texto {{ font-size: {tamanhos[tamanho]}; text-align: {alinhamentos[alinhamento]}; }}')


def p_error(p):
    print(f"Erro sintático: {p.value if p else 'final inesperado'}")