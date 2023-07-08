lis $7          ; store constant 7 in register $7
.word 7         ; store constant 7 in register $7

lis $1          ; store constant -1 in register $1
.word -1        ; store constant -1 in register $1

divu $3, $7      ; divide value of $1 by 7

mfhi $3           ; get remainder and store in register $3

slt $1, $3, $0    ; 1 = negative, 0 = positive 
beq $1, $0, 2     ; go straight to end if we are positive
mult $3, $1       ; multiply by 3
mflo $3           ; replace 3 with positive value

# ----------- OPTIMIZED SOLUTION

lis $7          ; store constant 7 in register $7
.word 7         ; store constant 7 in register $7

divu $3 $7      ; divide value of $1 by 7

mfhi $3         ; get remainder and store in register $3

slt $1, $3, $0    ; 1 = negative, 0 = positive 
beq $1, $0, 1     ; go straight to end if we are positive
sub $3, $0, $3 
mflo $3         ; replace 3 with positive values

