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

assert MODULE.digitos_impares(12426374856) == 1375
assert MODULE.digitos_impares(468) == 0
assert MODULE.digitos_impares(0) == 0
expect_error(ValueError, MODULE.digitos_impares, -12)

assert MODULE.inverter_numero(7633256) == 6523367
assert MODULE.inverter_numero(1200) == 21
assert MODULE.contar_zeros_consecutivos(98007640003) == 3
assert MODULE.contar_zeros_consecutivos(10002) == 2
assert MODULE.contar_zeros_consecutivos(1010) == 0

assert abs(MODULE.soma_serie_exp(2, 3) - 6.333333333333333) < 1e-12
assert MODULE.soma_serie_exp(5, 0) == 1
expect_error(ValueError, MODULE.soma_serie_exp, 2, -1)

assert MODULE.contar_fibonacci_entre(0, 1) == 3
assert MODULE.contar_fibonacci_entre(2, 10) == 4
assert MODULE.tipo_divisores(6) == "perfeito"
assert MODULE.tipo_divisores(12) == "abundante"
assert MODULE.tipo_divisores(8) == "deficiente"
expect_error(ValueError, MODULE.tipo_divisores, 0)

print("OK - L03")
