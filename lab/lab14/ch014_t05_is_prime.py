def is_prime(x):
    n = 2
    for n in x-1:
        if x % n ==0:
            return False
        else:
            return True