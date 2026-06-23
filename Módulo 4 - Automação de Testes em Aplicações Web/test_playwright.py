"""
Módulo 4: Automação de Testes em Aplicações Web
Implementação 2: Playwright + Pytest

Este arquivo demonstra a automação de testes E2E usando o Playwright moderno.
Mostramos a utilização de localizadores baseados em atributos dedicados para testes
(data-test), que são a melhor prática de resiliência, e o uso de asserções inteligentes 
(expect) que fazem o Auto-waiting nativo dos elementos na tela.
"""

import re
from playwright.sync_api import Page, expect

def test_login_playwright(page: Page):
    """
    [TESTE E2E]: Simula o mesmo fluxo de login no SauceDemo usando Playwright.
    Graças ao Auto-waiting embutido, dispensamos o controle manual de esperas na tela.
    """
    # Navegação
    page.goto("https://www.saucedemo.com/")
    
    # Interação robusta via data-test (Atributo Customizado de QA - Padrão Ouro)
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    
    # Validação (Assert) com auto-waiting do expect() no carregamento da nova URL
    expect(page).to_have_url(re.compile(".*/inventory.html"))
    
    # Localiza o título da página de inventário
    titulo_produtos = page.locator(".title")
    
    # Valida o texto com auto-waiting embutido no expect
    expect(titulo_produtos).to_have_text("Products")
