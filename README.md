# Single Cycle Processor Design
## This project simulates a single-cycle processor in Python, supporting AND, OR, and NOT instructions (via ALU input inversion). Each component is implemented as a separate file, run via `main.py`.

### Target Computation:
Y = A·B + C'·D

### Register Mapping
- t0 = A
- t1 = B
- t2 = C
- t3 = D
- t4 = A & B
- t5 = ~C
- t6 = (~C) & D
- t0 = t4 | t6 (final output Y)

### Program:  
**and t4, t0, t1**  
**and t6, t5, t3**  
**or t0, t4, t6**

### How to Run:
Download the project, navigate to the directory, and run `main.py`.

## Output and Expected Functionality:
`main.py` prints several values to terminal. Firstly, the initial register states are printed. Then three cycles are performed; one for each line of instruction. Every step is printed. Finally, the final output is printed, alongside the expected output (calculated as a single Boolean expression).
