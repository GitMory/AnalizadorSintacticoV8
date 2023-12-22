import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = (
    'ID', 'NUM', 'REAL',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    'AND', 'OR', 'NOT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET', 'SEMICOLON',
    'EQUALS'
)

# Definición de palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'break': 'BREAK',
    'true': 'TRUE',
    'false': 'FALSE',
    'int': 'INT',
    'float': 'FLOAT',
}

tokens += tuple(reserved.values())

# Expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_EQUALS = r'='

# Ignorar espacios en blanco y comentarios
t_ignore = ' \t\r\f'

#t_ignore_COMMENT = r'\#.*'

t_ignore_SPACE = r'\s+'


def t_COMMENT(t):
    r'\#.*'
    pass

# Definición de funciones para tokens complejos
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica si es una palabra reservada
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Manejo de errores léxicos
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

# Definición de la gramática
def p_programa(p):
    'programa : bloque'
    print("Correcto sintácticamente")

def p_bloque(p):
    'bloque : LBRACE decls instrs RBRACE'

def p_decls(p):
    '''decls : decls decl
             | empty'''

def p_decl(p):
    'decl : tipo ID SEMICOLON'

def p_tipo(p):
    '''tipo : tipo LBRACKET NUM RBRACKET
            | basico'''

def p_basico(p):
    '''basico : INT
                | FLOAT'''

def p_instrs(p):
    '''instrs : instrs stmt
              | empty'''

def p_instr(p):
    '''instr : loc EQUALS bool SEMICOLON
             | IF LPAREN bool RPAREN instr
             | IF LPAREN bool RPAREN instr ELSE instr
             | WHILE LPAREN bool RPAREN instr
             | DO instr WHILE LPAREN bool RPAREN SEMICOLON
             | BREAK SEMICOLON
             | bloque'''

def p_loc(p):
    '''loc : loc LBRACKET bool RBRACKET
           | ID'''

def p_bool(p):
    '''bool : bool OR comb
            | comb'''

def p_comb(p):
    '''comb : comb AND igualdad
            | igualdad'''

def p_igualdad(p):
    '''igualdad : igualdad EQ rel
                | igualdad NE rel
                | rel'''

def p_rel(p):
    '''rel : expr LT expr
           | expr LE expr
           | expr GE expr
           | expr GT expr
           | expr'''

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''

def p_term(p):
    '''term : term TIMES unario
            | term DIVIDE unario
            | unario'''

def p_unario(p):
    '''unario : NOT unario
              | MINUS unario
              | factor'''

def p_factor(p):
    '''factor : LPAREN bool RPAREN
              | loc
              | NUM
              | REAL
              | TRUE
              | FALSE'''

def p_stmt(p):
    '''stmt : loc EQUALS bool SEMICOLON
            | IF LPAREN bool RPAREN instr
            | IF LPAREN bool RPAREN instr ELSE instr
            | WHILE LPAREN bool RPAREN instr
            | DO instr WHILE LPAREN bool RPAREN SEMICOLON
            | BREAK SEMICOLON
            | bloque'''

def p_empty(p):
    'empty :'
    pass

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' en la línea {p.lineno}")
    else:
        print("Error de sintaxis en EOF")

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Prueba del analizador con un ejemplo
codigo_ejemplo = '''
{
    {
    int i; int j; float v; float x; float[100] a;
    while( true ) {
        do i = i+1; while( a[i] < v);
        do j = j-1; while( a[j] > v);
        if( i >= j ) break;
        x = a[i]; a[i] = a[j]; a[j] = x;
    }
    }
}
'''

lexer.input(codigo_ejemplo)
for tok in lexer:
    print(tok)

parser.parse(codigo_ejemplo)
