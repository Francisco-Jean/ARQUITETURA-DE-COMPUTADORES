import ufc2x as cpu
import memory as mem
import clock as clk

mem.write_word(50, 2)
mem.write_word(100, 10)

mem.write_byte(1, 2)
mem.write_byte(2, 100)

mem.write_byte(3, 29)
mem.write_byte(4, 50)

mem.write_byte(5, 10)
mem.write_byte(6, 150)

mem.write_byte(7, 36)
mem.write_byte(8, 151)
mem.write_byte(9, 255)

clk.start([cpu])

print(mem.read_word(150))
print(mem.read_word(151))
