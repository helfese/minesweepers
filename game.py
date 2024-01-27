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
    Devolve seus bits.
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

def cria_coordenada(col, lin):

    """
    A função recebe um caráter maiúsculo e um inteiro positvo menor que 100 correspondentes à coluna e à linha.
    Devolve a coordenada correspondente, verificando a validade dos argumentos.
    """

    if not (isinstance(col, str) and 'A' <= col <= 'Z' and len(col) == 1 and isinstance(lin, int) and 1 <= lin <= 99):
        raise ValueError('cria_coordenada: argumentos invalidos')

    return (col, lin)

def obtem_coluna(c):

    """
    A função recebe uma coordenada.
    Devolve a sua coluna.
    """

    return c[0]

def obtem_linha(c):

    """
    A função recebe uma coordenada.
    Devolve a sua linha.
    """

    return c[1]

def eh_coordenada(arg):

    """
    A função recebe um argumento.
    Devolve True se for um TAD coordenada, caso contrário, False.
    """

    return isinstance(arg, tuple) and isinstance(arg[0], str) and len(arg[0]) == 1 and isinstance(arg[1], int) \
        and 'A' <= arg[0] <= 'Z' and len(arg[0]) == 1 and 1 <= arg[1] <= 99 and len(arg) == 2

def coordenadas_iguais(c1, c2):

    """
    A função recebe duas coordenadas.
    Devolve True se forem iguais, caso contrário, False.
    """

    return eh_coordenada(c1) and eh_coordenada(c2) and obtem_coluna(c1) == obtem_coluna(c2) and obtem_linha(c2) == obtem_linha(c1)

def coordenada_para_str(c):

    """
    A função recebe uma coordenada.
    Devolve uma string representando-a.
    """

    return '{}{:0>2}'.format(obtem_coluna(c), obtem_linha(c))

def str_para_coordenada(s):

    """
    A função recebe uma string representando uma coordenada.
    Devolve a coordenada.
    """

    return (s[0],int(s[1:]))

def obtem_coordenadas_vizinhas(c):

    """
    A função recebe uma coordenada.
    Devolve um tuplo com as coordenadas vizinhas àquela, no sentido horário.
    """

    if obtem_coluna(c) == 'A':
        if obtem_linha(c) == 1:
            return (('B', 1), ('B', 2), ('A', 2))
        elif obtem_linha(c) == 99:
            return (('A', 98), ('B', 98), ('B', 99))
        else:
            return (('A', obtem_linha(c)-1), ('B', obtem_linha(c)-1), ('B', obtem_linha(c)), ('B', obtem_linha(c)+1), ('A', obtem_linha(c)+1))

    elif obtem_coluna(c) == 'Z':
        if obtem_linha(c) == 1:
            return (('Z', 2), ('Y', 2), ('Y', 1))
        elif obtem_linha(c) == 99:
            return (('Y', 98), ('Z', 98), ('Y', 99))
        else:
            return (('Y', obtem_linha(c)-1), ('Z', obtem_linha(c)-1), ('Z', obtem_linha(c)+1), ('Y', obtem_linha(c)+1), ('Y', obtem_linha(c)))

    else:
        if obtem_linha(c) == 1:
            return ((chr(ord(obtem_coluna(c)) + 1), 1), (chr(ord(obtem_coluna(c)) + 1), 2), (obtem_coluna(c), 2), (chr(ord(obtem_coluna(c)) - 1), 2), (chr(ord(obtem_coluna(c)) - 1), 1))
        elif obtem_linha(c) == 99:
            return ((chr(ord(obtem_coluna(c)) - 1), 98), (obtem_coluna(c), 98), (chr(ord(obtem_coluna(c)) + 1), 98), (chr(ord(obtem_coluna(c)) + 1), 99), (chr(ord(obtem_coluna(c)) - 1), 99))
        else:
            return ((chr(ord(obtem_coluna(c)) - 1), obtem_linha(c)-1), (obtem_coluna(c), obtem_linha(c)-1), (chr(ord(obtem_coluna(c)) + 1), obtem_linha(c)-1), (chr(ord(obtem_coluna(c)) + 1), obtem_linha(c)), \
                    (chr(ord(obtem_coluna(c)) + 1), obtem_linha(c)+1), (obtem_coluna(c), obtem_linha(c)+1), (chr(ord(obtem_coluna(c)) - 1), obtem_linha(c)+1), (chr(ord(obtem_coluna(c)) - 1), obtem_linha(c)))

def obtem_coordenada_aleatoria(c, g):

    """
    A função recebe uma coordenada e um gerador.
    Devolve uma coordenada aleatória.
    """

    return cria_coordenada(gera_carater_aleatorio(g, obtem_coluna(c)), gera_numero_aleatorio(g, obtem_linha(c)))
