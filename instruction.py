# imports dataclass from the dataclasses library to create a simple structure for instructions
from dataclasses import dataclass

@dataclass
# this class models an processor instruction, with its opcode, destination register, source registers, and inversion flags
class Instruction:
    opcode: str
    rd: str
    rs1: str
    rs2: str
    invert_rs1: bool = False
    invert_rs2: bool = False