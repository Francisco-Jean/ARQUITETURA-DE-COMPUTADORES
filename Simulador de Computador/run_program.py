import ufc2x as cpu
import sys
import memory as mem
import clock as clk
import disk as disk

disk.read(str(sys.argv[1]))

print("")

# for x in range(40):
#     print(f"{x} : {mem.read_byte(x)}")

    
clk.start([cpu])

if sys.argv[1] == "fatorial.bin":
    print("Resultado:", mem.read_word(2))

if sys.argv[1] == "divisao.bin":
    print("Resultado:", mem.read_word(3))
    print("Resto:", mem.read_word(4))

if sys.argv[1] == "csw.bin":

    print("Resultado:", mem.read_word(4))

    if mem.read_word(2) == mem.read_word(3) and mem.read_word(4) == 0:
        print("Valor do A :", mem.read_word(1))
        print("Valor do B :", mem.read_word(2))
        print("Valor do C alterado para :", mem.read_word(3))
    elif mem.read_word(1) == mem.read_word(3):
        print("Valor do A alterado para :", mem.read_word(1))
        print("Valor do B :", mem.read_word(2))
        print("Valor do C :", mem.read_word(3))

print("")