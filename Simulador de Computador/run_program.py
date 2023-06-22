import ufc2x as cpu
import sys
import memory as mem
import clock as clk
import disk as disk

disk.read(str(sys.argv[1]))

clk.start([cpu])

print("Resultado:", mem.read_word(3))

print("Resto:", mem.read_word(4))

