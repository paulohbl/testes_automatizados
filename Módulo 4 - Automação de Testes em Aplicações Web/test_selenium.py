"""
Módulo 4: Automação de Testes em Aplicações Web
Implementação 1: Selenium WebDriver + Pytest

Este arquivo demonstra a automação de testes E2E usando o Selenium WebDriver clássico.
Nele, mostramos o controle explícito de concorrência/sincronismo usando WebDriverWait e
a localização de elementos via localizadores tradicionais (By.ID e By.CLASS_NAME).
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_selenium():
    """
    [TESTE E2E]: Simula o fluxo de login de um usuário real no SauceDemo usando Selenium.
    Utiliza WebDriverWait para garantir a sincronização com o carregamento da página.
    """
    # Inicializa o navegador Chrome
    # O Selenium Manager baixa o driver do navegador apropriado automaticamente se necessário.
    driver = webdriver.Chrome()
    
    try:
        # Acessa a página web de demonstração
        driver.get("https://www.saucedemo.com/")
        
        # Preenche os campos usando By.ID (Localizador nativo)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # [ESPERA EXPLÍCITA]: Aguarda até 10s para que o elemento do título apareça na tela
        wait = WebDriverWait(driver, 10)
        titulo_produtos = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )
        
        # Asserções do Pytest
        assert titulo_produtos.text == "Products"
        assert "inventory.html" in driver.current_url
        
    finally:
        # Garante que o navegador seja fechado mesmo se o teste falhar
        driver.quit()
