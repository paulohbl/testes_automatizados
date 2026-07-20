# locustfile.py
from locust import HttpUser, task, between

class UsuarioNavegando(HttpUser):
    # O Locust simula o usuário hesitando entre 1 e 3s a cada ação
    wait_time = between(1, 3)

    @task
    def consultar_catalogo(self):
        # Medirá automaticamente a latência e o % de falhas
        with self.client.get("/produtos", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"API quebrou com erro: {response.status_code}")

    @task(3) # Configuração de Peso: Este fluxo será focado 3x mais (visualizar destaque)
    def visualizar_produto_unico(self):
        self.client.get("/produtos/id_destaque_123")
