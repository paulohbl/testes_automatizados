# Módulo 3: Testes em Software Orientado a Objetos

Este diretório contém exemplos práticos em Python ilustrando os conceitos fundamentais de testabilidade, princípios SOLID aplicados a testes e o uso de Dublês de Teste apresentados no material teórico do **Módulo 3**.

## Exemplos Implementados

### 1. Injeção de Dependência e Mocks (`app.py` & `test_app.py`)
Demonstra o Laboratório Prático de Isolamento de Serviços de Nuvem (Seção 5 do PDF):
*   **Código de Produção (`app.py`):** Define a classe `ProcessadorNegocio`, que depende de um serviço de log (`LoggerNuvem`). Em vez de acoplar rigidamente instanciando o logger internamente, a dependência é injetada via construtor.
*   **Código de Teste (`test_app.py`):** Utiliza o `unittest.mock.Mock` para isolar a dependência externa. Isso permite testar a lógica do processador sem precisar de conexões com redes reais ou chaves de acesso à nuvem.

### 2. Anatomia dos Dublês de Teste (`dubles.py` & `test_dubles.py`)
Demonstra de forma isolada e prática a diferença conceitual e de uso dos 4 tipos principais de Dublês de Teste (Seção 3 do PDF):
*   **Stub (Substituto de Resposta):** Focado no *estado*. Simula respostas enlatadas (ex: retornar sempre `True` para pagamentos válidos e `False` para inválidos) permitindo testar caminhos do código que dependem destas respostas.
*   **Mock (Substituto de Comportamento):** Focado na *interação*. Valida se métodos específicos do dublê foram executados com os parâmetros corretos durante o teste.
*   **Fake (Simulador Leve):** Uma implementação de fato executável, porém muito simplificada. Aqui simulamos um banco de dados real em memória através de um dicionário (`FakeDatabase`), eliminando a necessidade de conectar a um banco real (MySQL/PostgreSQL).
*   **Spy (Observador):** Embrulha um objeto de produção real (`Calculadora`) para capturar parâmetros de chamadas e interações ocorridas, sem interferir na lógica de cálculo real.

---

## Como Executar

### Pré-requisitos
Certifique-se de que possui o ambiente Conda configurado e ativado. Se ainda não o fez, instale as dependências a partir da pasta raiz `Codes/`:
```bash
conda activate testes-automatizados
```

### Executando os Códigos Interativos
Para ver os exemplos funcionando de forma demonstrativa no console:
```bash
python app.py
python dubles.py
```

### Executando os Testes com Pytest
Para rodar a suíte de testes do Módulo 3 e verificar o isolamento das dependências:
```bash
pytest -v
```

### Medindo a Cobertura de Código
Caso queira gerar o relatório de cobertura de código do laboratório prático:
```bash
pytest --cov=app test_app.py --cov-report=term-missing
```
