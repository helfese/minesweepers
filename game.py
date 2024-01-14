def cria_gerador(b, s):
    if not (isinstance(b, int) and isinstance(s, int) and s > 0 and ((b == 32 and s < 2 ** 32 - 1) \
        or (b == 64 and s <= 2 ** 64 - 1))):
        raise ValueError('cria_gerador: argumentos invalidos')
    return {'bits': b, 'seed': s}
