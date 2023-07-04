import ufc2x as cpu
import memory as mem
import clock as clk

# FATORIAL
# # X <- X!

# mem.write_word(50, 38)

# mem.write_byte(1, 44)
# mem.write_byte(2, 50)

# mem.write_byte(3, 10)
# mem.write_byte(4, 100)

# mem.write_byte(5, 255)


# DIVISÃO
# X <- X // memory[address]

mem.write_word(50, 20)
mem.write_word(51, 10)

mem.write_byte(1, 26)
mem.write_byte(2, 50)
mem.write_byte(3, 51)

mem.write_byte(4, 10)
mem.write_byte(5, 100)

mem.write_byte(6, 36)
mem.write_byte(7, 101)

mem.write_byte(8, 255)



clk.start([cpu])

print(mem.read_word(100))
print(mem.read_word(101))