import ply.lex as lex

tokens = (
    'BRO_SAY', 'IDK', 'ZIGOTO', 'BENDEW', 'WHAT_IS_IT', 'SHEEEEEEEESH', 'YES', 'IM_A_HACKER',
    'SUUUUUUUUUUU', 'PLS_ADD', 'PLS_SUB', 'IM_BATMAN', 'YAY', 'ENDINSTR', 'HELP', 'LICENSE',
    'I_HATE_THIS_LANG', 'NUM', 'STR',
)

t_ZIGOTO = r'zigoto'
t_BENDEW = r'bendew'
t_WHAT_IS_IT = r'what_is_it'
t_SHEEEEEEEESH = r'sheeeeeeesh'
t_IM_A_HACKER = r'i_am_a_hacker'
t_SUUUUUUUUUUU = r'suuuuuuuuuu'
t_PLS_ADD = r'pls_add'
t_PLS_SUB = r'pls_sub'
t_IM_BATMAN = r'i_am_batman'
t_YAY = r'yay'
t_ENDINSTR = r'.,'
t_HELP = r'help_me_!!!'
t_LICENSE = r'license'
t_I_HATE_THIS_LANG = r'i_hate_this_language'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STR(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_IDK(t):
    r'<-idk->\+\+\+.*'
    pass

def t_BRO_SAY(t):
    r'bro_say'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Illegal penguin on the cat.")
    t.lexer.skip(1)
    
lexer = lex.lex()