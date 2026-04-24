# this class models the processor's ALU, which takes two inputs and performs AND, OR, or an inversion on either input based on control signals
class ALU:
    # execute an ALU operation based on the given control signals
    def execute(self, a, b, alu_op, invert_a=False, invert_b=False):
        if invert_a:
            a = 1 - a
        if invert_b:
            b = 1 - b
        if alu_op == 'AND':
            return a & b
        elif alu_op == 'OR':
            return a | b
        ## throw an error if an unsupported operation is given
        else:
            raise ValueError(f"Unsupported ALU operation: {alu_op}")