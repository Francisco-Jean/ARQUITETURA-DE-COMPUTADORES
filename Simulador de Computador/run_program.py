import ufc2x as cpu
import sys
import memory as mem
import clock as clk
import disk as disk

disk.read(str(sys.argv[1]))


print("")
clk.start([cpu])

print("Resultado:", mem.read_word(1))
if mem.read_word(2) == cpu.MDR:
    print("Resto: ", mem.read_word(2))

print("")