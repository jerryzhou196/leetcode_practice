    .text                   # This indicates the start of the actual code
    .globl main             # This declares a global main function

main:
    # Step 1: Copy the value in register 1 ($t0) to register 2 ($t1).
    move    $t1, $t0        # Copy $t0 to $t1

    # Step 2: Store the two's complement encoding of -241 in register 4 ($t2).
    li      $t2, -241       # Load immediate -241 into $t2

    # Step 3: Add the value in register 2 ($t1) to the value in register 4 ($t2),
    # storing the result in register 1 ($t0).
    add     $t0, $t1, $t2   # Add $t1 and $t2 and store result in $t0

    # Step 4: Terminate the program by returning to the loader.
    jr      $ra             # Jump to the address stored in the $ra register (return address)
