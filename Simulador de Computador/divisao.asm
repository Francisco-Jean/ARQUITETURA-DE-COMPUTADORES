goto main
wb 0

a ww 1
b ww 1
c ww 0
d ww 0

main div x, a
     mem x, b
     mov x, a
     mod x, b
     halt
