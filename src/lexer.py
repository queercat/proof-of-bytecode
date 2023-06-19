from tok import Token
import re

def isNumber(c):
  regex = re.compile("[0-9]")
  return regex.match(c) is not None

def isAlphaNumeric(c):
  regex = re.compile("[a-zA-Z0-9]")  
  return regex.match(c) is not None

class Lexer:
  def __init__(self, source):
    self.tokens = []      
    self.start = 0
    self.current = 0
    self.line = 1
    self.source = source

    self.keywords = [
      "var"
    ]

  def get_position(self):
    return (self.start, self.current, self.line)
  
  def match(self, text):
    if text in self.keywords:
      return text
    return 

  def scan(self):
    while self.current < len(self.source):
      self.start = self.current
      c = self.source[self.current]

      if c in ["\t", " "]:
        self.current += 1
        continue
      
      elif isNumber(c):
        while self.current < len(self.source) and isNumber(c = self.source[self.current]): 
          self.current += 1
        lexeme = self.source[self.start:self.current]
        self.tokens.append(Token(self.get_position(), float(lexeme), "Number"))
        continue

      elif isAlphaNumeric(c):
        while self.current < len(self.source) and isAlphaNumeric(c = self.source[self.current]):
          self.current += 1
        type = "Identifier"
        lexeme = self.source[self.start:self.current]

        match = self.match(lexeme)

        if match is not None:
          type = match[0].upper() + match[1:] 

        self.tokens.append(Token(self.get_position(), lexeme, type))
        continue

      elif c in ["+", "-", "/", "*"]:
        lexeme = c
        type = "Operator"
        self.current += 1
        self.tokens.append(Token(self.get_position(), lexeme, type))
        continue

      elif c == ";":
        lexeme = c
        type = "End-Statement"
        self.current += 1
        self.tokens.append(Token(self.get_position(), lexeme, type))
        continue

      elif c == "=":
        lexeme = c
        type = "Equals"
        self.current += 1
        self.tokens.append(Token(self.get_position(), lexeme, type))
        continue


    EOF = Token((self.current, self.line), "EOF", "EOF")
    self.tokens.append(EOF)

    return self.tokens