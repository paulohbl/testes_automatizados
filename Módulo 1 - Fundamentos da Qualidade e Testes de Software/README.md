# Módulo 1: Fundamentos da Qualidade e Testes de Software

Este diretório contém exemplos práticos em Python ilustrando os conceitos fundamentais apresentados no material teórico do **Módulo 1**.

## Exemplos Implementados

### 1. Cadeia de Problemas (`cadeia_problemas.py` & `test_cadeia_problemas.py`)
Demonstra como o erro humano resulta em um defeito no código e, posteriormente, em uma falha de sistema durante a execução:
*   **Erro (Mistake):** O desenvolvedor assume incorretamente que o divisor de uma operação de divisão nunca será zero e não adiciona tratamento de entrada.
*   **Defeito (Bug/Fault):** O método `dividir` não possui proteção ou tratamento de exceção em sua implementação.
*   **Falha (Failure):** Ao chamar `dividir(10, 0)`, o programa trava exibindo uma exceção `ZeroDivisionError`.

### 2. Verificação vs Validação (`verificacao_validacao.py` & `test_verificacao_validacao.py`)
Demonstra a diferença crucial entre os dois processos:
*   **Verificação ("Construímos o produto corretamente?"):** Garante que o cálculo das taxas administrativas do boleto obedece à especificação matemática (2% do valor nominal, mínimo R$ 2,00 e máximo R$ 10,00). Pode ser 100% verificado com testes automatizados.
*   **Validação ("Construímos o produto correto?"):** Garante que atende à necessidade do usuário. O sistema força o usuário a digitar o CPF formatado estritamente com pontos e traços. Se ele digitar apenas números, a operação falha com um erro técnico incompreensível. Mesmo que as taxas estejam calculadas corretamente (Verificação OK), o produto falha em satisfazer o usuário real (Falha de Validação).

---

## Como Executar

### Pré-requisitos
Certifique-se de que possui o **Conda** ou o **Python 3.10+** com **Pip** instalado no sistema.

### Opção A: Utilizando Conda (Recomendado)
1. Crie o ambiente a partir do arquivo na pasta Codes:
   ```bash
   conda env create -f ../environment.yml
   ```
2. Ative o ambiente criado:
   ```bash
   conda activate testes-automatizados
   ```

### Opção B: Utilizando Pip
1. Instale as dependências a partir do arquivo na pasta Codes:
   ```bash
   pip install -r ../requirements.txt
   ```

### Executando os Códigos Interativos
Para ver os exemplos funcionando no console:
```bash
python cadeia_problemas.py
python verificacao_validacao.py
```

### Executando os Testes com Pytest
Para rodar os testes automatizados e verificar o comportamento esperado:
```bash
pytest -v
```
