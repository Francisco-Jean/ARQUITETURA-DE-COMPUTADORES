    goto main
    wb 0

a ww 5
b ww 1

main set x, a
     jz x, zero
     set y, a
     subone y
     goto fato
fato jz y, resu
     mul x, y
     subone y
     goto fato

zero halt

resu mov x, b
     halt