def is_prime(x):
    for n in range(2, x):
        if x <= 2:
            return True
        if x % n == 0:
            return False
        else:
            return True
