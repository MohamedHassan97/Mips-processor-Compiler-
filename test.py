from data import instruction_table, register_table
from binHex_converter import hex2bin

file = open('testfile.txt', 'r')
lines = file.readlines()
print(lines)
file.close()

input_lines = ["add $s1,$s2,$s3", "beq $s1,$s2,3"]
instruction_array = []
lable_dict =[]
input2 = ["2000 :j 2004 "]


def parse(lines):
    for line_i, line in enumerate(lines):
        if ':' in line:
            lable = line.split(':')[0]
            lable_dict[line_i] = lable
            line = line[3:]
            # print(lable_dict)
        instruction = line.strip().replace(' ', ',', 1).replace(')', '').replace('(', ',').replace('\n', '')
        instruction = instruction.replace(' ', '').split(',')
        instruction_array.append(instruction)
    return instruction_array


parse(lines)
print(instruction_array)


# the excution  every_list means every line but cut into  list elemnts

for every_list in instruction_array:
    if str(every_list[0]) == "add":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("add").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(hex2bin(register_table.get(every_list[3]), 5)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + shamt + str(
            hex2bin(instruction_table.get("add").get("func"), 6)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "and":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("and").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(hex2bin(register_table.get(every_list[3]), 5)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + shamt + str(
            hex2bin(instruction_table.get("and").get("func"), 6)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "or":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("or").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(hex2bin(register_table.get(every_list[3]), 5)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + shamt + str(
            hex2bin(instruction_table.get("or").get("func"), 6)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "sub":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("sub").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(hex2bin(register_table.get(every_list[3]), 5)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + shamt + str(
            hex2bin(instruction_table.get("sub").get("func"), 6)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "slt":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("slt").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(hex2bin(register_table.get(every_list[3]), 5)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + shamt + str(
            hex2bin(instruction_table.get("slt").get("func"), 6)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "nor":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("nor").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(hex2bin(register_table.get(every_list[3]), 5)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + shamt + str(
            hex2bin(instruction_table.get("nor").get("func"), 6)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "sll":
        shamt = str(hex2bin(register_table.get(every_list[3]), 5))
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("sll").get("opcode"), 6)) + "00000" + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + shamt + str(
            hex2bin(instruction_table.get("sll").get("func"), 6)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "srl":
        shamt = str(hex2bin(register_table.get(every_list[3]), 5))
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("srl").get("opcode"), 6)) + "00000" + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + shamt + str(
            hex2bin(instruction_table.get("srl").get("func"), 6)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "beq":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("beq").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + str(hex2bin(register_table.get(every_list[2]), 5)) + str(
            hex2bin(every_list[3], 16)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "bne":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("bne").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + str(hex2bin(register_table.get(every_list[2]), 5)) + str(
            hex2bin(every_list[3], 16)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "addi":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("addi").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(hex2bin(register_table.get(every_list[1]), 5)) + str(
            hex2bin(every_list[3], 16)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "ori":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("ori").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(hex2bin(register_table.get(every_list[1]), 5)) + str(
            hex2bin(every_list[3], 16)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "andi":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("andi").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[2]), 5)) + str(hex2bin(register_table.get(every_list[1]), 5)) + str(
            hex2bin(every_list[3], 16)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "lw":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("lw").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[3]), 5)) + str(hex2bin(register_table.get(every_list[1]), 5)) + str(
            hex2bin(every_list[2], 16)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "sw":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("sw").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[3]), 5)) + str(hex2bin(register_table.get(every_list[1]), 5)) + str(
            hex2bin(every_list[2], 16)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "jr":
        shamt = "00000"
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("jr").get("opcode"), 6)) + str(
            hex2bin(register_table.get(every_list[1]), 5)) + "00000" + "00000" + shamt + str(
            hex2bin(instruction_table.get("jr").get("func"), 6)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "j":
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("j").get("opcode"), 6)) + str(hex2bin(every_list[1], 26)) + "\n")
        Mc_file.close()

    elif str(every_list[0]) == "jal":
        Mc_file = open("output.txt", "a")
        Mc_file.write(str(hex2bin(instruction_table.get("jal").get("opcode"), 6)) + str(hex2bin(every_list[1], 26)) + "\n")
        Mc_file.close()