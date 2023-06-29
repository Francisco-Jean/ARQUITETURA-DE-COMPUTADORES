goto main
wb 0

a ww 1024
b ww 16
c ww 0
d ww 0
r ww 0

main div x, a
     mem x, b
     mov x, d
     mod x, r
     halt
