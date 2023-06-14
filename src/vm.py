# vm.py - Proof of concept for a stack based virtual machine.

class VirtualMachine:
  def __init__(self, max_stack_size=pow(2, 16)):
    self.stack = []
    self.program = []
    self.pc = 0
  
  def push(self, value):
    self.stack.append(value)
  
  def pop(self):
    return self.stack.pop()

  def load_program(self, program):
    self.program = program
    self.pc = 0 

  def add(self):
    self.stack.append(self.pop() + self.pop())

  def sub(self):
    self.stack.append(self.pop() - self.pop())
  
  def mul(self):
    self.stack.append(self.pop() * self.pop())
  
  def div(self):
    self.stack.append(self.pop() / self.pop())

  def print(self):
    print(self.stack)

  def number(self, opcode):
    self.stack.append(opcode - 16)

  def run(self):
    while self.pc < len(self.program):
      opcode = self.program[self.pc].value
      if opcode == 0:
        self.add()
      elif opcode == 1:
        self.sub()
      elif opcode == 2:
        self.mul()
      elif opcode == 3:
        self.div()
      elif opcode == 4:
        self.print()
      if opcode >= 16:
        self.number(opcode)
      self.pc += 1