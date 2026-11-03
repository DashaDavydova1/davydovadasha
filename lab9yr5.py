def order_weight(strng):
    numbers = strng.split()
    numbers.sort(key=lambda x: (sum(int(digit) for digit in x), x))
    return ' '.join(numbers)