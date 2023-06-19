class Parser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.current = 0

  def peek(self):
    return self.tokens[self.current + 1]

  def advance(self):
    self.current += 1
    return self.tokens[self.current]
  
  def error(self, message, location):
    print(message, "at line", location[2])

  def expected(self, message, garbage, location):
    print(message, "but found ~>", garbage, "<~", "at line", location[2])
    exit(1)
  
  # variable declaration statement, expects (var identifier = statement).
  def variable(self):
    t = self.advance() 

    if t.type != "Identifier":
      self.expected("expected variable identifier", t.lexeme, t.position)

    name = t.lexeme

    t = self.advance()

    if t.type != "Equals":
      self.expected("expected variable assignment", t.lexeme, t.position)

    t = self.advance()

    self.statement()

  # statements are handled here... can be.
  # x + 3 - 4 * 3 + y / 3;
  def statement(self):
    pass

  def parse(self):
    t = self.tokens[self.current]

    while (t.type != "EOF"):
      if (t.type == "Var"): 
        self.variable()