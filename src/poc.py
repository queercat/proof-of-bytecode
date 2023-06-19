# This is the main file for the project. It will be used to test the functionality of the project.
from vm import VirtualMachine
from lexer import Lexer
import instructions as ins

def main():
  lexer = Lexer("123abc var")
  tokens = lexer.scan()

  for token in tokens:
    print(token)

if __name__ == "__main__":
  main()