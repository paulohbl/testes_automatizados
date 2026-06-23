"""
Módulo 2: Processos e Engenharia de Testes
Sistema de Autenticação (Código de Produção)
"""

class SistemaAutenticacao:
    def __init__(self):
        # Estado em memória das contas de usuário
        self.contas = {
            "admin_x": {
                "ativa": True,
                "bloqueada": False,
                "tentativas_falhas": 0,
                "tempo_bloqueio_minutos": 0,
                "email_alerta_enviado": False
            }
        }
        self.na_tela_de_login = False

    def ir_para_tela_login(self):
        self.na_tela_de_login = True

    def tentar_login(self, usuario: str, senha_digitada: str) -> bool:
        if not self.na_tela_de_login:
            raise RuntimeError("Usuário precisa estar na tela de login para tentar logar.")
            
        conta = self.contas.get(usuario)
        if not conta:
            return False
            
        if conta["bloqueada"]:
            return False
            
        # Simula a senha correta
        senha_correta = "senha_correta_123"
        if senha_digitada == senha_correta:
            conta["tentativas_falhas"] = 0
            return True
        else:
            conta["tentativas_falhas"] += 1
            if conta["tentativas_falhas"] >= 3:
                conta["bloqueada"] = True
                conta["tempo_bloqueio_minutos"] = 15
                self._enviar_email_seguranca(usuario)
            return False

    def _enviar_email_seguranca(self, usuario: str):
        # Envia e-mail simulado ao setor de segurança cibernética
        self.contas[usuario]["email_alerta_enviado"] = True
