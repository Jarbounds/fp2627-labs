def digitos_impares(n: int) -> int:
    if n < 0:
        raise ValueError
    numero = n
    fator = 1
    numero_impar = 0
    while numero > 0:
        digito = numero % 10
        if digito % 2 != 0:
            numero_impar = numero_impar + (digito * fator)
            fator *= 10
        numero //= 10

    return numero_impar


def inverter_numero(n: int) -> int:
    if n < 0:
        raise ValueError
    numero = n
    inverso = 0
    while numero > 0:
        digito = numero % 10
        if digito != 0:
            inverso = inverso * 10 + digito
        numero //= 10
    return inverso


def contar_zeros_consecutivos(n: int) -> int:
    if n < 0:
        raise ValueError

    contador = 0
    anterior = -1
    numero = n
    while numero > 0:
        digito = numero % 10
        if anterior == -1 and digito == 0:
            anterior = digito
        elif anterior == digito == 0:
            contador += 1
        else:
            anterior = -1
        numero //= 10
    return contador


def soma_serie_exp(x: float, n: int) -> float:
    if n < 0:
        raise ValueError("n negativo")
    soma = 1.0
    termo = 1.0
    i = 1
    while i <= n:
        termo = termo * x / i
        soma += termo
        i += 1
    return soma


def contar_fibonacci_entre(minimo: int, maximo: int) -> int:
    if minimo > maximo:
        return 0
    total = 0
    a, b = 0, 1
    while a <= maximo:
        if a >= minimo:
            total += 1
        a, b = b, a + b
    return total


def tipo_divisores(n: int) -> str:
    if n < 1:
        raise ValueError("n deve ser positivo")
    soma = 0
    divisor = 1
    while divisor < n:
        if n % divisor == 0:
            soma += divisor
        divisor += 1
    if soma == n:
        return "perfeito"
    if soma > n:
        return "abundante"
    return "deficiente"
