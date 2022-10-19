# Напишите функцию last_discharge(a), которая в качестве аргумента получает строку, содержащую число a, и возвращает это же число, уменьшенное на единицу в последнем его разряде в виде строки.

# Обратите внимание:

# ●     в последнем разряде может быть ноль,

# ●     входная строка может представлять как целое число, так и число с плавающей точкой,

# ●     входная строка содержит число строго больше нуля.

from decimal import Decimal

def last_discharge(a: str):
    dec_line = Decimal(a)
    if dec_line.as_tuple().exponent < 0:
        submition = '0.' + '0' * (abs(dec_line.as_tuple().exponent) - 1) + '1'
    else:
        submition = '1'
    dec_submition = Decimal(submition)
    return dec_line - dec_submition

