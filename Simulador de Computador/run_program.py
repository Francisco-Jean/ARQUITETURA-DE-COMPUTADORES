import ufc2x as cpu
import sys
import memory as mem
import clock as clk
import disk as disk

disk.read(str(sys.argv[1]))


print("\n")
clk.start([cpu])

print("Resultado:", mem.read_word(3))

print("Caso esteja rodando a divisão, o resto é: ", mem.read_word(1))

print("\n")