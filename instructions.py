class Opcode:
  def __init__(self):
    self.type = None
    self.name = None

class Add (Opcode):
  def __init__(self):
    self.type = 'add'
    self.name = 'add'