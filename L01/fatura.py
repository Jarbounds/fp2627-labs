horas = float(input("Horas? "))
preco = float(input("Preco/hora? "))
subtotal = horas * preco
iva = subtotal * 0.23
total = subtotal + iva
print(f"Total: {total:.2f}")

"""
Tabela (Exercício 2)
nome, valor, tipo

horas, 2.5, float
preco, 8, float
subtotal, 20, float
iva, 4.6, float
total, 24.6, float

Print final
"Total: 24.60"
"""

"""
Tabela (Exercício 3)
nome, valor, tipo

subtotal, 1.5, float
iva, 0.345, float
total, 1.845, float

Print final
"Total: 1.84"
"""

"""
Remover o parêntesis final do print(...) provoca um erro de sintaxe (SintaxError) visto estarmos à espera de fechar a chamada à função após a passagem de argumentos.
Escrever 'oito' quando esperamos um número provoca um erro de valor (ValueError) visto que as funções numéricas não esperam receber valores numéricos em forma textual extensa.
"""