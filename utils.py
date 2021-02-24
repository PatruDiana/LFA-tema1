import sys

stack = []
stack_parentheses = []
ignore_inst = False
instruc = ""
b = 10


# realizeaza o copie a listei de instructiuni
def define_inst(instruction, base):
    global instruc
    instruc = instruction
    global b
    b = base


# codifica fiecare grup de 4 simboluri
def codification(line, i):
    y = 0
    dict = {}
    word = ""
    for x in line[i * 4: i * 4 + 4]:
        if x not in dict.keys():
            dict[x] = y
            y = y + 1
        word = word + str(dict[x])
    return word


# asociaza o instructiune corespunzatoare
def instructions(word):
    switcher = {
        '0000': 'n',
        '0001': 'i',
        '0010': '>',
        '0011': '\\',
        '0012': '1',
        '0100': '<',
        '0101': 'd',
        '0102': '+',
        '0110': '[',
        '0111': 'o',
        '0112': '*',
        '0120': 'e',
        '0121': '-',
        '0122': '!',
        '0123': ']',
    }
    return switcher.get(word, 'nothing')


def function_nop():
    pass


def function_input():
    if not ignore_inst:
        # citeste o valoare de la input
        value = input()
        # o transforma din baza corespunzatoare in baza zecimala
        new_val = int(value, b)
        # adauga in stiva noua valoare
        stack.append(new_val)


# extrage un element din varful stivei si il pune la coada
def function_rot():
    # daca instructiunea se poate executa
    if not ignore_inst:
        if stack:
            v1 = stack.pop()
            stack.insert(0, v1)
        else:
            raise Exception


# interschimba elementele din varful stivei
def function_swap():
    # daca instructiunea se poate executa
    if not ignore_inst:
        if len(stack) >= 2:
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1)
            stack.append(v2)
        else:
            raise Exception


# va pune in varful stivei un nou element cu valoarea 1
def function_push():
    # daca instructiunea se poate executa
    if not ignore_inst:
        stack.append(1)


# scoate un element de la coada stivei si il va pune in varf
def function_rrot():
    # daca instructiunea se poate executa
    if not ignore_inst:
        if stack:
            v1 = stack.pop(0)
            stack.append(v1)
        else:
            raise Exception


# duplica elementul din varful stivei
def function_dup():
    # daca instructiunea se poate executa
    if not ignore_inst:
        if stack:
            stack.append(stack[-1])
        else:
            raise Exception


# aduna 2 elemente din varful stivei punand suma in locul lor
def function_add():
    # daca instructiunea se poate executa
    if not ignore_inst:
        if len(stack) >= 2:
            v1 = stack.pop()
            v2 = stack.pop()
            s = int(v1) + int(v2)
            stack.append(s)
        else:
            raise Exception


def function_l_brace(index):
    if stack:
        # daca varful stivei nu este 0
        if stack[-1] != 0:
            # retin intr-o alta lista, pozitia instructiunii curente
            # din lista de instructiuni initiale
            stack_parentheses.append(index)
        else:
            # setez o variabila pe True, astfel ca urmatoarele
            # instructiuni nu se vor mai executa pana la
            # r_brace
            global ignore_inst
            ignore_inst = True
    else:
        raise Exception


# scoare elementul din varful stivei si il printeaza
def function_output():
    if not ignore_inst:
        if stack:
            if b == 10:
                print(stack.pop())
            else:
                print(dec_to_base(stack.pop(), b))
        else:
            raise Exception


# functie de convertire a unui numar din baza base in baza zecimala
def dec_to_base(num, base):
    base_num = ""
    while num > 0:
        dig = int(num % base)
        if dig < 10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A') + dig - 10)
        num //= base
    base_num = base_num[::-1]
    return base_num


# inmulteste ultimele 2 numere din varful stivei punand rezultatul
# in varful stivei
def function_multiply():
    if not ignore_inst:
        if len(stack) >= 2:
            v1 = stack.pop()
            v2 = stack.pop()
            s = int(v1) * int(v2)
            stack.append(s)
        else:
            raise Exception


# scoate ultimele 4 elemente din stiva, creand o noua instructiune
# si o executa
def function_execute():
    if not ignore_inst:
        if len(stack) >= 4:
            list_exec = []
            for x in range(4):
                list_exec.append(int(stack.pop()))
            # codifica lista de 4 numere
            word = codification(list_exec, 0)
            # asociaza o instructiune corespunzatoare
            inst = instructions(word)
            # executa instructiunea
            decoded_instr(inst)
        else:
            raise Exception


# inlocuieste varful stivei cu negatul lui
def function_negate():
    if not ignore_inst:
        if stack:
            v1 = stack.pop()
            stack.append(-(int(v1)))
        else:
            raise Exception


# scoate un element din varful stivei
def function_pop():
    if not ignore_inst:
        if stack:
            stack.pop()
        else:
            raise Exception


def function_r_brace(index):
    # daca lista cu pozitiile parantezelor deschise nu e goala
    if stack_parentheses:
        v1 = stack_parentheses.pop()
        v2 = index + 1
        if stack:
            while stack[-1] != 0:
                # calculez intervalul dintre paranteza deschisa
                # corespunzatoare parantezei inchide curente
                # si execut instructiunile din interior
                # atata timp cat in varful stivei nu e 0
                for x in range(v1 + 1, v2 - 1):
                    decoded_instr(instruc[x], x)
            global ignore_inst
        else:
            raise Exception

    ignore_inst = False


# executa o operatie specifica in functie de instructiunea curenta
def decoded_instr(i, index=0):
    if i == 'n':
        function_nop()
    elif i == 'i':
        function_input()
    elif i == '>':
        function_rot()
    elif i == '\\':
        function_swap()
    elif i == '1':
        function_push()
    elif i == '<':
        function_rrot()
    elif i == 'd':
        function_dup()
    elif i == '+':
        function_add()
    elif i == '[':
        function_l_brace(index)
    elif i == 'o':
        function_output()
    elif i == '*':
        function_multiply()
    elif i == 'e':
        function_execute()
    elif i == '-':
        function_negate()
    elif i == '!':
        function_pop()
    elif i == ']':
        function_r_brace(index)
    else:
        return lambda: print("invalid function")


# verifica daca numarul de paranteze inchise si cele de paranteze
# deschise sunt egale
def check_instruction(instruction):
    p = []
    for x in range(len(instruction)):
        if instruction[x] == '[':
            p.append(instruction[x])
        if instruction[x] == ']':
            if not p:
                return x
            p.pop()

    if p:
        return len(instruction)

    return -1
