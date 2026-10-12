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

r = MODULE.cria_relogio(9, 2, 34)
assert MODULE.horas(r) == 9
assert MODULE.minutos(r) == 2
assert MODULE.segundos(r) == 34
assert MODULE.escreve_relogio(r) == "09:02:34"
expect_error(ValueError, MODULE.cria_relogio, 24, 0, 0)
expect_error(ValueError, MODULE.cria_relogio, 12, 60, 0)

r1 = MODULE.cria_relogio(10, 2, 34)
r2 = MODULE.cria_relogio(11, 21, 34)
r3 = MODULE.cria_relogio(10, 2, 34)
assert MODULE.depois_rel(r1, r2)
assert not MODULE.depois_rel(r1, r3)
assert MODULE.mesmas_horas(r1, r3)
assert MODULE.dif_segs(r1, r2) == 4740
expect_error(ValueError, MODULE.dif_segs, r2, r1)

assert MODULE.avanca(MODULE.cria_relogio(23, 59, 50), 15) == MODULE.cria_relogio(0, 0, 5)
assert MODULE.intervalos_validos(MODULE.cria_relogio(8, 0, 0), (60, 3600, 30)) == (
    MODULE.cria_relogio(8, 1, 0),
    MODULE.cria_relogio(9, 1, 0),
    MODULE.cria_relogio(9, 1, 30),
)
print("OK - L04")
