def convert(inst):

    dest = {
    "null": "000",  # If no destination is specified
    "M": "001",     # Store the result in the memory location addressed by A
    "D": "010",     # Store the result in the D register
    "MD": "011",    # Store the result in both the D register and the memory location addressed by A
    "A": "100",     # Store the result in the memory location addressed by A (same as M)
    "AM": "101",    # Store the result in the memory location addressed by A and in the A register
    "AD": "110",    # Store the result in the D register and in the memory location addressed by A
    "AMD": "111"    # Store the result in the D register, the A register, and the memory location addressed by A
    }

    jump = {
    "null": "000",  # If no jump condition is specified
    "JGT": "001",   # If the result of the computation is greater than 0
    "JEQ": "010",   # If the result of the computation is equal to 0
    "JGE": "011",   # If the result of the computation is greater than or equal to 0
    "JLT": "100",   # If the result of the computation is less than 0
    "JNE": "101",   # If the result of the computation is not equal to 0
    "JLE": "110",   # If the result of the computation is less than or equal to 0
    "JMP": "111"    # Jump unconditionally
    }

    comp = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M":   "1110000",
    "!M":  "1110001",
    "-M":  "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101",
    }

    if ('=' in inst and ';' in inst):
        x=inst.split("=",";")
        return '111'+ comp[x[1]] + dest[inst[0]] + jump[x[2]]
    elif ('=' in inst):
        x=inst.split("=")
        return '111' + comp[x[1]] + dest[inst[0]] + jump['null']
    elif(';' in inst):
        x=inst.split(";")
        return '111' + comp[x[0]] + dest["null"] + jump[x[1]]