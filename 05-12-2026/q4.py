def getMinOperations(val):
    operations = 0
    
    while val >= 0:
        if val % 2 == 1: 
            operations += 1
        val //= 2
    return operations
    

