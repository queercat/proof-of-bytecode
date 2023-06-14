# This is the main file for the project. It will be used to test the functionality of the project.
from vm import VirtualMachine
import instructions as ins

def main():
  vm = VirtualMachine(max_stack_size=128)
  vm.load_program([
    ins.Number(0),
    ins.Number(1),
    ins.Add(),
    ins.Print(),
  ])
  vm.run()

if __name__ == "__main__":
  main() 