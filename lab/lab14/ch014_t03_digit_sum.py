def digit_sum(n):
    total = 0
    for i in n:
        if n >=0:
            total += n % 10
            n = n/10
