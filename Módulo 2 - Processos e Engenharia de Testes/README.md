# Módulo 2: Processos e Engenharia de Testes

Este diretório contém exemplos práticos em Python ilustrando os conceitos fundamentais apresentados no material teórico do **Módulo 2**.

## Conceitos Demonstrados

### 1. TDD e Cobertura de Código (`validador.py` & `test_validador.py`)
Demonstra o ciclo **Red-Green-Refactor**:
*   **Fase RED:** Escrever os testes em `test_validador.py` antes que a função exista, garantindo a falha inicial.
*   **Fase GREEN:** Escrever o código mínimo em `validador.py` para fazer os testes passarem.
*   **Fase REFACTOR:** Otimizar e limpar o código de produção mantendo a suíte de testes verde.
*   **Caixa Branca (Cobertura):** Utiliza o `pytest-cov` para medir as linhas de código e caminhos lógicos testados.

### 2. Técnicas de Caixa Preta (`projeto_testes.py` & `test_projeto_testes.py`)
Aplica técnicas estruturadas de projeto de testes baseadas na especificação de que a idade de cadastro deve ser de 18 a 65 anos:
*   **Partição de Equivalência (PE):** Agrupa os valores em classes válidas e inválidas, testando apenas um representante de cada grupo:
    *   *Partição Inválida (Menor):* ex: `15`
    *   *Partição Válida:* ex: `30`
    *   *Partição Inválida (Maior):* ex: `70`
*   **Análise de Valor Limite (AVL):** Foca nas fronteiras exatas da decisão condicional:
    *   *Limites Inferiores:* `17` (inválido) e `18` (válido)
    *   *Limites Superiores:* `65` (válido) e `66` (inválido)

### 3. BDD - Behavior-Driven Development (`features/bloqueio.feature` & `features/steps/bloqueio_steps.py`)
Utiliza o framework **`behave`** (o padrão oficial do Python para Cucumber BDD) para realizar a ligação automática entre a especificação de negócio escrita em texto livre Gherkin e o código de teste automatizado utilizando decoradores (`@given`, `@when`, `@then`).
*   **Código de Produção:** [autenticacao.py](./autenticacao.py)
*   **Arquivo de Especificação:** [features/bloqueio.feature](./features/bloqueio.feature)
*   **Step Definitions:** [features/steps/bloqueio_steps.py](./features/steps/bloqueio_steps.py)

---

## Como Executar

### Pré-requisitos
Garanta que possui o ambiente Conda configurado e ativado. Se ainda não o fez, instale as dependências atualizadas na pasta `Codes/` (que agora inclui o `behave` e `pytest-cov`):
```bash
conda env update -f ../environment.yml
conda activate testes-automatizados
```

### Executando os Testes Unitários e de Caixa Preta com Pytest
Para rodar a suíte de testes do Pytest:
```bash
pytest -v
```

### Executando os Testes BDD com Behave
Para rodar o cenário de testes BDD utilizando o `behave`:
```bash
behave
```

### Medindo a Cobertura de Código (Caixa Branca)
Para gerar o relatório de cobertura detalhado do nosso TDD (validador):
```bash
pytest --cov=validador test_validador.py --cov-report=term-missing
```

A saída exibirá o total de declarações (Stmts), falhas (Miss) e a porcentagem total de cobertura do código.
