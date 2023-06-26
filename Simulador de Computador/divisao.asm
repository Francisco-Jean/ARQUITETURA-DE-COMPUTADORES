goto main
wb 0

a ww 20
b ww 10
c ww 0
d ww 0

main div x, a
     mem x, b
     mov x, d
     mod x, b
     halt
