# Módulo 4: Automação de Testes em Aplicações Web

Este diretório contém exemplos práticos em Python e YAML ilustrando os conceitos fundamentais de automação de testes End-to-End (E2E) em aplicações Web apresentados no material teórico do **Módulo 4**.

## Conceitos Demonstrados

### 1. O DOM (Document Object Model) e Sincronização
*   **DOM:** A árvore de elementos que representa a página web em memória. Os testes interagem simulando cliques e digitações nesta árvore.
*   **Assincronia e Esperas:** O grande desafio da automação web é o tempo de resposta da rede. É demonstrado o perigo de usar esperas fixas (`time.sleep()`), que atrasam a suíte, em contraposição a esperas explícitas (`WebDriverWait` no Selenium) ou esperas dinâmicas automáticas (*Auto-waiting* no Playwright).

### 2. Estratégias de Localizadores (Locators)
Compara a resiliência de diferentes formas de se achar um elemento no DOM:
*   **XPath Absoluto:** Frágil e deve ser evitado a todo custo (ex: `/html/body/div[2]/form/button`).
*   **XPath Relativo:** Útil para navegar em estruturas complexas (ex: `//button[text()='Enviar']`).
*   **CSS Selectors:** Rápido e baseado em classes/estilos de design.
*   **ID HTML:** Rápido e direto, porém arriscado se os IDs forem gerados dinamicamente por frameworks modernos.
*   **Atributos de QA (Padrão Ouro):** A melhor prática do mercado. Uso de atributos dedicados exclusivamente a testes (como `data-testid` ou `data-test`), isolando os testes de mudanças visuais e de design na página.

---

## Exemplos Implementados

### 1. Selenium WebDriver (`test_selenium.py`)
Utiliza a abordagem clássica de automação de testes web com o Selenium:
*   Inicialização e encerramento controlado do `webdriver`.
*   Localização via `By.ID`.
*   Sincronização via `WebDriverWait` com condições esperadas (`EC.visibility_of_element_located`).

### 2. Playwright (`test_playwright.py`)
Utiliza o framework moderno da Microsoft:
*   Sintaxe limpa utilizando o plugin `pytest-playwright` que injeta o objeto `page`.
*   Seletores resilientes através do atributo customizado `data-test`.
*   Asserções inteligentes baseadas na função `expect`, que executa Auto-waiting de forma nativa.

### 3. Maestro (`fluxo_login.yaml`)
Um exemplo de fluxo declarativo YAML voltado para testes mobile/web emulados sem a necessidade de codificar em linguagens tradicionais, utilizando seletores e OCR nativo.

---

## Como Executar os Testes

### 1. Atualizar e Ativar o Ambiente Conda
Caso ainda não tenha atualizado o ambiente com as dependências do Módulo 4:
```bash
conda env update -f ../environment.yml
conda activate testes-automatizados
```

### 2. Instalar os Navegadores do Playwright
O Playwright precisa baixar seus próprios navegadores otimizados (como Chromium, Firefox e WebKit). Execute:
```bash
playwright install chromium
```

### 3. Executando os Testes do Selenium e Playwright com Pytest
Para rodar a suíte inteira de testes na pasta atual:
```bash
pytest -v
```
*(Nota: Por padrão, o Playwright roda no modo **headless** (sem abrir a janela do navegador) para melhor desempenho. Se quiser ver o navegador abrindo na tela, adicione o parâmetro `--headed` ao rodar o comando: `pytest -v --headed`).*

### 4. Executando os Testes do Maestro (Web)
O Maestro permite executar testes declarativos em aplicações Web (usando navegadores baseados em Chromium).

#### Instalação do Maestro
*   **No macOS, Linux ou Windows (via WSL - Windows Subsystem for Linux):**
    Abra o terminal bash e execute o comando abaixo para realizar a instalação do Maestro CLI:
    ```bash
    curl -Ls "https://get.maestro.mobile.dev" | bash
    ```
*   **Configuração de Variáveis de Ambiente:**
    Certifique-se de que o executável está no seu `PATH`. Geralmente, a instalação adiciona automaticamente, mas caso precise exportar manualmente no seu `.bashrc`/`.zshrc`:
    ```bash
    export PATH="$PATH:$HOME/.maestro/bin"
    ```

#### Execução do Teste Web
Para rodar o fluxo declarativo de login no navegador web com o Maestro:
```bash
maestro test fluxo_login.yaml
```
*(Nota: O Maestro gerenciará automaticamente uma instância otimizada do Chromium local para realizar o passo a passo).*

