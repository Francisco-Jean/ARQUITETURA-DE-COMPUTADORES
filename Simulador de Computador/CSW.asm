    goto main
    wb 0

a ww 8
b ww 8
c ww 8


d ww 1
e ww 0

main add x, a
     sub x, c
     jz x, equal
     set x, c
     mov x, a
     halt

equal set x, b
      mov x, c
      set x, e
      mov x, d
      halt