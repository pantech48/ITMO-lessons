def geometric_progression_generator(b, q):
    if not b:
        raise ArithmeticError('The first term is zero.')
    if not q:
        raise ArithmeticError('The denominator is zero.')
    while True:
        yield b
        b *= q