import ufc2x as cpu
import memory as mem
import clock as clk

mem.write_word(100, 10)
mem.write_word(50, 1)

mem.write_byte(1, 2)
mem.write_byte(2, 50)

mem.write_byte(3, 47)
mem.write_byte(4, 10)
mem.write_byte(5, 100)

mem.write_byte(6, 255)

## X <- X // memory[address]
# mem.write_byte(1, 2)
# mem.write_byte(2, 100)

# mem.write_byte(3, 29)
# mem.write_byte(4, 50)


# mem.write_byte(5, 10)
# mem.write_byte(6, 120)
# mem.write_byte(7, 36)
# mem.write_byte(8, 121)

# mem.write_byte(9, 255)

clk.start([cpu])

print(mem.read_word(100))

if mem.read_word(101) != 0:
    print(mem.read_word(101))