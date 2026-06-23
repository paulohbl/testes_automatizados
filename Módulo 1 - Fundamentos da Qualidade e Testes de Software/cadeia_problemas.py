"""
Módulo 1: Fundamentos da Qualidade e Testes de Software
Exemplo: Cadeia de Problemas (Erro, Defeito, Falha)

Este exemplo demonstra os três conceitos fundamentais definidos pelo ISTQB:
1. Erro (Mistake): Ação humana incorreta ao projetar ou codificar o software.
2. Defeito (Bug/Fault): A manifestação física do erro no código fonte (o bug em si).
3. Falha (Failure): O comportamento visível e incorreto do sistema durante a execução.
"""

class CalculadoraComDefeito:
    """
    Simula uma calculadora escrita por um programador cansado.
    Contém o defeito de não validar divisão por zero.
    """
    def dividir(self, a: float, b: float) -> float:
        # [ERRO]: O desenvolvedor esqueceu de validar a entrada.
        # [DEFEITO]: Código abaixo executa a divisão por zero diretamente.
        return a / b


class CalculadoraCorrigida:
    """
    Simula o código corrigido após o ciclo de testes expor a falha.
    O erro foi resolvido com tratamento adequado de exceção.
    """
    def dividir(self, a: float, b: float) -> float:
        # O comportamento esperado de divisão por zero é validado
        # e lança um erro com uma mensagem clara para o usuário final.
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b


# Exemplo de execução interativa
if __name__ == "__main__":
    print("--- Demonstração da Cadeia de Problemas ---")
    calc_defeito = CalculadoraComDefeito()
    
    print("\nExecutando Calculadora com Defeito:")
    try:
        # [FALHA]: O programa lança exceção técnica e trava se não tratada.
        calc_defeito.dividir(10, 0)
    except ZeroDivisionError as e:
        print(f"[FALHA] CalculadoraComDefeito quebrou com: {type(e).__name__} ({e})")
        
    print("\nExecutando Calculadora Corrigida:")
    calc_corrigida = CalculadoraCorrigida()
    try:
        calc_corrigida.dividir(10, 0)
    except ValueError as e:
        print(f"[CORRETO] CalculadoraCorrigida tratou o erro e retornou: {e}")
