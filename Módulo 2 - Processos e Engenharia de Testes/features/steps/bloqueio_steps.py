import sys
import os
from behave import given, when, then

# Adiciona o diretório do módulo ao path para garantir a importação de autenticacao.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from autenticacao import SistemaAutenticacao

@given('que o usuário "{usuario}" possui uma conta ativa')
def step_impl(context, usuario):
    context.usuario = usuario
    context.sistema = SistemaAutenticacao()
    # Verifica o estado inicial (Dado)
    assert context.sistema.contas[usuario]["ativa"] is True
    assert context.sistema.contas[usuario]["bloqueada"] is False

@given('está na tela de login da aplicação')
def step_impl(context):
    context.sistema.ir_para_tela_login()
    assert context.sistema.na_tela_de_login is True

@when('ele insere uma senha incorreta {tentativas:d} vezes consecutivas')
def step_impl(context, tentativas):
    for _ in range(tentativas):
        context.sistema.tentar_login(context.usuario, "senha_errada_qualquer")

@then('a conta deve ser temporariamente bloqueada por {tempo:d} minutos')
def step_impl(context, tempo):
    conta = context.sistema.contas[context.usuario]
    assert conta["bloqueada"] is True
    assert conta["tempo_bloqueio_minutos"] == tempo

@then('um e-mail de alerta de intrusão deve ser enviado ao setor de segurança cibernética')
def step_impl(context):
    conta = context.sistema.contas[context.usuario]
    assert conta["email_alerta_enviado"] is True
