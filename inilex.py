import ply.lex as lex

tokens = (
    'LBRACKET',
    'RBRACKET',
    'EQUALS',
    'STRING',
)

states = (
    ('afterlbracket', 'inclusive'),
    ('afterequals', 'inclusive'),
)


def t_LBRACKET(t):
    r'\['
    t.lexer.begin('afterlbracket')
    return t


def t_RBRACKET(t):
    r'\]'
    return t


def t_EQUALS(t):
    r'='
    t.lexer.begin('afterequals')
    return t


def t_STRING(t):
    r'[^\s=\[\]\#;][^=\[\]\#\n]*[^\s=\[\]\#;]?'
    return t


def t_afterlbracket_STRING(t):
    r'[^\s\]\#;]?.*[^\s\]\#;]'
    t.lexer.begin('INITIAL')
    return t


def t_afterequals_STRING(t):
    r'[^\s\#;]?.*[^\s\#;]'
    t.lexer.begin('INITIAL')
    return t


def t_COMMENT(t):
    r'[\#;].*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.begin('INITIAL')
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal caracter '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
if __name__ == "__main__":
    lex.runmain(lexer)
