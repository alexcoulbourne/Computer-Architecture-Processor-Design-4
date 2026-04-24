# imports the ALU, Register, and Control classes to be used within the Datapath class
from alu import ALU
from register import Register
from control import Control

# this class models the processor's datapath, which integrates the ALU, Register file, and Control unit to execute instructions
class Datapath:
    # initialize the datapath with a register file, ALU, and control unit
    def __init__(self):
        self.register = Register()
        self.alu = ALU()
        self.control = Control()
    # load the initial input values of A, B, C, and D (from main.py) into registers t0 - t3
    def load_inputs(self, A, B, C, D):
        self.register.write("t0", A, True)
        self.register.write("t1", B, True)
        self.register.write("t2", C, True)
        self.register.write("t3", D, True)
    # execute a single instruction by using functions from Control, ALU, and Register classes
    # also print the current cycle, instruction, control signals, register reads, ALU result, and register state
    def execute_instruction(self, instruction, cycle):
        print(f"\nCycle {cycle}")
        print(f"Instruction: {instruction.opcode} {instruction.rd}, {instruction.rs1}, {instruction.rs2}")
        control = self.control.decode(instruction)
        read_data_1 = self.register.read(instruction.rs1)
        read_data_2 = self.register.read(instruction.rs2)
        alu_result = self.alu.execute(read_data_1, read_data_2, control["ALUOp"], control["InvertA"], control["InvertB"])
        self.register.write(instruction.rd, alu_result, control["RegWrite"])
        print("Control Signals:", control)
        print(f"Read {instruction.rs1} = {read_data_1}")
        print(f"Read {instruction.rs2} = {read_data_2}")
        print(f"ALU Result = {alu_result}")
        print("Registers:", self.register.display())
    # run a program consisting of multiple instructions and return the final output Y to register t0
    def run_program(self, program):
        for cycle, instruction in enumerate(program, start=1):
            self.execute_instruction(instruction, cycle)
        return self.register.read("t0")