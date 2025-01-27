tokens = (
    'ADICIONAR',
    'CRIAR',
    'TELA',
    'X',
    'CONTAINER',
    'FECHAR',
    'ABRIR',
    'NUMERO',
    'TEXTO',
    'STRING',
    'TAMANHO',
    'COLORIR',
    'PARA',
    'ALINHAR',
    'ITEMS',
    'JUSTIFICAR',
)

t_ignore = ' \t'

t_CRIAR             = r'CRIAR'
t_TELA              = r'TELA'
t_X                 = r'X'
t_TAMANHO           = r'TAMANHO'
t_CONTAINER         = r'CONTAINER'
t_FECHAR            = r'FECHAR'
t_ABRIR             = r'ABRIR'
t_TEXTO             = r'TEXTO'
t_STRING            = r'\".*?\"'
t_ADICIONAR         = r'ADICIONAR'
t_COLORIR           = r'COLORIR'
t_PARA              = r'PARA'
t_ALINHAR           = r'ALINHAR'
t_ITEMS             = r'ITEMS'
t_JUSTIFICAR        = r'JUSTIFICAR'


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