import importlib
import os

MODULE = importlib.import_module(os.environ.get("LAB_MODULE", "lab"))


def expect_error(error_type, function, *args):
    try:
        function(*args)
    except error_type:
        return
    except Exception as error:  # pragma: no cover
        raise AssertionError(f"erro inesperado: {type(error).__name__}: {error}") from error
    raise AssertionError(f"esperado {error_type.__name__}")

assert MODULE.bissexto(1984) is True
assert MODULE.bissexto(1900) is False
assert MODULE.bissexto(2000) is True
assert MODULE.dias_mes(2, 2024) == 29
assert MODULE.dias_mes(2, 2023) == 28
assert MODULE.dias_mes(4, 2024) == 30
assert MODULE.dias_mes(12, 2024) == 31
expect_error(ValueError, MODULE.dias_mes, 13, 2024)
assert MODULE.data_valida(29, 2, 2024) is True
assert MODULE.data_valida(29, 2, 2023) is False
assert MODULE.data_valida(31, 4, 2024) is False
assert MODULE.data_valida(1, 13, 2024) is False

assert MODULE.dias_de_segundos(86400) == 1
expect_error(ValueError, MODULE.dias_de_segundos, -1)

assert MODULE.decompor_segundos(0) == (0, 0, 0, 0)
assert MODULE.decompor_segundos(90061) == (1, 1, 1, 1)
assert MODULE.formatar_duracao(345678) == "dias: 4; horas: 0; mins: 1; segs: 18"

assert MODULE.maior_de_tres(7, 12, 5) == 12
assert MODULE.maior_de_tres(4, 4, 2) == 4
assert MODULE.salario_semanal(38, 10) == 380
assert MODULE.salario_semanal(40, 10) == 400
assert MODULE.salario_semanal(45, 10) == 500
expect_error(ValueError, MODULE.salario_semanal, -1, 10)

assert MODULE.troco_centimos(0) == ""
assert MODULE.troco_centimos(388) == "200:1; 100:1; 50:1; 20:1; 10:1; 5:1; 2:1; 1:1"
assert MODULE.troco_centimos(7865).startswith("5000:1")
expect_error(ValueError, MODULE.troco_centimos, -5)

assert MODULE.tarifa_envio(100) == 120
assert MODULE.tarifa_envio(101) == 250
assert MODULE.tarifa_envio(2500) == 800
assert MODULE.tarifa_envio(2500, urgente=True) == 1120
expect_error(ValueError, MODULE.tarifa_envio, 0)

print("OK - L02")
