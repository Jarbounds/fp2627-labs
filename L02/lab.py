from math import ceil


def bissexto(ano: int) -> bool:
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    return False

def bissexto_alternativa(ano: int) -> bool:
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def dias_mes(mes: int, ano: int) -> int:
    if not (1 <= mes <= 12):
        raise ValueError

    if mes == 2:
        if bissexto(ano):
            return 29
        return 28
    
    if mes in [4, 6, 9, 11]:
        return 30
    
    return 31


def data_valida(dia: int, mes: int, ano: int) -> bool:
    if ano < 0:
        return False

    try:
        if not (1 <= dia <= dias_mes(mes, ano)):
            return False
    except ValueError:
        return False

    return True


def dias_de_segundos(segundos: int) -> float:
    if segundos < 0:
        raise ValueError
    return segundos // 86400


def decompor_segundos(segundos: int) -> tuple[int, int, int, int]:
    if segundos < 0:
        raise ValueError

    total_segundos = segundos
    dias = total_segundos // 86400
    total_segundos %= 86400
    horas = total_segundos // 3600
    total_segundos %= 3600
    minutos = total_segundos // 60
    seg = total_segundos % 60

    return (dias, horas, minutos, seg)


def formatar_duracao(segundos: int) -> str:
    decomposicao = decompor_segundos(segundos)
    dias, horas, minutos, segs = decomposicao
    return f'dias: {dias}; horas: {horas}; mins: {minutos}; segs: {segs}'


def maior_de_tres(a: float, b: float, c: float) -> float:
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior


def salario_semanal(horas: float, preco_hora: float) -> float:
    if horas < 0 or preco_hora < 0:
        raise ValueError

    if horas <= 40:
            return horas * preco_hora
    return horas * preco_hora + (horas - 40) * (2 * preco_hora)


def _troco_parcela(resto: int, denominacao: int, texto: str) -> tuple[int, str]:
    quantidade = resto // denominacao
    if quantidade == 0:
        return resto, texto
    if texto:
        texto += "; "
    texto += f"{denominacao}:{quantidade}"
    return resto % denominacao, texto


def troco_centimos(total: int) -> str:
    if total < 0:
        raise ValueError("total negativo")
    resto = total
    texto = ""
    resto, texto = _troco_parcela(resto, 5000, texto)
    resto, texto = _troco_parcela(resto, 2000, texto)
    resto, texto = _troco_parcela(resto, 1000, texto)
    resto, texto = _troco_parcela(resto, 500, texto)
    resto, texto = _troco_parcela(resto, 200, texto)
    resto, texto = _troco_parcela(resto, 100, texto)
    resto, texto = _troco_parcela(resto, 50, texto)
    resto, texto = _troco_parcela(resto, 20, texto)
    resto, texto = _troco_parcela(resto, 10, texto)
    resto, texto = _troco_parcela(resto, 5, texto)
    resto, texto = _troco_parcela(resto, 2, texto)
    resto, texto = _troco_parcela(resto, 1, texto)
    return texto


def tarifa_envio(peso_g: int, urgente: bool = False) -> int:
    if peso_g <= 0:
        raise ValueError

    if peso_g <= 100:
        preco_peso = 120
    elif peso_g <= 500:
        preco_peso = 250
    elif peso_g <= 2000:
        preco_peso = 500
    else:
        preco_peso = 500 + 300 * ceil((peso_g - 2000) / 1000)

    if urgente:
        return ceil(preco_peso * 1.4)
    return preco_peso
