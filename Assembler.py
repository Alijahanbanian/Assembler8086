# Ali Jahanbanian
# Code Assembler 8086
# Python Version: 3.10.2
import re

op = ["ADD", "OR", "AND", "SUB", "ADC"]
opcode = ["000000", "000010", "001000", "001010", "000100"]
reg_name = ["al-ax-eax", "cl-cx-ecx", "dl-dx-edx", "bl-bx-ebx", "ah-sp-esp", "ch-bp-ebp", "dh-si-esi", "bh-di-edi"]
mod = ["11", "00"]
reg_value = ["000", "001", "010", "011", "100", "101", "110", "111"]
eight_bits = ["al", "cl", "dl", "bl", "ah", "ch", "dh", "bh"]
d = ['0', '1', '0']
s = ['1', '0']
REG = []
RM = []
list2 = ['[h]', '']
#----------------------- Input Code:
code_8086 = str(input("Enter Assembly Code:\n"))
#----------------------- Split The Code And Put It In The List:
list_code_8086 = re.split(r"[\b\W\b]+", code_8086)
#----------------------- Split The Code For Find Index Memory:
list_code_8086_2 = re.split(r"[ |,]+", code_8086)
#----------------------- Checks If It Has Memory Or Not:
Is_MEM_2_REG = int(bool(re.search(r"\[([a-z]+)\]", code_8086)))
list_code_8086_2.append(list2[Is_MEM_2_REG])
#----------------------- Regulare Expression Memory:
ss = re.compile(r'\[([a-z]+)\]')
#----------------------- Find Index Memory:
li = [1, list_code_8086_2.index(str(list(filter(ss.match, list_code_8086_2)))[2:-2])]
#----------------------- Regulare Expression first Register:
r1 = re.compile(".*" + list_code_8086[1].lower() + ".*")
#----------------------- Regulare Expression second Register Or Memory:
r2 = re.compile(".*" + list_code_8086[2].lower() + ".*")
#----------------------- Calculate first Register:
Value_1 = reg_value[reg_name.index(str(list(filter(r2.match, reg_name)))[2:-2])]
#----------------------- Calculate second Register Or Memory:
Value_2 = reg_value[reg_name.index(str(list(filter(r1.match, reg_name)))[2:-2])]
#-----------------------
which_d = d[li[Is_MEM_2_REG]-1]
#-----------------------
li2 = [Value_1 + Value_2, Value_2 + Value_1]
#----------------------- Calculate Binary Code:
binary = opcode[op.index(list_code_8086[0].upper())] + which_d + s[int(list_code_8086[1] in eight_bits)] + mod[Is_MEM_2_REG] + li2[int(which_d)]
#----------------------- Calculate Hex Code:
hexadecimal = f'{int(binary,2):X}'

print("binary: " + binary)
print("hexadecimal: " + hexadecimal)

