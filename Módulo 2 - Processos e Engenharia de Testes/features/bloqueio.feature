# language: pt

Funcionalidade: Autenticação no painel administrativo
  Como um administrador de sistemas,
  Eu quero que contas sejam bloqueadas após erros sucessivos de senha,
  Para evitar ataques de força bruta contra o sistema.

  Cenário: Bloqueio cautelar após múltiplas tentativas falhas
    Dado que o usuário "admin_x" possui uma conta ativa
    E está na tela de login da aplicação
    Quando ele insere uma senha incorreta 3 vezes consecutivas
    Então a conta deve ser temporariamente bloqueada por 15 minutos
    E um e-mail de alerta de intrusão deve ser enviado ao setor de segurança cibernética
