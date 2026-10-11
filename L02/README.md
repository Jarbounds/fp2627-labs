---
title: "L02 - Elementos Básicos e Condicionais"
subtitle: "Fundamentos de Programação 2026-2027"
lang: pt-PT
---

## Pré-requisitos

Expressões, atribuições, tipos numéricos, comparação, condicionais e funções
simples.

## Objetivos

- decompor cálculos em auxiliares legíveis;
- separar casos com condicionais sem duplicar contas;
- representar resultados compostos como texto formatado quando ainda não há
  coleções estruturadas;
- testar casos de fronteira antes de acrescentar variantes.

## Exercícios

O enunciado abaixo é auto-contido: não é necessário consultar `lab.py` para
perceber o que cada função deve fazer. Durante a aula, resolva em papel,
escrevendo para cada função a assinatura, o algoritmo em Python ou pseudocódigo
Python, os casos de erro e exemplos de chamada com resultado. Quando tiver
computador, transcreva as soluções para `lab.py`, substituindo os marcadores
`TODO`.

1. `bissexto(ano)` recebe um inteiro correspondente a um ano e devolve `True`
   se o ano for bissexto. Um ano é bissexto se for divisível por `4` e não for
   divisível por `100`, exceto quando também é divisível por `400`. Assim,
   `bissexto(1984)` e `bissexto(2000)` devolvem `True`, mas `bissexto(1900)`
   devolve `False`.
2. `dias_mes(mes, ano)` recebe um mês entre `1` e `12` e um ano, e devolve o
   número de dias desse mês. Fevereiro tem `29` dias em anos bissextos e `28`
   nos restantes. Se `mes` estiver fora do intervalo `1..12`, levanta
   `ValueError`.
3. `data_valida(dia, mes, ano)` devolve `True` se `dia/mes/ano` for uma data
   válida no calendário simplificado desta ficha, e `False` caso contrário. A
   função deve reutilizar `dias_mes` sem deixar escapar o `ValueError` dos meses
   inválidos. Por exemplo, `data_valida(29, 2, 2024)` devolve `True`, mas
   `data_valida(29, 2, 2023)` e `data_valida(31, 4, 2024)` devolvem `False`.
4. `dias_de_segundos(segundos)` recebe um inteiro não negativo e devolve o
   número real de dias correspondente. Se o
   argumento for negativo, levanta `ValueError`.
5. `decompor_segundos(segundos)` recebe um inteiro não negativo e devolve o
   tuplo `(dias, horas, mins, segs)`. Cada
   campo deve ficar no intervalo natural da unidade: horas entre `0` e `23`,
   minutos e segundos entre `0` e `59`. Por exemplo, `90061` devolve
   `(1, 1, 1, 1)`. Se o argumento for negativo, levanta `ValueError`.
6. `formatar_duracao(segundos)` devolve exatamente a string
   `"dias: D; horas: H; mins: M; segs: S"`, preenchendo `D`, `H`, `M` e `S`
   com o resultado de `decompor_segundos`. Por exemplo, `formatar_duracao(0)`
   devolve `"dias: 0; horas: 0; mins: 0; segs: 0"`.
7. `maior_de_tres(a, b, c)` devolve o maior dos três valores. Empates são
   resolvidos naturalmente pelo próprio valor máximo: `maior_de_tres(4, 4, 2)`
   devolve `4`.
8. `salario_semanal(horas, preco_hora)` recebe valores não negativos. Até `40`
   horas, devolve `horas * preco_hora`; as horas acima de `40` são pagas a
   dobrar. Por exemplo, `salario_semanal(45, 10)` devolve `500`. Se algum
   argumento for negativo, levanta `ValueError`.
9. `troco_centimos(total)` recebe uma quantia inteira em cêntimos e devolve uma
   string com o menor número de notas/moedas, da denominação maior para a menor.
   Use as denominações `5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2,
   1`. Cada parcela aparece como `"denominacao:quantidade"` e as parcelas são
   separadas por `"; "`. Não inclua denominações usadas zero vezes. Por exemplo,
   `troco_centimos(388)` devolve `"200:1; 100:1; 50:1; 20:1; 10:1; 5:1; 2:1; 1:1"`.
   `troco_centimos(0)` devolve `""`; valores negativos levantam `ValueError`.
10. `tarifa_envio(peso_g, urgente=False)` recebe um peso inteiro positivo em
   gramas e devolve o preço em cêntimos. Até `100` g custa `120`; até `500` g
   custa `250`; até `2000` g custa `500`; acima disso custa `500` mais `300`
   por cada bloco iniciado de `1000` g adicional. Se `urgente` for `True`,
   acrescente `40%` e arredonde para cima. Peso menor ou igual a zero levanta
   `ValueError`.

### Testes públicos

O ficheiro `test_lab.py` contém chamadas já preparadas para verificar os casos
principais desta ficha. Depois de completar `lab.py`, abra o terminal na pasta
`labs/student/L02` e execute:

```sh
python3 test_lab.py
```

Se tudo estiver correto, o processo termina com `OK - L02`. Se houver falha,
leia a primeira mensagem de erro: ela indica uma chamada que não devolveu o
resultado esperado ou uma exceção que não foi levantada. Corrija `lab.py` e
volte a executar o mesmo comando.

## Checkpoint final

Todos os exercícios têm pelo menos um teste de fronteira: fevereiro em ano
bissexto e comum, zero segundos, 40 horas, empate no máximo, troco sem resto e
tarifário no limite de escalão.
