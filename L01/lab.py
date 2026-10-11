def mensagem_boas_vindas(nome: str, cadeira: str) -> str:
    """Devolve uma mensagem de boas-vindas personalizada."""
    return f'{nome}, bem-vindo/a a {cadeira}!'


def area_retangulo(largura: float, altura: float) -> float:
    return largura * altura


def total_servico(horas: float, preco_hora: float) -> float:
    """Calcula o total com IVA a 23% para um serviço."""
    subtotal = horas * preco_hora
    iva = subtotal * 0.23
    total = subtotal + iva
    return total


def formatar_fatura(descricao: str, horas: float, preco_hora: float) -> str:
    """Devolve uma linha como 'Apoio tecnico: 24.60 euros'."""
    total = total_servico(horas, preco_hora)
    return f'{descricao}: {total:.2f} euros'


def formatar_fatura_sessoes(
    descricao: str,
    sessoes: int,
    horas: float,
    preco_hora: float,
) -> str:
    """Devolve uma linha de fatura para várias sessões iguais."""
    total_sessao = total_servico(horas, preco_hora)
    total = total_sessao * sessoes
    return f'{descricao}: {total:.2f} euros'


def classificar_erro(descricao: str) -> str:
    """Devolve 'sintaxe', 'execucao', 'logica' ou 'desconhecido'."""
    if "SyntaxError" in descricao:
        return "sintaxe"
    elif "ValueError" in descricao:
        return "execucao"
    return "logica"