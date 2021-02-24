# LFA-tema1
Tema LFA 2020-2021 Interpretor Glypho
Patru Diana-Georgiana, 332CA

    Implementarea temei am realizat-o in Python. Pentru a avea codul cat mai bine structurat, am realizat in main.py logica programului urmand ca in utils.py sa realizez cat o functie pentru fiecare operatie specifica instructiunii.
    Astfel:
    1) TRATAREA ERORILOR
      - pentru fiecare linie citita din fisierul de intrare, verific daca lungimea este multiplu de 4, iar in caz contrar constat o eroare. Acelasi lucru se intampla si in cazul in care nu exista un numar egal de paranteze inchise si deschise sau nu exista o corespondenta intre ele (prin functia check_instruction())
    2) LOGICA PROGRAMULUI
      - Pentru fiecare grupare de 4 simboluri din fisierul de intrare, codific si asociez o instruciune corespunzatoare (prin functiile codification() si instructions()) ce este adaugata intr-o lista de instructiuni ce urmeaza a fi executate
      - Parcurg fiecare instructiune si o execut
    3) TRATAREA EXCEPTIILOR
      - Se face in cadrul fiecarei functie ce executa cate o operatie iar executia programului se va oprii si va afisa o exceptie cu un mesaj corespunzator ce contine pozitia instructiunii unde s-a produs eroarea.
    4) LOGICA L-BRACE ~ R-BRACE
      - Intrucat celelalte operatii ce sunt execuate in tema sunt destul de  straight-forward (si am detaliat si in comentarii in cod), am decis sa explic doar logica parantezelor deoarece pentru mine a parut cea mai complicata:
          a) L-brace
            * daca in varful stivei nu este 0, retin intr-o alta lista, pozitia instructiunii curente din lista de instructiuni initiale
            * daca in varful stivei este 0, setez o variabila pe True, astfel ca urmatoarele instructiuni nu se vor mai executa pana la r_brace
          b) R-brace:
            * daca lista cu pozitiile parantezelor deschise nu e goala, inseamna ca am intalnit o paranteza inchisa corespunzatoarea ulimei pozitii adaugate in lista
            * calculez intervalul dintre paranteza deschisa corespunzatoare parantezei inchide curente si execut instructiunile din interior atata timp cat in varful stivei nu e 0
            * la final, setez variabila ignore_instr pe False, astfel ca urmatoarele instructiuni sa se poata executa
    5) IMPLEMENTAREA IN ALTA BAZA
      - In momentul citirii de la intrarea standard a unui numar intr-o alta baza fata de 10, prin functia int(value, base), realize conversia valorii value din baza citita in baza 10 si o adaug in stiva
      - In momentul afisarii unui element din stiva la iesirea standard, realizez conversia inversa prin functia dec_to_base(), care realizeaza  conversia din baza 10 in baza care este citita in linia de comanda si printez numarul
        Precizez ca functia dec_to_base() este implementata pe site-ul urmator:
    https://www.codespeedy.com/inter-convert-decimal-and-any-base-using-python/
