import memory as memory
from array import array

firmware = array('L', [0]) * 512

# main: PC <- PC + 1; MBR <- read_byte(PC); goto MBR
firmware[0] =   0b000000000_100_00110101_001000_001_001

# HALT
firmware[255] = 0b000000000_000_00000000_000000_000_000

# X = X + memory[address]

## 2: PC <- PC + 1; fetch; goto 3
firmware[2] = 0b000000011_000_00110101_001000_001_001

## 3: MAR <- MBR; read_word(MAR); goto 4
firmware[3] = 0b000000100_000_00010100_100000_010_010

## 4: H <- MDR; goto 5
firmware[4] = 0b000000101_000_00010100_000001_000_000

## 5: X <- H + X; goto 0
firmware[5] = 0b000000000_000_00111100_000100_000_011


# X = X - memory[address]

## 6: PC <- PC + 1; fetch; goto 7
firmware[6] = 0b000000111_000_00110101_001000_001_001

## 7: MAR <- MBR; read; goto 8
firmware[7] = 0b000001000_000_00010100_100000_010_010

## 8: H <- MDR; goto 9
firmware[8] = 0b000001001_000_00010100_000001_000_000

## 9: X <- X - H; goto 0
firmware[9] = 0b000000000_000_00111111_000100_000_011

# memory[address] = X

## 10: PC <- PC + 1; fetch; goto 11
firmware[10] = 0b00001011_000_00110101_001000_001_001

## 11: MAR <- MBR; goto 12
firmware[11] = 0b00001100_000_00010100_100000_000_010

## 12: MDR <- X; write; goto 0
firmware[12] = 0b00000000_000_00010100_010000_100_011

# goto address 

## 13: PC <- PC + 1; fetch; goto 14
firmware[13] = 0b00001110_000_00110101_001000_001_001

## 14: PC <- MBR; fetch; goto MBR
firmware[14] = 0b00000000_100_00010100_001000_001_010

# if X == 0 goto address

## 15: X <- X; if alu = 0 goto 272 else goto 16
firmware[15] = 0b00010000_001_00010100_000100_000_011

## 16: PC <- PC + 1; goto 0
firmware[16] = 0b00000000_000_00110101_001000_000_001

## 272: goto 13
firmware[272]= 0b00001101_000_00000000_000000_000_000


# X <- X // memory[address]
## 26: PC <- PC + 1, fetch; GOTO 27
firmware[26] = 0b000011011_000_00110101_001000_001_001
## 27: MAR <- MBR; read_word; GOTO 28
firmware[27] = 0b000011100_000_00010100_100000_010_010
## 28: X <- MDR; GOTO 29
firmware[28] = 0b000011101_000_00010100_000100_000_000
## 29: PC <- PC + 1; MBR <- read_byte(PC); GOTO 30
firmware[29] = 0b000011110_000_00110101_001000_001_001
## 30: MAR <- MBR; read_word; GOTO 31
firmware[30] = 0b000011111_000_00010100_100000_010_010
## 31: H <- MDR; GOTO 32
firmware[31] = 0b000100000_000_00010100_000001_000_000
## 32: Y <- X; GOTO 33
firmware[32] = 0b000100001_000_00010100_000010_000_011
## 33: X <- 0; GOTO 34
firmware[33] = 0b000100010_000_00010000_000100_000_000
## 34: Y <- Y - H; if Y - H < 0 GOTO 35 + 256; else GOTO 35
firmware[34] = 0b000100011_010_00111111_000010_000_100

### 35: Y é maior ou igual a 0
## X <- X + 1; GOTO 34
firmware[35] =  0b000100010_000_00110101_000100_000_011
### [291] Y é menor que 0
firmware[291] = 0b000000000_100_00110101_001000_001_001


# RESTO DA DIVISÃO
# memory[address] <- H + Y
## 36: PC <- PC + 1; fetch; GOTO 37
firmware[36] = 0b000100101_000_00110101_001000_001_001
## 37: MAR <- MBR; goto 38
firmware[37] = 0b000100110_000_00010100_100000_000_010

## 38: MDR <- H + Y; write; goto 0
firmware[38] = 0b000000000_000_00111100_010000_100_100


# X <- X!
## 44: PC <- PC + 1, fetch; GOTO 45
firmware[44] = 0b000101101_000_00110101_001000_001_001
## 45: MAR <- MBR; read_word; GOTO 46
firmware[45] = 0b000101110_000_00010100_100000_010_010
## 46: X <- MDR; GOTO 47
firmware[46] = 0b000101111_000_00010100_000100_000_000
## 47: if X == 0 GOTO 48 + 256; else GOTO 48
firmware[47] = 0b000110000_001_00010100_000100_000_011
## 304: X <- 1; GOTO 0
firmware[304]= 0b000000000_000_00110101_000100_000_011 
## MDR <- X; GOTO 49
firmware[48] = 0b000110001_000_00010100010000000011
## H <- X; GOTO 50
firmware[49] = 0b00011001000000010100000001000011
## MDR <- MDR - 1; GOTO 51
firmware[50] = 0b00011001100000110110010000000000
## if MDR == 0; GOTO 52 + 256; else GOTO 52
firmware[51] = 0b000110100_00100010100000000000000
### [308] MDR é igual a 0
firmware[308] = 0b00000000010000110101001000001001
### [52] MDR é diferente de 0
## Y <- MDR; GOTO 53
firmware[52] = 0b00011010100000010100000010000000
### [53] inicia a multiplicação
## X <- 0; GOTO 54
firmware[53] = 0b00011011000000010000000100000000
## if Y == 0; GOTO 55 + 256; else GOTO 55
firmware[54] = 0b00011011100100010100000000000100
### [311] Y é igual a 0, portanto, GOTO 50 e H <- X
## H <- X; GOTO 50
firmware[311] = 0b00011001000000010100000001000011
### [55] Y é diferente de 0 
## Y <- Y - 1; GOTO 56
firmware[55] = 0b00011100000000110110000010000100
## X <- X + H; GOTO 54
firmware[56] = 0b00011011000000111100000100000011

