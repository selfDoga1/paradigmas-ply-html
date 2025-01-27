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

