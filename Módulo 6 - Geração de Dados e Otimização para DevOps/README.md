# Módulo 6: Geração de Dados e Otimização para DevOps

Este diretório contém exemplos práticos em Python e YAML ilustrando as técnicas fundamentais de gerenciamento de massa de dados e execução em pipelines de Integração Contínua (CI) apresentadas no material teórico do **Módulo 6**.

## Conceitos Demonstrados

### 1. Testes Intermitentes (Flaky Tests)
*   **Problema de Estado:** Testes que falham de forma imprevisível devido à dependência de dados fixos ou estado compartilhado no banco de dados.
*   **Solução Stateless:** Projetar testes isolados e independentes. O teste deve criar os dados de que precisa e limpá-los ao finalizar, garantindo a integridade do ambiente.

### 2. Geração Dinâmica de Massa de Dados (Faker)
*   Uso de dados dinâmicos e randômicos realistas em vez de dados estáticos hardcoded. 
*   Evita colisões em restrições de unicidade (como CPFs ou e-mails únicos) no banco de dados.

### 3. Ciclo de Vida dos Testes (Fixtures com Setup e Teardown)
*   **Setup:** Preparação automatizada do cenário de teste (geração de dados dinâmicos).
*   **Teardown:** Limpeza obrigatória do banco de dados e liberação de recursos após a conclusão do teste (mesmo se o teste falhar no meio do fluxo).

### 4. Execução em Pipeline (DevOps e Modo Headless)
*   **Modo Headless:** Execução de navegadores (Chrome, Firefox, etc.) sem interface gráfica física, ideal para servidores de CI. A aceleração de processamento pode ser de 2 a 5 vezes mais rápida.
*   **Quality Gates:** Barreiras de qualidade automatizadas no pipeline que impedem a integração de códigos quebrados ou instáveis no repositório principal.

---

## Exemplos Implementados

### 1. Fixtures e Faker (`test_faker_fixtures.py`)
Um script completo utilizando o `pytest` e a biblioteca `Faker` (configurada no padrão brasileiro):
*   Uma fixture (`gerar_dados_usuario`) com lógica de `Setup` e `Teardown` usando `yield`.
*   Impressão explicativa do fluxo de execução no terminal para facilitar a visualização didática do ciclo de vida.
*   Validações e asserções nos dados sintéticos gerados.

### 2. Pipeline E2E GitHub Actions (`ci.yml`)
Exemplo de arquivo de fluxo orquestrador (`.github/workflows/ci.yml`) contendo:
*   Disparador automático a cada `push` nas branches `main` e `homolog`.
*   Provisionamento de máquina Linux enxuta (`ubuntu-latest`).
*   Instalação das dependências e navegadores dinâmicos para rodar a suíte em modo headless.

---

## Como Executar os Testes

### 1. Atualizar e Ativar o Ambiente Conda
Garanta que as dependências adicionais (como a biblioteca `faker`) estejam devidamente instaladas:
```bash
conda env update -f ../environment.yml
conda activate testes-automatizados
```

### 2. Executando os Testes Unitários e Fixtures
Execute o teste local ativando a exibição de logs de terminal (`-s` ou `--capture=no`) para poder visualizar o fluxo de **Setup** e **Teardown** em ação:
```bash
pytest test_faker_fixtures.py -v -s
```
*(Nota: O parâmetro `-s` permite que os `print()` colocados na Fixture e no teste apareçam diretamente no console).*
