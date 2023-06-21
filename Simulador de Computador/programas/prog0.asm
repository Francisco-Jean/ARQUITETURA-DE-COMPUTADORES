   goto main 
   wb 0

a ww 15
b ww 32
c ww 10
d ww 0

main add x, a           
     jz x, nova         
     add x, b           
nova sub x, c           
     mov x, d
     halt

