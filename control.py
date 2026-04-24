# this class models the processor's control unit, which decodes instruction fields and generates control signals
class Control:
    # decode an instruction field, including AND, OR, or an error
    def decode(self, instruction):
        if instruction.opcode == "AND":
            alu_op = "AND"
        elif instruction.opcode == "OR":
            alu_op = "OR"
        # throw an error if an unsupported instruction is given
        else:
            raise ValueError(f"Unsupported instruction: {instruction.opcode}")
        # generate control signals based on the decoded instruction
        control_signals = {
            "ALUOp": alu_op,
            "RegWrite": True,
            "InvertA": instruction.invert_rs1,
            "InvertB": instruction.invert_rs2,
        }
        return control_signals