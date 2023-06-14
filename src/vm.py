# vm.py - Proof of concept for a stack based virtual machine.

class VirtualMachine:
  def __init__(self):
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