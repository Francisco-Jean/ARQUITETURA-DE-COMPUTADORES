goto main
wb 0

a ww 16
b ww 0
c ww 0
d ww 0

main div x, a
     mem x, b
     mov x, a
     mod x, b
     halt
