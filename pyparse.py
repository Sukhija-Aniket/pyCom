from pylex import MyLexer
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
        '''Statement : FromImport
                    | DotImport
                    | NormalImport
                    | OtherStatement'''
        if p[1] == 'OtherStatement':
            pass
        else:
            p[0] = p[1]

    def p_FromImport(self, p):
        'FromImport : FROM DotIdentifier IMPORT ImportList'
        
        p[0] = ''
        temp = ''
        if p[4] == '':
            p[0] = p[2]
            pass
        
        for x in p[4]:
            if x == ',':
                p[0] += p[2] + '.' + temp + '\n'
                temp = ''
            else:
                temp += x

        if temp != '':
            p[0] += p[2] + '.' + temp
            temp = ''


    def p_DotImport(self, p):
        'DotImport : FROM DOT IMPORT ImportList'
        
        p[0]=''
        temp = ''
        for x in p[4]:
            if x == ',':
                p[0] += temp + '\n'
                temp = ''
            else:
                temp += x

        if temp != '':
            p[0] += temp
            temp = ''
        
    def p_NormalImport(self, p):
        'NormalImport : IMPORT ImportList'
        
        p[0]=''
        temp = ''
        for x in p[2]:
            if x == ',':
                p[0] += temp + '\n'
                temp = ''
            else:
                temp += x
            
        if temp != '':
            p[0] += temp
            temp = ''
    
    def p_ImportList(self, p):
        '''ImportList : ImportList COMMA ImportIdentifier
                      | ImportIdentifier'''
        if len(p) == 4:
            p[0] = p[1] + ',' + p[3]
        else:
            p[0] = p[1]

    def p_ImportIdentifier(self, p):
        '''ImportIdentifier : DotIdentifier RestIdentifier
                            | Asterisk'''
        p[0] = p[1] 

    def p_RestIdentifier(self, p):
        '''RestIdentifier : AS IDENTIFIER
                          | empty'''
        p[0] = ''
        

    def p_DotIdentifier(self, p):
        '''DotIdentifier : DotIdentifier RemainingIdentifier
                         | IDENTIFIER'''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    # def p_RemainingIdentifierList(self, p):
    #     '''RemainingIdentifierList : RemainingIdentifierList RemainingIdentifier
    #                             | empty'''
    #     if len(p) == 3:
    #         p[0] = p[1] + p[2]
    #     else:
    #         p[0] = ''

    def p_RemainingIdentifier(self, p):
        '''RemainingIdentifier : DOT IDENTIFIER
                            | DOT Asterisk'''
        if p[2] == 'Asterisk':
            p[0] = ''
        else:
            p[0] = p[1] + p[2]

    def p_Asterisk(self, p):
        'Asterisk : MULT'
        p[0] = ''

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
                    | AS
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
                    | ELIF
                    | EXCLAMATION_MARK
                    | IN
                    | TILDE
                    | XOR
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
                    | COMMENT
                    | ARROW
                    | MULTILINE_COMMENT
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
        print("Syntax error", self, p)

    def yacc(
        debug: bool = True
    ):
        pass
        
    def build(self, lexer):
        self.parser = yacc.yacc(module=self, start='Goal', debug=True)
        self.lexer = lexer

    def test(self, data):
        result = self.parser.parse(data,lexer=self.lexer)
        print(result)

'''To operate parser independently, just Uncomment the below code'''
# TODO: write code to use parser independantly.