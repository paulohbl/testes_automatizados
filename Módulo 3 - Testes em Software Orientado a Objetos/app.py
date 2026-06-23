"""
Módulo 3: Testes em Software Orientado a Objetos
Laboratório Prático: Isolamento de Serviços de Nuvem (Código de Produção)

Este arquivo demonstra a importância da Injeção de Dependência para a testabilidade.
A classe ProcessadorNegocio depende de um logger, mas em vez de instanciar diretamente
uma classe concreta que se comunica com a nuvem (LoggerNuvem), ela recebe a dependência
em seu construtor (Injeção de Dependência). Isso nos permite isolar o serviço de nuvem
usando um Dublê de Teste (Mock) nos testes de unidade.
"""

class LoggerNuvem:
    """
    Simula um logger real que envia registros para um serviço na nuvem (ex: AWS S3).
    Em produção, essa operação dependeria de credenciais válidas e de conexão com a rede.
    """
    def salvar(self, log: str) -> bool:
        # Simulando uma chamada complexa de rede
        print(f"[NUVEM] Enviando para a nuvem: '{log}'...")
        # Em um cenário real, haveria código aqui para enviar os dados via HTTP/SDK
        return True


class ProcessadorNegocio:
    """
    Contém a lógica de negócio do sistema.
    Utiliza Injeção de Dependência pelo construtor para receber o serviço de log.
    """
    def __init__(self, logger):
        # [INJEÇÃO DE DEPENDÊNCIA]: O processador não instancia LoggerNuvem diretamente,
        # o que evita o acoplamento rígido e permite a substituição por um Mock nos testes.
        self.logger = logger

    def processar(self, dado: str) -> str:
        if not dado:
            return "Erro"
            
        resultado = f"Processado: {dado}"
        
        # [CHAMADA EXTERNA]: Salva o log utilizando a dependência injetada.
        self.logger.salvar(resultado)
        
        return resultado


if __name__ == "__main__":
    print("--- Execução do Código de Produção (Sem Mock) ---")
    # Em produção, instanciamos a dependência real
    logger_real = LoggerNuvem()
    processador = ProcessadorNegocio(logger_real)
    
    # Processa um dado válido, gerando uma chamada simulada à nuvem
    print("\nProcessando dado válido:")
    res = processador.processar("Venda #101")
    print(f"Resultado final: {res}")
    
    # Processa um dado inválido (sem gerar logs)
    print("\nProcessando dado inválido:")
    res_erro = processador.processar("")
    print(f"Resultado final: {res_erro}")
