class Token:
  position = -1
  lexeme = "UNDEFINED"
  type = "UNDEFINED"

  def __init__(self, position, lexeme, type):
    self.position = position
    self.lexeme = lexeme
    self.type = type

  def __str__(self) -> str:
    return f"Token({self.position}, {self.lexeme}, {self.type})"