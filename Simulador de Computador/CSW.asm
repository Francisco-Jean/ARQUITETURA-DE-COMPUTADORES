    goto main
    wb 0

a ww 1
b ww 10
c ww 12
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