def flip_bit(number, n):
    result = number ^ (1 << (n - 1))
    return bin(result)