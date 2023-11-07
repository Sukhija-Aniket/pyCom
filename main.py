import sys
from pylex import MyLexer
from pyparse import MyParser

data  = sys.stdin.read()
myLexer = MyLexer()
lexer = myLexer.build()
parser = MyParser(myLexer)
parser.build(lexer)
parser.test(data)