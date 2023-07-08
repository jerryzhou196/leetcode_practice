


(define get-cfg 
    (let helper ([accumulator empty])
      (define c (peek-char in))
      (cond [(eof-object? c)
             (cond [(empty? accumulator) eof]
                   [else accumulator])]
            [(char-whitespace? c)
             (cond [(empty? accumulator)
                    (read-char in)
                    (helper accumulator)]
                   [else accumulator])]
            [else (helper (cons (read-char in) accumulator))]))




    


)


(define guided-parser 
    (let* [CFG (get-cfg)])



)
