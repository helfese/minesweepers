def cria_gerador(b, s):

    """
    A função recebe um inteiro e outro positvo correspondentes ao número de bits e à seed.
    Devolve o gerador correspondente, verificando a validade dos argumentos.
    """

    if not (isinstance(b, int) and isinstance(s, int) and s > 0 and ((b == 32 and s < 2 ** 32 - 1) \
        or (b == 64 and s <= 2 ** 64 - 1))):
        raise ValueError('cria_gerador: argumentos invalidos')

    return {'bits': b, 'seed': s}

def cria_copia_gerador(g):

    """
    A função recebe um gerador.
    Devolve uma cópia sua.
    """

    return g.copy()

def obtem_estado(g):

    """
    A função recebe um gerador.
    Devolve o seu estado.
    """

    return g['seed']

def obtem_bits(g):

    """
    A função recebe um gerador.
    Devolve os seus bits.
    """

    return g['bits']

def define_estado(g, s):

    """
    A função recebe um gerador e uma seed, e muda o valor do estado anterior.
    Devolve o novo estado.
    """

    g['seed'] = s
    return g['seed']

def atualiza_estado(g):

    """
    A função recebe um gerador.
    Devolve o estado do gerador atualizado.
    """

    if g['bits'] == 32:
        g['seed'] ^= (g['seed'] << 13) & 0xFFFFFFFF
        g['seed'] ^= (g['seed'] >> 17) & 0xFFFFFFFF
        g['seed'] ^= (g['seed'] << 5) & 0xFFFFFFFF
        return g['seed']

    elif g['bits'] == 64:
        g['seed'] ^= (g['seed'] << 13) & 0xFFFFFFFFFFFFFFFF
        g['seed'] ^= (g['seed'] >> 7) & 0xFFFFFFFFFFFFFFFF
        g['seed'] ^= (g['seed'] << 17) & 0xFFFFFFFFFFFFFFFF
        return g['seed']

def eh_gerador(arg):

    """
    A função recebe um argumento.
    Devolve True se for um TAD gerador, caso contrário, False.
    """

    return isinstance(arg, dict) and 'bits' in arg and 'seed' in arg and isinstance(arg['bits'], int) \
    and (arg['bits'] == 32 or arg['bits'] == 64) and isinstance(arg['seed'], int) and arg['seed'] > 0 and len(arg) == 2

def geradores_iguais(g1, g2):

    """
    A função recebe dois geradores.
    Devolve True se forem iguais, caso contrário, False.
    """

    return eh_gerador(g1) and eh_gerador(g2) and g1['bits'] == g2['bits'] and g1['seed'] == g2['seed']

def gerador_para_str(g):

    """
    A função recebe um gerador.
    Devolve uma string representando-o.
    """

    return 'xorshift{}(s={})'.format(g['bits'], g['seed'])

def gera_numero_aleatorio(g, n):

    """
    A função recebe um gerador e um número.
    Devolve um número aleatório entre 1 e o número do argumento.
    """

    atualiza_estado(g)
    return 1 + (obtem_estado(g) % n)

def gera_carater_aleatorio(g, c):

    """
    A função recebe um gerador e um caráter maiúsculo.
    Devolve um caráter aleatório entre 'A' e o caráter do argumento.
    """

    atualiza_estado(g)
    string = ''.join([chr(x) for x in range(ord('A'), ord(c) + 1)])
    return string[obtem_estado(g) % len(string)]
