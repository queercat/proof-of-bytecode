# This is the main file for the project. It will be used to test the functionality of the project.
from parse import Parser
from vm import VirtualMachine
from lexer import Lexer
import instructions as ins

def main():
  lexer = Lexer("var x = 3; var y = 3; var z = x + y;")
  parser = Parser(lexer.scan())
  parser.parse()

if __name__ == "__main__":
  main()