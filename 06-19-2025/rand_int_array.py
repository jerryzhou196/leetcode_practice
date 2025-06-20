import random

def rand_int_array(x: int, y: int, n: int) -> list[int]:
    """List of n random integers, each uniformly drawn from [x, y]."""
    if x > y:
        raise ValueError("x must not be greater than y")
    return [random.randint(x, y) for _ in range(n)]
