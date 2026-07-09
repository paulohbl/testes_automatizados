# Módulo 5: Automação de Testes em Aplicações Móveis

Este diretório contém exemplos práticos em Python e YAML ilustrando os conceitos fundamentais de automação de testes End-to-End (E2E) em dispositivos e aplicações móveis apresentados no material teórico do **Módulo 5**.

## Conceitos Demonstrados

### 1. Desafios de Testes Mobile
*   **Fragmentação Extrema:** A variação de tamanhos de tela, DPIs, fabricantes e customizações do Android, e diferentes versões do iOS.
*   **Emuladores vs. Dispositivos Reais:** O uso estratégico de emuladores para velocidade e paralelismo em integração contínua (CI/CD) versus dispositivos reais (ou *Device Farms* em nuvem) para fidelidade e testes físicos (bateria, rede, GPS).
*   **Interações Físicas:** Simulação ergonômica de toques complexos, como *Swipe* (deslizar), *Pinch* (zoom) e interrupções do aparelho (ligações, notificações).

### 2. Estratégias de Localizadores (Locators) no Mobile
*   **Accessibility ID (Padrão Ouro):** Baseado nas propriedades de acessibilidade dos elementos (`content-desc` no Android e `accessibilityIdentifier` no iOS). É a forma mais robusta e independente de layout ou traduções.
*   **ID Nativo:** Baseado no `resource-id` do sistema Android. É rápido, mas necessita de instrumentação de código.
*   **XPath:** Deve ser **evitado no mobile**, pois o custo computacional de varredura estrutural em tempo real de árvores XML nativas é muito alto, tornando os testes lentos e suscetíveis a quebras (*flaky*).

---

## Exemplos Implementados

### 1. Appium com Python (`test_appium.py`)
Implementa um cenário clássico de automação móvel:
*   Configuração das *Desired Capabilities* (`caps`) direcionadas ao emulador Android.
*   Conexão remota ao servidor Appium (`http://localhost:4723`).
*   Uso de `WebDriverWait` e `AppiumBy` para localizar e clicar em botões, preencher formulários e salvar o registro na agenda de contatos.

### 2. Maestro Studio (`contato.yaml`)
Demonstra a nova geração de testes declarativos (*low-code*):
*   Sintaxe limpa em formato YAML.
*   Inicialização zerada do aplicativo (`launchApp` com `clearState: true`).
*   Seleção dinâmica baseada em acessibilidade e texto visível na tela de forma simplificada, abstraindo a espera assíncrona.
*   Validação visual de sucesso com `assertVisible`.

---

## Como Executar os Testes

### 1. Atualizar e Ativar o Ambiente Conda
Garanta que as dependências móveis (incluindo o cliente do Appium) estejam instaladas:
```bash
conda env update -f ../environment.yml
conda activate testes-automatizados
```

### 2. Executando os Testes do Appium
1. **Iniciar o Servidor Appium:**
   Garanta que você tem o Appium instalado e rodando em sua máquina (geralmente em `http://localhost:4723`):
   ```bash
   appium
   ```
2. **Iniciar o Emulador Android:**
   Garanta que um emulador com as configurações correspondentes (ex: `Pixel_API_33`) esteja aberto e ativo.
3. **Disparar o Pytest:**
   ```bash
   pytest test_appium.py -v
   ```

### 3. Executando os Testes do Maestro Studio
Certifique-se de que o emulador está aberto e execute o comando:
```bash
maestro test contato.yaml
```

---

## Guia de Instalação e Configuração (Windows)

Caso ainda não possua o ambiente de testes móveis configurado em seu computador, siga os passos abaixo para configurar o ecossistema local:

### 1. Instalação do Node.js e Appium
O servidor do Appium necessita do ambiente Node.js para execução:
1. Baixe e instale a versão **LTS** recomendada em [nodejs.org](https://nodejs.org/).
2. Abra um terminal e execute o comando abaixo para instalar o Appium globalmente:
   ```bash
   npm install -g appium
   ```
3. Instale o driver nativo para Android (UiAutomator2):
   ```bash
   appium driver install uiautomator2
   ```

### 2. Configuração do Android SDK e Variáveis de Ambiente
O SDK do Android é o conjunto de ferramentas utilizadas para compilar e interagir com emuladores. No Windows, seu caminho padrão é:
📂 `C:\Users\IFMT\AppData\Local\Android\Sdk`

Certifique-se de que as seguintes variáveis de ambiente estejam devidamente configuradas em seu sistema operacional:
1. Defina a variável de ambiente **`ANDROID_HOME`** apontando para o caminho do SDK acima.
2. Adicione os seguintes diretórios no seu **`Path`** de usuário:
   * `%ANDROID_HOME%\platform-tools` (onde reside o utilitário `adb`)
   * `%ANDROID_HOME%\emulator` (utilizado para inicializar e gerenciar emuladores virtuais)

### 3. Java Development Kit (JDK)
Garanta que você tem o JDK instalado (por exemplo, a versão Eclipse Adoptium JDK-21) e a variável **`JAVA_HOME`** configurada apontando para a pasta principal de instalação do JDK.

### 4. Instalação do Maestro CLI
Para instalar a interface de linha de comando (CLI) do Maestro:
*   **Via Terminal (Bash/WSL/macOS/Linux):**
    ```bash
    curl -Ls "https://get.maestro.mobile.dev" | bash
    ```
*   **Instalação Manual / Documentação:**
    Para obter instruções detalhadas ou download manual, visite a página oficial de instalação do Maestro:
    👉 [maestro.mobile.dev/getting-started/installation](https://maestro.mobile.dev/getting-started/installation)

### 5. Validação de Dependências (Opcional)
Para auditar se todo o ambiente móvel está pronto e sem erros, você pode utilizar a ferramenta utilitária `appium-doctor`:
```bash
npm install -g appium-doctor
appium-doctor --android
```

