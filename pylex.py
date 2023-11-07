from ply import lex as lex

class MyLexer(object):

    def __init__(self):

        self.reserved = {
        'if': 'IF',
        'elif': 'ELIF',
        'else' : 'ELSE',
        'then': 'THEN',
        'while' : 'WHILE',
        'boolean' : 'BOOLEAN',
        'import' : 'IMPORT',
        'from' : 'FROM',
        'as' : 'AS',
        'class' : 'CLASS',
        'interface' : 'INTERFACE',
        'extends' : 'EXTENDS',
        'true' : 'TRUE',
        'false' : 'FALSE',
        'in': 'IN',
        'int' : 'INT',
        'float' : 'FLOAT',
        'main' : 'MAIN',
        'new': 'NEW',
        'public' : 'PUBLIC',
        'return' : 'RETURN',
        'static': 'STATIC',
        'string': 'STRING',
        'this': 'THIS',
        'print': 'PRINT',
        'void': 'VOID',
        'Object': 'OBJECT' 
        }

        self.tokens = [
            'INTEGER_LITERAL',
            'IDENTIFIER',
            'COMMENT',
            'MULTILINE_COMMENT',
            'LE',
            'GE',
            'ARROW',
            'NE',
            'AND',
            'OR',
            'XOR',
            'PLUS',
            'MINUS',
            'MULT',
            'DIVIDE',
            'LPAREN',
            'RPAREN',
            'LBRACE',
            'RBRACE',
            'LSQPAREN',
            'RSQPAREN',
            'AT',
            'COMMA',
            'SEMICOLON',
            'COLON',
            'DOT',
            'QUOTE',
            'DOUBLEQUOTE',
            'EQUAL',
            'LESS',
            'GREATER',
            'BITOR',
            'BITAND',
            'EXCLAMATION_MARK',
            'TILDE',
            'NOT',
            'QUESTION',
            'DOLLAR',
            'SLASH',
            'FLOAT_LITERAL',
            'STRING_LITERAL'
        ] + list(self.reserved.values())

        self.t_LE = r'<='
        self.t_GE = r'>='
        self.t_ARROW = r'->'
        self.t_NE = r'!='
        self.t_AND = r'and'
        self.t_OR = r'OR'
        self.t_XOR = r'\^'
        self.t_NOT = r'NOT'
        self.t_PLUS = r'\+'
        self.t_MINUS = r'-'
        self.t_MULT = r'\*'
        self.t_DIVIDE = r'/'
        self.t_LPAREN = r'\('
        self.t_RPAREN = r'\)'
        self.t_LBRACE = r'\{'
        self.t_RBRACE = r'\}'
        self.t_LSQPAREN = r'\['
        self.t_RSQPAREN = r'\]'
        self.t_AT = r'@'
        self.t_COMMA = r','
        self.t_SEMICOLON = r';'
        self.t_COLON = r':'
        self.t_DOT = r'\.'
        self.t_QUOTE = r'\''
        self.t_DOUBLEQUOTE = r'\"'
        self.t_EQUAL = r'='
        self.t_LESS = r'<'
        self.t_GREATER = r'>'
        self.t_BITOR = r'\|'
        self.t_BITAND = r'&'
        self.t_EXCLAMATION_MARK = r'!'
        self.t_TILDE = r'~'
        self.t_QUESTION = r'\?'
        self.t_DOLLAR = r'\$'
        self.t_SLASH = r'\\'
        
        self.t_ignore = " \t\r\n" # write something here

    def t_INTEGER_LITERAL(self, t):
        r'\d+'
        t.value = int(t.value)    
        return t

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
        return t

    def t_COMMENT(self, t):
        r'\#.*'
        t.lexer.lineno += t.value.count('\n')
        # No return value. Token discarded

    def t_MULTILINE_COMMENT(self, t):
        r"'''\s*.*?\s*'''"
        t.lexer.lineno += t.value.count('\n')

    def t_FLOAT_LITERAL(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_STRING_LITERAL(self, t):
        r'\"([^\\\n]|(\\.))*?\"'
        t.value = t.value[1:-1]
        return t
    
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    
    # Building the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

    def test(self, data):
        if not self.lexer:
            self.build()
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
            print(tok.type, tok.value, tok.lineno, tok.lexpos)

'''To use Lexer Independently, uncomment the below code'''
# mylexer = MyLexer()
# lexer = mylexer.build()

# with open('testcases_input/c.py', 'r') as file:
#     data = file.read() 

# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
