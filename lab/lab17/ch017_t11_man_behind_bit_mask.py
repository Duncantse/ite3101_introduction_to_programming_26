def check_bit4(input):
    mask = 0b1000
    result = input & mask
    if result > 0:
        return "on"
    else:
        return "off"