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
