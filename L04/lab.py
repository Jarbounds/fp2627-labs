Relogio = tuple[int, int, int]


def cria_relogio(h: int, m: int, s: int) -> Relogio:
    if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        raise ValueError
    return (h, m, s)


def horas(r: Relogio) -> int:
    return r[0]


def minutos(r: Relogio) -> int:
    return r[1]


def segundos(r: Relogio) -> int:
    return r[2]


def escreve_relogio(r: Relogio) -> str:
    return f"{horas(r):02d}:{minutos(r):02d}:{segundos(r):02d}"


def _total_segundos(r: Relogio) -> int:
    return horas(r) * 3600 + minutos(r) * 60 + segundos(r)


def mesmas_horas(r1: Relogio, r2: Relogio) -> bool:
    # return horas(r1) == horas(r2) and minutos(r1) == minutos(r2) and segundos(r1) == segundos(r2)
    return _total_segundos(r1) == _total_segundos(r2)


def depois_rel(r1: Relogio, r2: Relogio) -> bool:
    return _total_segundos(r2) > _total_segundos(r1)


def dif_segs(r1: Relogio, r2: Relogio) -> int:
    if not depois_rel(r1, r2):
        raise ValueError
    return _total_segundos(r2) - _total_segundos(r1)
    


def avanca(r: Relogio, delta: int) -> Relogio:
    if delta < 0:
        raise ValueError

    novo_total = (_total_segundos(r) + delta) % 86400

    # if _total_segundos(r) + delta > 86400:
        # novo_total = _total_segundos(r) - 86400 + delta
    # else:
        # novo_total = _total_segundos(r) + delta

    h = novo_total // 3600
    novo_total = novo_total % 3600
    m = novo_total // 60
    s = novo_total % 60
    return cria_relogio(h, m, s)


def intervalos_validos(inicio: Relogio, duracoes: tuple[int, ...]) -> tuple[Relogio, ...]:
    lista_relogios = []
    relogio = inicio
    for duracao in duracoes:
        relogio = avanca(relogio, duracao)
        lista_relogios.append(relogio)
    # Alternativa com ciclo while
    # i = 0
    # while i < len(duracoes):
        # relogio = avanca(relogio, duracoes[i])
        # lista_relogios.append(relogio)
        # i += 1

    return tuple(lista_relogios)
