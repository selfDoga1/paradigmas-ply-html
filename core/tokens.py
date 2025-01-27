tokens = (
    'TELA', 'CABECALHO', 'BOTAO', 'IMAGEM', 'TEXTO',
    'NUMERO', 'STRING', 'TAMANHO', 'ALINHAMENTO'
)

t_ignore = ' \t'

t_TELA = r'tela'
t_CABECALHO = r'cabecalho'
t_BOTAO = r'botao'
t_IMAGEM = r'imagem'
t_TEXTO = r'texto'

t_STRING = r'\".*?\"'
t_TAMANHO = r'grande|medio|pequeno'
t_ALINHAMENTO = r'centralizado|esquerdo|direito'


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Erro léxico: Caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)