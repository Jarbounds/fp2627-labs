---
title: "L04 - Funções e Abstração de Dados"
subtitle: "Fundamentos de Programação 2026-2027"
lang: pt-PT
---

## Pré-requisitos

Funções, tuplos, validação, construtores, seletores e operações de alto nível
sobre uma representação escondida.

## Objetivos

- escolher uma representação interna simples para um TAD;
- manter clientes afastados da representação concreta;
- validar invariantes no construtor;
- implementar operações novas apenas com a interface pública.

## Exercícios

Nesta ficha vai implementar um TAD para relógios dentro de um dia. Um relógio
guarda horas, minutos e segundos válidos.

O enunciado abaixo é auto-contido: não é necessário consultar `lab.py` para
perceber o que cada função deve fazer. Durante a aula, resolva em papel a
interface do TAD: escolha a representação, escreva as assinaturas, indique que
invariantes o construtor mantém e desenvolva cada operação em Python ou
pseudocódigo Python. Para cada operação de alto nível, inclua exemplos de
chamada. Quando tiver computador, transcreva as soluções para `lab.py`,
substituindo os marcadores `TODO`.

1. `cria_relogio(h, m, s)` constrói um relógio. As horas têm de estar entre
   `0` e `23`; minutos e segundos entre `0` e `59`. Valores fora destes
   intervalos levantam `ValueError`. Os seletores `horas(r)`, `minutos(r)` e
   `segundos(r)` devolvem cada componente sem expor a representação interna.
2. `escreve_relogio(r)` devolve uma string no formato `hh:mm:ss`, sempre com
   dois algarismos por campo. Por exemplo, um relógio criado com `(9, 2, 34)`
   deve ser escrito como `"09:02:34"`.
3. `mesmas_horas(r1, r2)` devolve `True` se os dois relógios representam o
   mesmo instante do dia. `depois_rel(r1, r2)` devolve `True` apenas se `r2`
   for posterior a `r1` no mesmo dia; relógios iguais não contam como
   posteriores.
4. `dif_segs(r1, r2)` devolve o número de segundos entre `r1` e `r2`, assumindo
   que `r2` é posterior a `r1`. Por exemplo, entre `10:02:34` e `11:21:34` há
   `4740` segundos. Se `r2` não for posterior, levanta `ValueError`.
5. `avanca(r, delta)` recebe um relógio e um número não negativo de segundos,
   e devolve um novo relógio avançado esse tempo. Se passar a meia-noite, deve
   rodar dentro do mesmo dia: `23:59:50` avançado `15` segundos dá `00:00:05`.
   `delta < 0` levanta `ValueError`.
6. `intervalos_validos(inicio, duracoes)` recebe um relógio inicial e um tuplo
   de durações não negativas em segundos. Devolve um tuplo com os relógios
   obtidos após aplicar cada duração sucessivamente. Com início `08:00:00` e
   durações `(60, 3600, 30)`, o resultado contém, por esta ordem, `08:01:00`,
   `09:01:00` e `09:01:30`.

### Testes públicos

O ficheiro `test_lab.py` contém chamadas já preparadas para verificar os casos
principais desta ficha. Depois de completar `lab.py`, abra o terminal na pasta
`labs/student/L04` e execute:

```sh
python3 test_lab.py
```

Se tudo estiver correto, o processo termina com `OK - L04`. Se houver falha,
leia a primeira mensagem de erro: ela indica uma chamada que não devolveu o
resultado esperado ou uma exceção que não foi levantada. Corrija `lab.py` e
volte a executar o mesmo comando.

## Checkpoint final

Altere mentalmente a representação interna: apenas construtor e seletores
deveriam mudar; as operações de alto nível continuam apoiadas na interface.
