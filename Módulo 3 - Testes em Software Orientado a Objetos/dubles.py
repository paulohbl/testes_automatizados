"""
Módulo 3: Testes em Software Orientado a Objetos
Exemplos práticos da Anatomia dos Dublês de Teste (Test Doubles)

Este arquivo contém classes e funções de produção que servem de cenário para
a demonstração prática de:
1. Stub: Fornece respostas prontas (estado configurado) para o código sob teste.
2. Mock: Focado na verificação de comportamento (se uma chamada ocorreu e como).
3. Fake: Uma implementação real mais simples/leve (ex: banco de dados em memória).
4. Spy: Registra as interações feitas em um objeto real sem alterar seu comportamento.
"""

# -------------------------------------------------------------------------
# 1. Cenário para STUB (Substituto de Resposta)
# -------------------------------------------------------------------------
class AutorizadorPagamento:
    """
    Interface/Classe de produção que se comunica com um gateway externo
    (ex: PayPal, Stripe) para autorizar transações.
    """
    def autorizar(self, valor: float) -> bool:
        # Em produção, faria uma requisição HTTP para a API de pagamentos.
        print(f"[PRODUÇÃO] Enviando requisição de R$ {valor} ao gateway...")
        return False # Comportamento padrão fictício


class ProcessadorVendas:
    def __init__(self, autorizador: AutorizadorPagamento):
        self.autorizador = autorizador

    def realizar_venda(self, valor: float) -> str:
        # O processador de vendas depende da resposta do autorizador.
        if self.autorizador.autorizar(valor):
            return "Venda Aprovada"
        return "Venda Rejeitada"


# -------------------------------------------------------------------------
# 2. Cenário para MOCK (Substituto de Comportamento)
# -------------------------------------------------------------------------
class EnviadorEmail:
    """
    Classe de produção responsável por formatar e enviar e-mails via servidor SMTP.
    """
    def enviar_email(self, destinatario: str, mensagem: str) -> None:
        # Em produção, conecta no servidor SMTP real.
        print(f"[PRODUÇÃO] E-mail enviado para {destinatario}: {mensagem}")


class ServicoNotificacao:
    def __init__(self, enviador: EnviadorEmail):
        self.enviador = enviador

    def notificar_usuario(self, mensagem: str) -> None:
        # Envia um e-mail com a notificação
        self.enviador.enviar_email("usuario@email.com", mensagem)


# -------------------------------------------------------------------------
# 3. Cenário para FAKE (Simulador Leve)
# -------------------------------------------------------------------------
class FakeDatabase:
    """
    Um banco de dados em memória usando um dicionário padrão.
    Serve como substituto leve de um banco relacional real (como MySQL/PostgreSQL).
    """
    def __init__(self):
        self.dados = {}

    def salvar(self, id_registro: int, valor: str) -> None:
        self.dados[id_registro] = valor

    def buscar_por_id(self, id_registro: int) -> str:
        return self.dados.get(id_registro, None)


# -------------------------------------------------------------------------
# 4. Cenário para SPY (Observador / Espião)
# -------------------------------------------------------------------------
class Calculadora:
    """
    Uma classe de produção com lógica real simples.
    Será espionada para validar se os parâmetros corretos foram passados.
    """
    def somar(self, a: float, b: float) -> float:
        return a + b


if __name__ == "__main__":
    print("--- Execução Didática das Classes de Produção ---")
    
    # Exemplo rápido da Calculadora
    calc = Calculadora()
    print(f"Calculadora real: 2 + 3 = {calc.somar(2, 3)}")
    
    # Exemplo rápido do FakeDatabase
    db = FakeDatabase()
    db.salvar(1, "Professor Paulo")
    print(f"Fake Database busca id 1: {db.buscar_por_id(1)}")
