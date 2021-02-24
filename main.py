import sys
from utils import *


def main():
    instruction = ""
    base = 10
    # daca se da si o alta baza in care sunt reprezentate numerele
    if len(sys.argv) == 3:
        base = int(sys.argv[2])
    file1 = open(sys.argv[1], 'r')
    lines = file1.readlines()
    # pentru fiecare linie citita din fisierul de intrare
    for line in lines:
        # daca lungimea liniei nu e multiplu de 4, este eroare
        if len(line) % 4 != 0:
            sys.stderr.write("Error:" + str(len(line) // 4))
            sys.exit(-1)
        else:
            for i in range(len(line) // 4):
                # codifica fiecare grup de 4 simboluri
                word = codification(line, i)
                # asociaza o instructiune corespunzatoare
                inst = instructions(word)
                # o adauga in lista de instructiuni ce urmeaza a fi executate
                instruction = instruction + inst
    define_inst(instruction, base)
    # daca instruciunea nu are un numar egal de paranteze care
    # se deschid si inchis, eroare
    if check_instruction(instruction) != -1:
        sys.stderr.write("Error:" + str(check_instruction(instruction)))
        sys.exit(-1)
    for i in range(0, len(instruction)):
        try:
            # decodifica fiecare instructiune din lista
            # si o execut
            decoded_instr(instruction[i], i)
        except:
            sys.stderr.write("Exception:" + str(i))
            sys.exit(-2)


if __name__ == "__main__":
    main()
