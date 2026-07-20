# Módulo 7: Testes Não Funcionais (Performance, Carga e Estresse)

Este diretório contém exemplos práticos demonstrando testes de carga, estresse e pico usando ferramentas modernas baseadas em código: **k6** e **Locust**.

## Estrutura do Módulo

1. **`app.py`**: API REST mock construída em Flask que simula endpoints reais de produtos com latência variável para testes locais.
2. **`script-carga.js`**: Script de teste de carga escrito para rodar com o **k6** em JavaScript.
3. **`locustfile.py`**: Script de teste de estresse escrito para rodar com o **Locust** em Python.

---

## Como Executar os Exemplos

### Passo 1: Iniciar a API Local Mock
Ative o ambiente conda do curso e inicie o servidor Flask:
```bash
conda activate testes-automatizados
python app.py
```
Isso iniciará o servidor na URL `http://localhost:5000`.

---

### Passo 2: Executar Testes com Locust

Com o servidor Flask rodando em um terminal, abra um segundo terminal e execute:
```bash
conda activate testes-automatizados
locust -f locustfile.py --host=http://localhost:5000
```

1. Acesse o painel web do Locust abrindo `http://localhost:8089` no seu navegador.
2. Configure o número de usuários (ex: `50`) e a taxa de ramp-up (ex: `5` usuários por segundo).
3. Clique em **Start swarming** e observe em tempo real as métricas de requisições, latências médias e percentis na aba gráfica.

---

### Passo 3: Executar Testes com k6

O **k6** é executado por meio de um binário local de alta performance. Caso queira testá-lo manualmente:
1. Faça o download no site oficial: [https://k6.io](https://k6.io) ou instale via gerenciador de pacotes do Windows (como o winget):
   ```powershell
   winget install grafana.k6
   ```
2. Após a instalação, execute o teste de carga:
   ```bash
   k6 run script-carga.js
   ```
3. O k6 imprimirá um relatório estatístico completo diretamente no terminal ao final do teste (contendo tempo de resposta médio, mediana, p90, p95 e falhas).