# X = memory[address]

## 60: PC <- PC + 1; fetch; goto 61
firmware[60] = 0b000111101_000_00110101_001000_001_001

## 61: MAR <- MBR; read_word(MAR); goto 62
firmware[61] = 0b000111110_000_00010100_100000_010_010

## 62: X <- MDR; goto 0
firmware[62] = 0b000000000_000_00010100_000100_000_000

# CSW (a, b, c):
# 60: PC <- PC + 1; fetch; GOTO 61
# 61: MAR <- MBR; read_word; GOTO 62
# 62: H <- MDR (a); GOTO 63

# 63: PC <- PC + 1; fetch; GOTO 64
# 64: MAR <- MBR; read_word; GOTO 65
# 65: Y <- MDR (c); GOTO 66
# 67: IF Y - H == 0 GOTO 68 + 256; ELSE GOTO 68


# 68: PC <- PC + 1; fetch; GOTO 69
# 69: MDR <- 1; GOTO 70
# 70: MAR <- MBR; write; GOTO 0
# 71: X <- Y; GOTO 0

# 324: PC <- PC + 1; fetch; GOTO 69
# 325: MDR <- 0; GOTO 70
# 326: MAR <- MBR; write; GOTO 0
# 327: X <- Y; GOTO 0



MPC = 0               
MIR = 0

MAR = 0
MDR = 0
PC  = 0
MBR = 0
X = 0
Y = 0
H = 0

N = 0
Z = 1

BUS_A = 0
BUS_B = 0
BUS_C = 0

def read_regs(reg_num):
    global MDR, PC, MBR, X, Y, H, BUS_A, BUS_B
    
    BUS_A = H
    
    if reg_num == 0:
        BUS_B = MDR
    elif reg_num == 1:
        BUS_B = PC
    elif reg_num == 2:
        BUS_B = MBR
    elif reg_num == 3:
        BUS_B = X
    elif reg_num == 4:
        BUS_B = Y
    else:
        BUS_B = 0
            
def write_regs(reg_bits):

    global MAR, BUS_C, MDR, PC, X, Y, H

    if reg_bits & 0b100000:
        MAR = BUS_C
         
    if reg_bits & 0b010000:
        MDR = BUS_C
        
    if reg_bits & 0b001000:
        PC = BUS_C
        
    if reg_bits & 0b000100:
        X = BUS_C
        
    if reg_bits & 0b000010:
        Y = BUS_C
        
    if reg_bits & 0b000001:
        H = BUS_C
        
            
def alu(control_bits):

    global BUS_A, BUS_B, BUS_C, N, Z
    
    a = BUS_A 
    b = BUS_B
    o = 0
    
    shift_bits = control_bits & 0b11000000
    shift_bits = shift_bits >> 6
    
    control_bits = control_bits & 0b00111111
    
    if control_bits == 0b011000: 
        o = a
    elif control_bits == 0b010100:
        o = b
    elif control_bits == 0b011010:
        o = ~a
    elif control_bits == 0b101100:
        o = ~b
    elif control_bits == 0b111100:
        o = a + b    
    elif control_bits == 0b111101:
        o = a + b + 1
    elif control_bits == 0b111001:
        o = a + 1
    elif control_bits == 0b110101:
        o = b + 1
    elif control_bits == 0b111111:
        o = b - a
    elif control_bits == 0b110110:
        o = b - 1
    elif control_bits == 0b111011:
        o = -a
    elif control_bits == 0b001100:
        o = a & b
    elif control_bits == 0b011100:
        o = a | b
    elif control_bits == 0b010000:
        o = 0
    elif control_bits == 0b110001:
        o = 1
    elif control_bits == 0b110010:
        o = -1 
        
    if o == 0:
        Z = 1
    else:
        Z = 0

    if o < 0:
        N = 1
    else:
        N = 0

        
    if shift_bits == 0b01:
        o = o << 1 # MULT POR 2
    elif shift_bits == 0b10:
        o = o >> 1 # DIVI POR 2
    elif shift_bits == 0b11:
        o = o << 8 # MULT POR 256
        
    BUS_C = o
 

def next_instruction(next, jam):

    global MPC, MBR, N, Z
    
    if jam == 0b000:
        MPC = next
        return
        
    if jam & 0b001:                 # JAMZ
        next = next | (Z << 8)
        
    if jam & 0b010:                 # JAMN
        next = next | (N << 8)

    if jam & 0b100:                 # JMPC
        next = next | MBR
        
    MPC = next


def memory_io(mem_bits):

    global PC, MBR, MDR, MAR
    
    if mem_bits & 0b001:                # FETCH
       MBR = memory.read_byte(PC)
       
    if mem_bits & 0b010:                # READ
       MDR = memory.read_word(MAR)
       
    if mem_bits & 0b100:                # WRITE
       memory.write_word(MAR, MDR)
       
def step():
   
    global MIR, MPC
    
    MIR = firmware[MPC]
    
    if MIR == 0:
        return False    
    
    read_regs        ( MIR & 0b00000000000000000000000000000111)
    alu              ((MIR & 0b00000000000011111111000000000000) >> 12)
    write_regs       ((MIR & 0b00000000000000000000111111000000) >> 6)
    memory_io        ((MIR & 0b00000000000000000000000000111000) >> 3)
    next_instruction ((MIR & 0b11111111100000000000000000000000) >> 23,
                      (MIR & 0b00000000011100000000000000000000) >> 20)
                      
    return True