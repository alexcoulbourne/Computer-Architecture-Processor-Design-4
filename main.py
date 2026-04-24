# imports the Instruction and Datapath classes to be used within the main function
from instruction import Instruction
from datapath import Datapath

# this is the main function, initializing the processor, loading inputs, defining the program, and running it to get the final output Y
def main():
    # these inputs will yield True (1) for the equation, change if you want to test other cases    
    A = 1
    B = 1
    C = 0
    D = 0
    # set up the datapath and loads the initial input values into registers t0 - t3
    processor = Datapath()
    processor.load_inputs(A, B, C, D)
    # print initial register states before running the program
    print("Initial Register State:")
    print(processor.register.display())
    # creates a program consisting of three Instruction objects with the specified opcodes, rd, rs1, rs2, and inversion flags
    # the program implements the boolean equation Y = (A & B) | ((~C) & D); change the instructions if you want to test other equations
    program = [
        Instruction("AND", "t4", "t0", "t1"),  # t4 = A AND B
        Instruction("AND", "t6", "t2", "t3", invert_rs1=True),  # t6 = (~C) AND D
        Instruction("OR", "t0", "t4", "t6"),  # t0 = t4 OR t6
    ]
    # runs the program via the Datapath's run_program method and prints the final output Y (stored in t0)
    final_output = processor.run_program(program)
    print("\nFinal Output:")
    print(f"Y = {final_output}")
    # calculate the expected output using the given boolean equation and prints it for verification; change if you want to test other cases
    expected = (A & B) | ((1 - C) & D)
    print(f"Expected Y = {expected}")
    # checks whether the test passed :) or failed :( by comparing the final output with the calculated expected output
    if final_output == expected:
        print("Test Passed!")
    else:
        print("Test Failed!")
if __name__ == "__main__":
    main()