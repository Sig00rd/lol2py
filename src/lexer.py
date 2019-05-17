from rply import LexerGenerator
from ply import lex

tokens = [
    'HAI',
    'KTHXBAI',
    'IM IN YR',
    'WILE',
    'IM OUTTA YR',
    'I HAS A',
    'ITZ',
    'OBTW',  #
    'TLDR',  #
    'VISIBLE',
    'MKAY?',
    'O RLY?',
    'YA RLY',
    'OIC',
    'MEBBE',
    'NO WAI',
    'GIMMEH',
    'HOW DUZ I',
    'YR',
    'AN YR',
    'IF YOU SAY SO',
    'R',
    'BOTH SAEM',
    'DIFFRINT',
    'AN',
    'BOTH OF',
    'EITHER OF',
    'BIGGR OF',
    'SMALLR OF',
    'SUM OF',  #
    'DIFF OF',
    'PRODUKT OF',
    'QUOSHUNT OF',
    'MOD OF',
    'MAEK',
    'ALL OF',
    'ANY OF',
    'NOT',
    'WIN',
    'FAIL',
    'NOOB',
    'NUMBER',
    'FLOAT_NUMBER',
    'STRING',
    'NEWLINE',  #
    'COMMA', #
    'NUMBR',
    'NUMBAR',
    'YARN',
    'TROOF',#
    'BTW'  #
]

t_SUM_OF = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_TLDR = r'\TLDR'
t_COMMA = r'\,'


# line comment
def t_btw(t):
    r'\BTW.*'
    pass
    # No return value. Token discarded


# multiline comment
def t_obtw(t):
    r'\OBTW[^TLDR]*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# ignored characters
t_ignore = '\t'

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
HAI 1.2
I HAS A NAME
VISIBLE "NAME::"!
GIMMEH NAME
VISIBLE "tutorialsPoint " NAME "!"
KTHXBYE
 '''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
