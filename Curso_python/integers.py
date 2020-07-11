#change the base of a b10 number

def from_base10(number, base):
    if base < 2:
        raise ValueError('base must be greater than 2')
    if number == 0:
        return [0]
    digits = []
    while number > 0:
        number ,mod = divmod(number,base)
        digits.insert(0,mod)
    digits = encode(digits,'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return digits


def encode(digits, digit_maper):
    if max(digits) >= len(digit_maper):
        raise ValueError("mapper is not large enough")
    return ''.join([digit_maper[digit] for digit in digits])
print(from_base10(255,16))