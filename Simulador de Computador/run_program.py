import ufc2x as cpu
import sys
import memory as mem
import clock as clk
import disk as disk

print("Antes: ", mem.read_word(1))

disk.read(str(sys.argv[1]))

clk.start([cpu])

print("Depois: ", mem.read_word(3))
print("Depois: ", mem.read_word(4))

