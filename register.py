## this class models the processor's register file, containing the required registers t0 - t6
class Register:
    # initialize registers t0 - t6 with 0
    def __init__(self):
        self.registers = {
            "t0": 0,
            "t1": 0,
            "t2": 0,
            "t3": 0,
            "t4": 0,
            "t5": 0,
            "t6": 0,
        }
    # return the value stored in the specified register
    def read(self, reg_name):
        return self.registers[reg_name]
    # write a value to the specified register if reg_write is True
    # this models the RegWrite control signal
    def write(self, reg_name, value, reg_write):
        if reg_write == True:
            self.registers[reg_name] = value
    # return the current register state as a dictionary for printing
    def display(self):
        return dict(self.registers)