---
title: "L03 - Ciclos Numéricos"
subtitle: "Fundamentos de Programação 2026-2027"
lang: pt-PT
---

## Pré-requisitos

Ciclos `while`, acumulação, divisibilidade, atualização de estado e validação
simples de argumentos.

## Objetivos

- construir ciclos com estado mínimo e condição de paragem clara;
- processar dígitos sem converter para strings;
- atualizar termos de uma série a partir do termo anterior;
- separar funções auxiliares quando a decisão algorítmica se repete.

## Exercícios

O enunciado abaixo é auto-contido: não é necessário consultar `lab.py` para
perceber o que cada função deve fazer. Durante a aula, resolva em papel,
escrevendo para cada função a assinatura, as variáveis que mudam no ciclo, a
condição de paragem, os casos de erro e exemplos de chamada com resultado.
Quando tiver computador, transcreva as soluções para `lab.py`, substituindo os
marcadores `TODO`.

1. `digitos_impares(n)` recebe um inteiro não negativo e devolve o número
   formado apenas pelos dígitos ímpares de `n`, pela ordem original. Não use
   conversão para string. Se `n` não tiver dígitos ímpares, devolve `0`. Por
   exemplo, `digitos_impares(12426374856)` devolve `1375` e
   `digitos_impares(468)` devolve `0`. Valores negativos levantam `ValueError`.
2. `inverter_numero(n)` recebe um inteiro não negativo e devolve o número obtido
   ao inverter a ordem dos seus dígitos. Zeros que passariam a estar à esquerda
   desaparecem: `inverter_numero(1200)` devolve `21`. Valores negativos
   levantam `ValueError`.
3. `contar_zeros_consecutivos(n)` recebe um inteiro não negativo e conta quantos
   pares consecutivos de zeros existem na escrita decimal. Pares sobrepostos
   contam: `10002` tem dois pares, correspondentes aos três zeros centrais.
4. `soma_serie_exp(x, n)` recebe um número `x` e um inteiro `n >= 0`, e devolve
   `1 + x + x**2/2! + ... + x**n/n!`. Calcule cada termo a partir do termo
   anterior, multiplicando por `x / i`, sem recalcular potências e fatoriais do
   zero. Se `n < 0`, levanta `ValueError`.
5. `contar_fibonacci_entre(minimo, maximo)` devolve quantos valores da sequência
   de Fibonacci pertencem ao intervalo fechado `[minimo, maximo]`. A sequência
   começa em `0, 1, 1, 2, 3, ...`; por isso `contar_fibonacci_entre(0, 1)`
   devolve `3`. Se `minimo > maximo`, devolve `0`.
6. `tipo_divisores(n)` recebe um inteiro positivo e soma os divisores próprios
   de `n`, isto é, os divisores positivos menores que `n`. Devolve
   `"perfeito"` se a soma for igual a `n`, `"abundante"` se for maior e
   `"deficiente"` se for menor. Se `n < 1`, levanta `ValueError`.

### Testes públicos

O ficheiro `test_lab.py` contém chamadas já preparadas para verificar os casos
principais desta ficha. Depois de completar `lab.py`, abra o terminal na pasta
`labs/student/L03` e execute:

```sh
python3 test_lab.py
```

Se tudo estiver correto, o processo termina com `OK - L03`. Se houver falha,
leia a primeira mensagem de erro: ela indica uma chamada que não devolveu o
resultado esperado ou uma exceção que não foi levantada. Corrija `lab.py` e
volte a executar o mesmo comando.

## Checkpoint final

As funções de dígitos funcionam para `0`, números terminados em zero e números
sem algarismos do tipo pedido; a série usa um ciclo linear em `n`.
