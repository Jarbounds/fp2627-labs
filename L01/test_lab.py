import importlib
import os


def expect_error(error_type, function, *args):
    try:
        function(*args)
    except error_type:
        return
    raise AssertionError(f"esperava {error_type.__name__}")


MODULE = importlib.import_module(os.environ.get("LAB_MODULE", "lab"))

assert MODULE.mensagem_boas_vindas("Ana", "FP") == "Ana, bem-vindo/a a FP!"
assert MODULE.mensagem_boas_vindas("", "FP") == ", bem-vindo/a a FP!"
assert MODULE.area_retangulo(3, 4) == 12
assert MODULE.area_retangulo(2.5, 4) == 10
assert MODULE.total_servico(2.5, 8) == 24.6
assert MODULE.total_servico(1, 1.5) == 1.845
assert MODULE.formatar_fatura("Apoio tecnico", 2.5, 8) == "Apoio tecnico: 24.60 euros"
assert MODULE.formatar_fatura("Revisao", 1, 1.5) == "Revisao: 1.84 euros"
assert MODULE.formatar_fatura_sessoes("Apoio tecnico", 2, 2.5, 8) == "Apoio tecnico: 49.20 euros"
assert MODULE.formatar_fatura_sessoes("Revisao", 3, 1, 1.5) == "Revisao: 5.54 euros"
assert MODULE.classificar_erro("SyntaxError na linha 3") == "sintaxe"
assert MODULE.classificar_erro("ValueError durante a execução") == "execucao"
assert MODULE.classificar_erro("resultado errado: erro de lógica") == "logica"

print("OK - L01")
