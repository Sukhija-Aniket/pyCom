from pyCom.pylex import MyLexer
import ply.yacc as yacc

class MyParser(object):

    def __init__(self, lexer):
        self.tokens = lexer.tokens

    start = 'Goal'

    def p_Goal(self, p):
        'Goal : Statements'
        p[0] = p[1]

    def p_Statements(self, p):
        '''Statements : Statements Statement
                    | empty'''
        if len(p) == 3:
            if p[2] is None:
                p[0] = p[1]
            else:
                if p[1] == '':
                    p[0] = p[2]
                else:
                    p[0] = p[1] + '\n' +  p[2]
        else:
            p[0] = ''
        

    def p_Statement(self, p):
        '''Statement : PackageDeclaration
                    | StaticImportStatement
                    | ImportStatement
                    | OtherStatement'''
        if p[1] == 'OtherStatement':
            pass
        else:
            p[0] = p[1]

    def p_PackageDeclaration(self, p):
        'PackageDeclaration : PACKAGE DotIdentifier SEMICOLON'
        p[0] = p[2]

    def p_StaticImportStatement(self, p):
        'StaticImportStatement : IMPORT STATIC DotIdentifier SEMICOLON'
        p[0] = p[3]

    def p_ImportStatement(self, p):
        'ImportStatement : IMPORT DotIdentifier SEMICOLON'
        p[0] = p[2] 
        

    def p_DotIdentifier(self, p):
        '''DotIdentifier : IDENTIFIER RemainingIdentifierList'''
        p[0] = p[1] + p[2]
        pass

    def p_RemainingIdentifierList(self, p):
        '''RemainingIdentifierList : RemainingIdentifier RemainingIdentifierList
                                | empty'''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = ''

    def p_RemainingIdentifier(self, p):
        '''RemainingIdentifier : DOT IDENTIFIER
                            | DOT Asterisk'''
        if p[2] == 'Asterisk':
            p[0] = ''
        else:
            p[0] = p[1] + p[2]

    def p_Asterisk(self, p):
        'Asterisk : MULT'
        pass

    def p_OtherStatement(self, p):
        'OtherStatement : OtherTokens'
        pass

    def p_OtherTokens(self, p):
        '''OtherTokens : LPAREN
                    | RPAREN
                    | LSQPAREN
                    | RSQPAREN
                    | LBRACE
                    | RBRACE
                    | AT
                    | QUOTE
                    | SEMICOLON
                    | DOT
                    | COMMA
                    | GREATER
                    | GE
                    | LESS
                    | LE
                    | NE
                    | PLUS
                    | FLOAT
                    | MINUS
                    | MULT
                    | AND
                    | OR
                    | NOT
                    | BOOLEAN
                    | CLASS
                    | INTERFACE
                    | ELSE
                    | EXTENDS
                    | FALSE
                    | IF
                    | WHILE
                    | INT
                    | MAIN
                    | NEW
                    | PUBLIC
                    | RETURN
                    | STATIC
                    | STRING
                    | THIS
                    | TRUE
                    | PRINT
                    | VOID
                    | OBJECT
                    | INTEGER_LITERAL
                    | FLOAT_LITERAL
                    | STRING_LITERAL
                    | IDENTIFIER
                    | EQUAL
                    | DOUBLEQUOTE
                    | DOLLAR
                    | QUESTION
                    | SLASH
                    | THEN
                    | BITAND
                    | BITOR
                    | COLON
                    | DIVIDE'''
        pass

    def p_empty(self, p):
        'empty :'
        pass

    def p_error(self, p):
        print("Syntax error")


    def build(self, lexer):
        self.parser = yacc.yacc(module=self, start='Goal')
        self.lexer = lexer
    def test(self, data):
        result = self.parser.parse(data,lexer=self.lexer)
        print(result)
