def gerar_arquivos(html_output, css_output):
    with open('output/output.html', 'w') as html_file:
        html_file.write('<!DOCTYPE html>\n<html>\n<head>\n<link rel="stylesheet" href="style.css">\n</head>\n')
        html_file.write('\n'.join(html_output))
        if '<body>' in html_output:
            html_file.write('\n</body>\n</html>')

    with open('output/style.css', 'w') as css_file:
        css_file.write('\n'.join(css_output))

    print("Arquivos 'output.html' e 'style.css' gerados com sucesso!")


def convert_to_id(text):
    return text.replace('"', '').replace(' ', '_').lower()


def clear(text):
    return text.replace('"', '')


def gerar_lista_html(titulo, items, tipo_lista="ul"):
    """Função auxiliar para gerar HTML de listas"""
    items_html = ''.join([f'\n\t\t<li>{li}</li>' for li in items]) + '\n'
    lista_tag = "ul" if tipo_lista == "ul" else "ol"  # Determina se é <ul> ou <ol>
    return f"""<div>\n\t<h1 id="{convert_to_id(titulo)}">{titulo}</h1>\n\t<{lista_tag}>{items_html}\t</{lista_tag}>\n<div>"""
