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
    'AJUDA',
    'ITEM',
    'ITENS',
    'JUSTIFICAR',
    'ENTRADA',
    'TIPO',
    'COM',
    'ROTULO',
    'ORGANIZAR',
    'APLICAR',
    'SOMBRA',
    'NO',
    'ARRENDONDAR',
    'BOTAO',
    'E',
    'COR',
    'CABECALHO',
    'SECUNDARIO',
    'LISTA',
    'LISTAGEM',
    'ORDENADA',
    'IMAGEM',
    'COMO',
    'FUNDO'
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
t_ADICIONAR         = r'ADICIONAR'
t_COLORIR           = r'COLORIR'
t_PARA              = r'PARA'
t_ALINHAR           = r'ALINHAR'
t_AJUDA             = r'AJUDA'
t_ITEM              = r'ITEM'
t_ITENS             = r'ITENS'
t_JUSTIFICAR        = r'JUSTIFICAR'
t_ENTRADA           = r'ENTRADA'
t_TIPO              = r'TIPO'
t_COM               = r'COM'
t_ROTULO            = r'ROTULO'
t_ORGANIZAR         = r'ORGANIZAR'
t_APLICAR           = r'APLICAR'
t_NO                = r'NO'
t_SOMBRA            = r'SOMBRA'
t_ARRENDONDAR       = r'ARRENDONDAR'
t_BOTAO             = r'BOTAO'
t_E                 = r'E'
t_COR               = r'COR'
t_CABECALHO         = r'CABECALHO'
t_SECUNDARIO         = r'SECUNDARIO'
t_LISTA             = r'LISTA'
t_ORDENADA          = r'ORDENADA'
t_IMAGEM            = r'IMAGEM'
t_FUNDO             = r'FUNDO'
t_COMO              = r'COMO'

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remove as aspas
    return t

def t_LISTAGEM(t):
    r'\[[\wÀ-ÿ]+(?:\s*,\s*[\wÀ-ÿ]+)*\]'
    t.value = str(t.value)
    t.value = t.value.replace('[', '')
    t.value = t.value.replace(']', '')
    t.value = map(lambda i: i.strip(), t.value.split(','))
    return t

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