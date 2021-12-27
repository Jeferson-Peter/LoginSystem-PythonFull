from Controller import Login_controller, Cadastrar_controller
while True:
    print("================[SYSTEM MENU]================")
    option = int(input("Digite 1 para Cadastrar\nDigite 2 para logar\nDigite 3 para sair\nOpção: "))
    if option == 1:
        nome = input("Digite o seu nome de usuário: ")
        email = input("Digite o seu email: ")
        senha = input("Digite a sua senha para cadastro: ")
        return_cadastrar = Cadastrar_controller.cadastrar(nome,email, senha)
        if return_cadastrar == 1: print("Cadastrado com sucesso!")
        elif return_cadastrar == 2: print("ERRO! Digite um email válido!")
        elif return_cadastrar == 3: print("ERRO! Sua senha deve conter no mínimo 10 caracteres. A senha deve possuir caracteres minusculos, maiusculos, especiais, e numeros")
        elif return_cadastrar == 4: print("ERRO! O nome deve possuir entre 3 à 50 caracteres!")
        elif return_cadastrar == 5: print("ERRO! Já existe um usuário com estas credenciais!")
    elif option == 2:
        email = input("Digite o seu email: ")
        senha = input("Digite a sua senha para cadastro: ")
        return_login = Login_controller.login(email, senha)
        if not return_login: print("Email ou senha inv[alidos")
        else: print(f' O usuário {return_login["user"]} foi autenticado com sucesso')
    elif option == 3:
        break
    print("================[SYSTEM MENU]================")