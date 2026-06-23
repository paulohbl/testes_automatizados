"""
Módulo 1: Fundamentos da Qualidade e Testes de Software
Exemplo: Verificação vs Validação (V&V)

- Verificação: "Construímos o produto corretamente?" 
  Garante que o software atende aos requisitos técnicos e especificações de design.
  Foco: Código, cálculos matemáticos, conformidade com a especificação técnica.

- Validação: "Construímos o produto correto?"
  Garante que o software atende às necessidades reais do cliente/usuário final.
  Foco: Experiência do usuário (UX), fluxos de negócio, satisfação da necessidade real.
"""

class GeradorBoleto:
    """
    Simula um gerador de boletos bancários para demonstrar os conceitos de V&V.
    """
    def __init__(self):
        self.taxa_minima = 2.00
        self.taxa_maxima = 10.00
        self.percentual_taxa = 0.02

    def calcular_taxa(self, valor_nominal: float) -> float:
        """
        Calcula a taxa administrativa do boleto.
        [ESPECIFICAÇÃO]: A taxa é de 2% do valor nominal, respeitando o mínimo
        de R$ 2,00 e o máximo de R$ 10,00.
        
        Este método pode ser VERIFICADO através de testes unitários automatizados.
        """
        if valor_nominal < 0:
            raise ValueError("O valor nominal não pode ser negativo.")
            
        taxa = valor_nominal * self.percentual_taxa
        
        if taxa < self.taxa_minima:
            return self.taxa_minima
        if taxa > self.taxa_maxima:
            return self.taxa_maxima
        return round(taxa, 2)

    def processar_fluxo_geracao(self, valor_nominal: float, cpf: str) -> dict:
        """
        Simula a geração do boleto com interface/interação com o usuário.
        
        [PROBLEMA DE VALIDAÇÃO]: Embora as taxas estejam matemáticas e tecnicamente corretas
        (Verificação aprovada), se a experiência de uso for confusa ou exigir formatos 
        desnecessariamente complexos, o usuário final não conseguirá usar o sistema.
        """
        # Exemplo: O sistema exige CPF estritamente formatado com pontos e traços.
        # Se o usuário digitar apenas números, o sistema lança um erro incompreensível.
        if len(cpf) != 14 or "." not in cpf or "-" not in cpf:
            return {
                "sucesso": False,
                "erro": "Erro crítico no banco de dados código 0x88912A. Operação abortada.", 
                # ^ Falha de Validação: Erro técnico confuso que impede o usuário de atingir seu objetivo.
                "boleto": None
            }
            
        taxa = self.calcular_taxa(valor_nominal)
        valor_total = valor_nominal + taxa
        
        return {
            "sucesso": True,
            "erro": None,
            "boleto": {
                "valor_original": valor_nominal,
                "taxa": taxa,
                "valor_total": valor_total,
                "codigo_barras": "34191.79001 01043.513184 91020.150008 7 90000000000000"
            }
        }

if __name__ == "__main__":
    print("--- Gerador de Boletos (Demonstração de Verificação vs Validação) ---")
    gerador = GeradorBoleto()
    
    # 1. Demonstração de VERIFICAÇÃO (Construímos o produto corretamente?)
    print("\n1. [VERIFICAÇÃO]: Validando os cálculos matemáticos da taxa...")
    valores = [50.00, 300.00, 1000.00]
    for v in valores:
        taxa = gerador.calcular_taxa(v)
        print(f"  Valor do Boleto: R$ {v:.2f} -> Taxa Calculada: R$ {taxa:.2f}")
    print("  -> Cálculos corretos conforme a especificação técnica. Verificação: APROVADA.")
    
    # 2. Demonstração de VALIDAÇÃO (Construímos o produto correto?)
    print("\n2. [VALIDAÇÃO]: Testando a geração com usuário real...")
    
    # Usuário tenta gerar o boleto digitando o CPF apenas com números
    print("  - Usuário tenta gerar boleto de R$ 100.00 usando CPF '12345678901' (sem formatação)...")
    resultado_falha = gerador.processar_fluxo_geracao(100.00, "12345678901")
    print(f"    Resultado: Sucesso = {resultado_falha['sucesso']}")
    print(f"    Erro retornado: {resultado_falha['erro']}")
    print("  -> O cálculo técnico funciona, mas o usuário não consegue gerar o boleto devido à interface rígida.")
    print("  -> Validação: REPROVADA (O produto não atende bem às necessidades de uso real).")
    
    # Fluxo corrigido (se o CPF for digitado exatamente como o sistema exige)
    print("\n  - Usuário tenta novamente formatando o CPF como '123.456.789-01'...")
    resultado_sucesso = gerador.processar_fluxo_geracao(100.00, "123.456.789-01")
    print(f"    Resultado: Sucesso = {resultado_sucesso['sucesso']}")
    print(f"    Boleto Gerado: R$ {resultado_sucesso['boleto']['valor_total']:.2f}")
    print("  -> Validação: APROVADA (Apenas com a formatação exigida pelo sistema).")

