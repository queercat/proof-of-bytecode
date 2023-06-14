# Abstract class for opcodes.
class Opcode:
  def __init__(self):
    self.name = None
    self.value = -1

class Add (Opcode):
  def __init__(self):
    self.name = 'Add'
    self.value = 0

class Sub (Opcode):
  def __init__(self):
    self.name = 'Sub'
    self.value = 1

class Mul (Opcode):
  def __init__(self):
    self.name = 'Mul'
    self.value = 2

class Div (Opcode):
  def __init__(self):
    self.name = 'Div'
    self.value = 3

class Print (Opcode):
  def __init__(self):
    self.name = 'Print'
    self.value = 4

class Number (Opcode):
  def __init__(self, value):
    self.name = 'Number'
    self.value = value + 16

# An opcodes is 4 bits long, so we can have 16 opcodes.