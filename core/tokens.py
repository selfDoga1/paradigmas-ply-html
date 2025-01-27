tokens = (
    'ADICIONAR',
    'CRIAR',
    'TELA',
    'X',
    'CONTAINER',
    'FECHAR_CONTAINER',
    'NUMERO',
    'TEXTO',
    'STRING',
    'TAMANHO',
    'COLORIR',
    'PARA',
)

t_ignore = ' \t'

t_CRIAR             = r'CRIAR'
t_TELA              = r'TELA'
t_X                 = r'X'
t_TAMANHO           = r'TAMANHO'
t_CONTAINER         = r'CONTAINER'
t_FECHAR_CONTAINER  = r'FECHAR_CONTAINER'
t_TEXTO             = r'TEXTO'
t_STRING            = r'\".*?\"'
t_ADICIONAR         = r'ADICIONAR'
t_COLORIR           = r'COLORIR'
t_PARA              = r'PARA'


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