    goto main
    wb 0

a ww 10
b ww 1
c ww 9

d ww 0
e ww 1

main set x, a
     sub x, c
     jz x, equal
     set x, c
     halt

equal set x, b
     mov x, c
     halt