import ufc2x as cpu
import memory as mem
import clock as clk

mem.write_word(100, 0)
mem.write_word(50, 2)

mem.write_byte(1, 2)
mem.write_byte(2, 100)

mem.write_byte(3, 48)


mem.write_byte(4, 10)
mem.write_byte(5, 120)

mem.write_byte(6, 255)

clk.start([cpu])

print(mem.read_word(120))
# print(mem.read_word(151))
