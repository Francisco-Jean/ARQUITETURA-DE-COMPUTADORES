    goto main
    wb 0

a ww 8
b ww 10
c ww 7
d ww 1
e ww 0

main set x, a
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