---
title: "L01 - Primeiros Programas"
subtitle: "Fundamentos de Programação 2026-2027"
lang: pt-PT
---

## Pré-requisitos

Ambiente Python 3.11+, terminal, REPL e execução de ficheiros.

## Objetivos

- confirmar o ambiente de trabalho e executar um programa
- prever valores de expressões antes de usar o REPL
- distinguir erros de sintaxe, execução e lógica
- calcular e formatar uma fatura simples
- completar um primeiro programa com funções pequenas, entrada e saída

## 1. Revisão

Antes de executar Python, preencha uma tabela com previsão, tipo e explicação
para cada expressão:

- `2 + 3 * 4`
- `(2 + 3) * 4`
- `17 // 5`
- `17 % 5`
- `"FP" * 3`
- `int("18")`
- `float("1.72")`
- `int("1.72")`

Depois confirme no REPL, mantendo as previsões erradas visíveis. Para cada
divergência, escreva uma frase curta: precedência, tipo, divisão inteira,
resto, repetição de strings ou conversão inválida.

## 2. Trace guiado

Considere o ficheiro `fatura.py`, descrito em baixo:

```python
horas = float(input("Horas? "))
preco = float(input("Preco/hora? "))
subtotal = horas * preco
iva = subtotal * 0.23
total = subtotal + iva
print(f"Total: {total:.2f}")
```

Use as entradas `2.5` e `8`. Antes de executar, preencha uma tabela com
as colunas nome, valor e tipo para `horas`, `preco`, `subtotal`, `iva` e
`total`. Preveja também a linha impressa no terminal.

Depois execute o programa e explique qualquer diferença entre a previsão
e a execução.


## 3. Exercícios de treino

- No mesmo `fatura.py`, use as entradas `horas = 1` e
  `preco = 1.5`. Complete a tabela para `subtotal`, `iva`, `total` e
  para a saída formatada. Diga que valor é usado no cálculo e que valor aparece
  com duas casas decimais.
- Crie uma tabela de diagnóstico com duas linhas: uma para remover o
  parêntesis final de `print(...)` e outra para escrever `oito` quando o
  programa pede um número. Para cada linha, registe tipo de erro,
  mensagem provável, causa e correção.

## 4. Implementação principal

Abra `lab.py` e substitua todos os marcadores `TODO`.

1. Complete `mensagem_boas_vindas(nome, cadeira)` para devolver uma mensagem, sem imprimir.
2. Complete `area_retangulo(largura, altura)` e teste valores inteiros e reais.
3. Complete `total_servico(horas, preco_hora)` para calcular subtotal, IVA a 23% e total.
4. Complete `formatar_fatura(descricao, horas, preco_hora)` para produzir uma linha textual com duas casas decimais.
5. Complete `formatar_fatura_sessoes(descricao, sessoes, horas, preco_hora)` para reutilizar a ideia anterior quando há várias sessões iguais.
6. Complete `classificar_erro(descricao)` para reconhecer `sintaxe`, `execucao` e `logica`.

### Comportamento esperado

Execute:

```sh
python3 test_lab.py
```

O processo deve terminar com a mensagem `OK - L01`.

## 5. Integração e depuração

Execute `python3 test_lab.py`. Corrija primeiro a implementação e só depois reveja as previsões iniciais. Em seguida, crie um ficheiro `fatura.py` executável que lê descrição, horas e preço por hora e imprime a fatura usando as funções já testadas.

Não altere os testes para esconder uma falha. Acrescente testes próprios no
fim de `test_lab.py` ou num ficheiro separado.

## 6. Extensão

Acrescente ao `fatura.py` uma pergunta pelo número de sessões e use `formatar_fatura_sessoes`. Teste pelo menos dois casos à mão, incluindo preço/hora com casas decimais.

## Checkpoint final

O programa executa no terminal e todos os testes públicos passam.

Antes de sair, confirme que:

- o programa compila com Python 3.11;
- todos os testes públicos passam;
- consegue explicar uma decisão de representação ou algoritmo;
- deixou registado pelo menos um teste próprio.
