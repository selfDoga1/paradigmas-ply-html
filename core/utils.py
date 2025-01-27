def gerar_arquivos(html_output, css_output):
    with open('output/output.html', 'w') as html_file:
        html_file.write('<!DOCTYPE html>\n<html>\n<head>\n<link rel="stylesheet" href="style.css">\n</head>\n')
        html_file.write('\n'.join(html_output))
        html_file.write('\n</body>\n</html>')

    with open('output/style.css', 'w') as css_file:
        css_file.write('\n'.join(css_output))

    print("Arquivos 'output.html' e 'style.css' gerados com sucesso!")


def convert_to_id(text):
    return text.replace('"', '').replace(' ', '_').lower()


def clear(text):
    return text.replace('"', '')


alinhamentos = {
    'centro': 'center',
    'inicio': 'start',
    'final': 'end',
    'uniforme': 'space-between',
    'igual': 'space-around',
    'destribuido': 'space-evenly',
    'estendido': 'stretch',
    'baseline': 'baseline',
}

cores = {
    'preto': '#4F4F4F',           # Cinza escuro suave
    'branco': '#F8F8F8',          # Branco quase puro
    'vermelho': '#FFB3B3',        # Vermelho suave
    'verde': '#B3E6B3',           # Verde suave
    'azul': '#B3D9FF',            # Azul suave
    'amarelo': '#FFF9B3',         # Amarelo suave
    'laranja': '#FFD1B3',         # Laranja suave
    'rosa': '#FFCCE5',            # Rosa suave
    'roxo': '#D1B3FF',            # Roxo suave
    'cinza': '#D9D9D9',           # Cinza claro suave
    'marrom': '#D9B3B3',          # Marrom suave
    'ciano': '#B3FFFF',           # Ciano suave
    'lima': '#CCFFCC',            # Verde limão suave
    'prata': '#E5E5E5',           # Prata suave
    'dourado': '#FFECB3',         # Dourado suave
    'azul-claro': '#CCE5FF',      # Azul-claro suave
    'verde-claro': '#D9F2D9',     # Verde-claro suave
    'vermelho-escuro': '#D99898', # Vermelho escuro suave
    'azul-marinho': '#99B3CC',    # Azul-marinho suave
    'magenta': '#FFB3FF'          # Magenta suave
}

entradas = {
    'texto': 'text',               # Campo de texto padrão
    'senha': 'password',           # Campo para senhas (caracteres mascarados)
    'email': 'email',              # Campo para endereços de e-mail (validação incluída)
    'numero': 'number',            # Campo para números (com controles de incremento/decremento)
    'telefone': 'tel',             # Campo para números de telefone
    'url': 'url',                  # Campo para URLs (validação incluída)
    'data': 'date',                # Campo para seleção de data (com calendário)
    'hora': 'time',                # Campo para seleção de hora
    'busca': 'search',             # Campo para buscas (estilizado para pesquisas)
    'arquivo': 'file',             # Campo para upload de arquivos
    'checkbox': 'checkbox',        # Caixa de seleção (marcar/desmarcar)
    'radio': 'radio',              # Botão de seleção (escolha única em grupo)
    'cor': 'color',                # Seleção de cor (aparece uma paleta)
    'intervalo': 'range',          # Controle deslizante para intervalos de valores
    'oculto': 'hidden',            # Campo oculto (não visível, mas enviado com o formulário)
    'submit': 'submit',            # Botão para enviar o formulário
    'reset': 'reset',              # Botão para resetar os campos do formulário
    'imagem': 'image',             # Botão de envio com imagem
    'botao': 'button',              # Botão genérico (não envia formulário)
}

direcoes_config = {
    'verticalmente': 'column',
    'horizontalmente': 'row',
}

sombras_config = {
    "leve": "0px 2px 4px rgba(0, 0, 0, 0.1)",
    "moderada": "0px 4px 8px rgba(0, 0, 0, 0.15)",
    "agressiva": "0px 6px 12px rgba(0, 0, 0, 0.25)"
}

arredondar_config = {
    "levemente": "4px",
    "moderadamente": "8px",
    "agressivamente": "16px"
}




