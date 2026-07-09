"""
Módulo 5: Automação de Testes em Aplicações Móveis
Exemplo prático de automação móvel usando Appium e Pytest
"""

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.options.android import UiAutomator2Options

# Mapeamento do Emulador Android alvo (Desired Capabilities)
caps = {
    "platformName": "Android",
    "appium:deviceName": "Pixel_API_33",
    "appium:appPackage": "com.google.android.contacts",
    "appium:appActivity": "com.android.contacts.activities.PeopleActivity",
    "appium:automationName": "UiAutomator2",
    "appium:autoGrantPermissions": True
}

def test_adicionar_contato_appium():
    # Cria os options correspondentes ao driver UiAutomator2
    options = UiAutomator2Options().load_capabilities(caps)
    
    # Conecta ao servidor local do Appium
    driver = webdriver.Remote("http://localhost:4723", options=options)
    wait = WebDriverWait(driver, 10)

    try:
        # Clica no Floating Action Button (+) para novo contato
        btn_add = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.google.android.contacts:id/floating_action_button")))
        btn_add.click()

        # Trata o bottom sheet de "Choose where to save" caso apareça
        try:
            btn_sheet = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//*[@text='Device & Google' or @text='More options' or @text='Device only']")))
            btn_sheet.click()
        except Exception:
            # Se não aparecer (já salvo como preferência), segue adiante
            pass

        # Aguarda a tela de digitação e preenche o Nome
        campo_nome = wait.until(EC.visibility_of_element_located(
            (AppiumBy.XPATH, "//*[@text='First name']")))
        campo_nome.send_keys("Alan Turing")

        # Localiza o campo de Telefone (EditText contendo o label 'Phone') e insere o número fictício
        campo_telefone = wait.until(EC.visibility_of_element_located(
            (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[contains(@text, 'Phone')]]")))
        campo_telefone.send_keys("555-0100")

        # Localiza o botão de Salvar (Save) por texto e clica
        btn_salvar = wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, "//*[@text='Save']")))
        btn_salvar.click()
        
        # Opcional: Validar se o contato foi salvo com sucesso na tela
        contato_salvo = wait.until(EC.visibility_of_element_located(
            (AppiumBy.XPATH, "//*[@text='Alan Turing']")))
        assert contato_salvo is not None

    finally:
        # Garante o encerramento da sessão do driver mesmo se houver falha
        driver.quit()
