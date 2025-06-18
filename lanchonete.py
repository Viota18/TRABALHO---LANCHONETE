#>>>>>>>>>>>> | VARIAVEIS GLOBAIS - LISTAS |<<<<<<<<<<<<<<<
Categoria = ['codigo','nome','preço']

Iniciar = 1
temp =[]
lista_prod=[]
lista_pedido=[]
tempo_codigo =[]
codigo_ind=[]

#>>>>>>>>>>>>>>| FUNÇOES DO CODIGO |<<<<<<<<<<<<<<<


#---| CODIGO DO CLIENTE |---  

def Menu_de_Entrada():
    print(">>>>>>>| MENU DE ENTRADA |<<<<<<<")
    print("")
    print(" --> SELECIONE UMA DAS OPÇÃO DE ENTRADA")
    print("")
    print(" (1) - ENTRAR COMO ADMINISTRADOR")
    print(" (2) - ENTRAR COMO CLIENTE")
    print(" (3) - CADASTRAR NOVO ADMINISTRADOR ")
    print(" (4) - SAIR DO PROGRAMA")
    print("")
    opção_de_entrda = ("1","2","3","4") #OPÇÃO PARA O USUARIO DIGITAR 
    entrada_usuario =input("--> ")#AGUARDANDO O USUARIO DIGITAR 
    while entrada_usuario not in opção_de_entrda:#CODIGO PARA VERIFICAR O QUE O USUARIO DIGITOU ESTA DENTRO DAS ESPECIFICAÇÕES PERMITIDAS.
        print(">>> OPÇÃO INVALIDA! <<<")
        print(">>> DIGITE UMA OPÇÃO VALIDA! <<<")
        entrada_usuario =input("--> ")
        print("")
    return entrada_usuario

def Confirmação_de_Cadastro():
    print("--> VOCE POSSUI CADASTRO?")
    print("")
    print("SE POSSUI DIGITE (SIM) /---/ SE NÃO POSSUI DIGITE (NÃO)")
    print("")
    decisão_cliente =input("--> ").strip().lower()
    while decisão_cliente not in ("sim","não"):
        print(">>> OPÇÃO INVALIDA! <<<")
        print(">>> DIGITE UMA OPÇÃO VALIDA! <<<")
        decisão_cliente =input("--> ").strip().lower()
        print("")
    return decisão_cliente

def Buscar_cadastro():
    print("--| VAMOS PROCURAR SEU CADASTRO EM NOSSO SERVIDOR |--")
    print("DIGITE UM DE SEUS DADOS PARA PROCURARMOS --> NOME, EMAIL OU TELEFONE")
    dados_cliente =input("--> ").strip().lower()
    Arquivo = open('Banco_de_dados_lanchonete.txt','r',encoding='utf-8')#ESSE CODIGO VAI ABRIR O ARQUIVO(Servidor_da_lanchonete.txt) E LER O ARQUIVO. (encoding='utf-8')-> codificação padrão moderna que suporta acentos e caracteres especiais como ç, ã, é, etc.
    encontrado = False
    senha_encontrada = -0
    for linha in Arquivo:#LE O ARQUIVO LINHA POR LINHA
        if dados_cliente in linha.lower():#COMPARA O QUE O USUARIO DIGITOU COM A LINHA DENTRO DO ARQUIVO EM MINUSCULA
            print("--->>> CADASTRO ENCONTRADO <<<---")
            print(linha.strip())# ESTE CODIGO SERVE PARA IMPRIMIR A LINHA ESCONTRADA REMOVENDO ESPAÇO EM BRANCO
        
           #EXTRAIR SENHA DA LINHA 
            # Extrair a senha da linha
            partes = linha.strip().split('|')
            for parte in partes:
                    if "SENHA:" in parte:
                        senha_encontrada = parte.split("SENHA:")[1].strip()
                        break
            encontrado = True
            break
        
    Arquivo.close()#FECHAR ARQUIVO
    if not encontrado: #Essa linha só será executada se nenhuma linha do arquivo tiver correspondido
        print("--->>> / NÃO ENCONTRADO CADASTRO \ <<<---")
        print("")
    else:
        return senha_encontrada  # <- RETORNA A SENHA
           
def Confirmação_de_senha(senha_correta):
    tentativa = 1#NUMEROS DE TENTAIVAS 
    senha_digitada_usuario =input("--> DIGITE SUA SENHA CADASTRADA: ")
    while senha_digitada_usuario != senha_correta:# SE A SENHA QUE O USUARIO DIGITAR FOR INCORRETA DA SENHA CORRETA
        print("---||| SENHA INCORRETA |||---")
        print("")
        tentativa+=1 # ESTA CONTANDO CADA VEZ QUE O USUARIO DIGITAR A SENHA 
        if tentativa > 3:# O NUMERO MAXIMO DE TENTATIVAS PARA O USUARIO DIGITAR A SUA SENHA 
            print("NUMEROS DE TENTATIVAS EXCEDIDO")
            print("")
            print("ACESSO BLOQUEADO!")
            print("")
            return False
        senha_digitada_usuario =input("--> TENTE NOVAMENTE: ") 
    print("---> SENHA CORRETA! ")
    return True

def Cadastro_de_usuario():
    print("--> DIGITE OS SEGUINTES DADOS PARA CADASTRO: NOME, EMAIL,TELEFONE E UMA SENHA !!")
    print("")
    # VERIFICAÇÃO DE NOME
    Nome =input("--> DIGITE SEU NOME:  ").strip().lower()#split() -> REMOVE ESPAÇO E QUEBRA LINHAS EXTRAS. lower() -> IRA CONVERTER PARA MINUSCULAN
    print("")
    while not Nome.replace(" ","").isalpha() or len (Nome) < 3 :#strip() remove espaços extras nas pontas ---> replace(" ", "") remove espaços internos para permitir nomes como "Maria da Silva" ---> .isalpha() garante que só tem letras ---> len(Nome) < 3 evita nomes curtos demais como "Jo".
        print("--> NOME INVÁLIDO! USE APENAS LETRAS E MÍNIMO 3 CARACTERES.")
        print("")
        Nome =input("--> DIGITE UM NOME VALIDO !:  ").strip().lower()
        print("")
    #VERIFICAÇÃO DE EMAIL
    Email =input("--> DIGITE SEU EMAIL: ")
    print("")
    while "@" not in Email or "." not in Email:#ESSA LINHA VERIFICA SE O EMAIL É VALIDO, SE NAO ESTIVER USANDO O (@) OU O (.) ELE SERA INVALIDO
        print("--> DIGITE UM EMAIL VALIDO !")
        print("")
        Email =input("--> DIGITE UM EMAIL VALIDO !: ")
        print("")
    #VERIFICAÇÃO DE TELEFONE
    Telefone =input("--> DIGITE SEU TELEFONE: ")
    print("")
    while not Telefone.isdigit():#VERIFICAR SE A STRING CONTEM APENAS NUMEROS DE (0 A 9). SE USUARIO DIGITAR QUAL QUER LETRA, SIMBULO OU ESPAÇO, SERA RECUSADO.
        print("DIGITE APENAS NUMEROS ! (SEM TRAÇO - PARENTES - ESPAÇO)") 
        print("")   
        Telefone =input("--> DIGITE UM TELEFONE VALIDO!!!: ")
        print("")
    #VERIFICAÇÃO DE SENHA
    print("--| CADASTRE UMA SENHA PARA SUA CONTA ! |--")
    print("")
    Senha =input("--> DIGITE SUA SENHA: ")
    Confirmar_senha =input("--> DIGITE SUA SENHA NOVAMENTE PARA CONFIRMAÇÃO: ")
    while Senha != Confirmar_senha:
        print("--->> SENHA INCORRETA!! <<--")
        print("")
        Senha =input("--> DIGITE SUA SENHA: ")
        print("")
        Confirmar_senha =input("--> DIGITE SUA SENHA NOVAMENTE PARA CONFIRMAÇÃO: ")
        print("")
    print('--->>>/ TODOS SEUS DADOS FORAM CADASTRADOS COM SUCESSO !!! \<<<----')
    print("")
    #SALVANDO OS CADASTROS DOS CLIENTES NO (Servidor_da_lanchonete.txt)
    Arquivo = open('Banco_de_dados_lanchonete.txt','a',encoding='utf-8')#CODIGO IRA ABRIR O ARQUIVO E ADICIONAR SEUS DADOS DENTRO DELE.(encoding='utf-8') -> codificação padrão moderna que suporta acentos e caracteres especiais como ç, ã, é, etc.
    Arquivo.write(f'\n|NOME: {Nome}|\n')
    Arquivo.write(f'|EMAIL: {Email}|\n')
    Arquivo.write(f'|TELEFONE: {Telefone}|\n')
    Arquivo.write(f'|SENHA: {Senha}|\n')
    Arquivo.write(f'---------------------------------------------------')
    Arquivo.close()

def cardapio():
    print("\n------ CARDÁPIO DA LANCHONETE ------\n")

    arquivo = open("produtos3.txt", "r", encoding="utf-8")
    dados = arquivo.readlines()
    arquivo.close()

    if dados == []:
        print("Nenhum produto cadastrado no momento.\n")
        return

    print("CÓDIGO | DESCRIÇÃO | VALOR")
    for linha in dados:
        partes = linha.strip().split(";")
        if len(partes) == 3:
            codigo, nome, preco = partes
            print(f"{codigo} | {nome} | R$ {float(preco):.2f}")
    print("\n-------------------------------------\n")
    return 
   
def Pedido():
    Arquivo1 = open("Pedidos_do_Cliente.txt", 'a', encoding="utf-8")

    arquivo = open("produtos3.txt", "r", encoding="utf-8")
    dados_lista = arquivo.readlines()
    arquivo.close()

    if dados_lista == []:
        print("----> NÃO TEM NENHUM PRODUTO DISPONÍVEL NESTE MOMENTO\n")
        return

    produtos = {}  # dicionário {codigo: (nome, preco)}
    for linha in dados_lista:
        partes = linha.strip().split(";")
        if len(partes) == 3:
            codigo = partes[0].strip()
            nome = partes[1].strip()
            preco = float(partes[2].strip())
            produtos[codigo] = (nome, preco)

    # Exibe o cardápio
    print("---->>> LISTA DE PRODUTOS DISPONÍVEIS <<<----")
    print("CÓDIGO | DESCRIÇÃO | VALOR UNITÁRIO")
    for cod in produtos:
        nome, preco = produtos[cod]
        print(f"{cod} | {nome} | R$ {preco:.2f}")

    print("\n >>>> VAMOS REALIZAR SEU PEDIDO ! <<<<")
    print(" -> DIGITE APENAS OS CÓDIGOS DO CARDÁPIO (ou 'encerrar' para finalizar)")

    Ped = []
    total = 0

    while True:
        entrada = input("--> ").strip().lower()

        if entrada == "encerrar":
            if Ped:
                print("\n---- RESUMO DO SEU PEDIDO ----")
                for nome, preco in Ped:
                    print(f"{nome} --- R$ {preco:.2f}")
                    Arquivo1.write(f"{nome} - R${preco:.2f}\n")
                print(f"TOTAL: R${total:.2f}")
                Arquivo1.write(f"TOTAL: R${total:.2f}\n\n")
                Arquivo1.write(f"-----------------------------------------\n")
            else:
                print("Nenhum item foi adicionado ao pedido.")
            print(" --> SEU PEDIDO FOI ENCERRADO!")
            break

        if entrada in produtos:
            nome_produto, preco_produto = produtos[entrada]
            Ped.append((nome_produto, preco_produto))
            total += preco_produto
            print(f"ADICIONADO: {nome_produto} --- R$ {preco_produto:.2f}")
        else:
            print("CÓDIGO INVÁLIDO! DIGITE UM CÓDIGO EXISTENTE DO CARDÁPIO.")

    Arquivo1.close()


#-------| CODIGO DO ADM |--------      

def Cadastro_do_ADM():
    print("")
    print(">>>>> VAMOS REALIZAR SEU CADASTRO! <<<<<")
    print("")
    print("-->TER NO MINIMO 4 CARACTER")

    #VERIFICAÇÃO DE NOME
    dados_Nome = input("DIGITE SEU NOME -->: ").strip().lower()#split() -> REMOVE ESPAÇO E QUEBRA LINHAS EXTRAS. lower() -> IRA CONVERTER PARA MIN
    while not dados_Nome.replace(" ","").isalpha() or len (dados_Nome) < 4 :#strip() remove espaços extras nas pontas ---> replace(" ", "") remove espaços internos para permitir nomes como "Maria da Silva" ---> .isalpha() garante que só tem letras ---> len(Nome) < 3 evita nomes curtos demais como "Jo".
        print("--> NOME INVÁLIDO! USE APENAS LETRAS E MÍNIMO 4 CARACTERES.")
        print("")
        dados_Nome =input("--> DIGITE UM NOME VALIDO !:  ").strip().lower()
        print("") 

    #VARIFICAÇÃO DE CPF
    dados_CPF = input("DIGITE SEU CPF -->:  ")
    while not dados_CPF.isdigit() or len(dados_CPF) !=11:#VERIFICAR SE A STRING CONTEM APENAS NUMEROS DE (0 A 9). SE USUARIO DIGITAR QUAL QUER LETRA, SIMBULO OU ESPAÇO, SERA RECUSADO. E TAMBEM Garante que o CPF tenha exatamente 11 dígitos.
        print("DIGITE APENAS NUMEROS ! (SEM TRAÇO - PARENTES - ESPAÇO)") 
        print("")   
        dados_CPF =input("--> DIGITE UM CPF VALIDO!!!: ")
        print("")

    #VERIFICAÇÃO DE EMAIL
    dados_Email =input("DIGITE SEU EMAIL: ")
    while "@" not in dados_Email or "." not in dados_Email:#ESSA LINHA VERIFICA SE O EMAIL É VALIDO, SE NAO ESTIVER USANDO O (@) OU O (.) ELE SERA INVALIDO
        print("--> DIGITE UM EMAIL VALIDO !")
        print("")
        dados_Email =input("--> DIGITE UM EMAIL VALIDO !: ")
        print("")

    #VERIFICAÇÃO DE TELEFONE
    dados_Telefone =input("DIGITE SEU TELEFONE: ")
    while not dados_Telefone.isdigit() or len(dados_Telefone) != 11:#VERIFICAR SE A STRING CONTEM APENAS NUMEROS DE (0 A 9). SE USUARIO DIGITAR QUAL QUER LETRA, SIMBULO OU ESPAÇO, SERA RECUSADO.
        print("DIGITE APENAS NUMEROS ! (SEM TRAÇO - PARENTES - ESPAÇO)") 
        print("")   
        dados_Telefone =input("--> DIGITE UM TELEFONE VALIDO!!!: ")
        print("")

    #CADASTRO DE SENHA DO ADM
    print("--| CADASTRE UMA SENHA PARA SUA CONTA ! |--")
    print("")
    dados_Senha =input("--> DIGITE SUA SENHA: ")
    Confirmar_senha =input("--> DIGITE SUA SENHA NOVAMENTE PARA CONFIRMAÇÃO: ")
    while dados_Senha != Confirmar_senha:
        print("--->> SENHA INCORRETA!! <<--")
        print("")
        dados_Senha =input("--> DIGITE SUA SENHA: ")
        print("")
        Confirmar_senha =input("--> DIGITE SUA SENHA NOVAMENTE PARA CONFIRMAÇÃO: ")
        print("")
    print('--->>>/ TODOS SEUS DADOS FORAM CADASTRADOS COM SUCESSO !!! \<<<----')
    print("")

    #SALVANDO OS CADASTROS DOS ADM NO (Dados_do_Adminis.txt)
    Arquivo3 = open('Dados_do_Adm.txt','a',encoding='utf-8')#CODIGO IRA ABRIR O ARQUIVO E ADICIONAR SEUS DADOS DENTRO DELE.(encoding='utf-8') -> codificação padrão moderna que suporta acentos e caracteres especiais como ç, ã, é, etc.
    Arquivo3.write(f'\n|NOME: {dados_Nome}|\n')
    Arquivo3.write(f'|CPF: {dados_CPF}|\n')
    Arquivo3.write(f'|EMAIL: {dados_Email}|\n')
    Arquivo3.write(f'|TELEFONE: {dados_Telefone}|\n')
    Arquivo3.write(f'|SENHA: {dados_Senha}|\n')
    Arquivo3.write(f'------------------------------------------------------')
    Arquivo3.close()
    return dados_Senha

def Autenticacao_do_ADM():
    print("\n>>>>---| AUTENTICAÇÃO DO ADMINISTRADOR |---<<<<\n")

    nome_login = input("DIGITE SEU NOME -->: ").strip().lower()
    senha_login = input("DIGITE SUA SENHA -->: ")

    # Abrir o arquivo
    Arquivo3 = open('Dados_do_Adm.txt', 'r', encoding='utf-8')
    linhas = Arquivo3.readlines()
    Arquivo3.close()

    if len(linhas) == 0:
        print("ARQUIVO DE USUÁRIOS VAZIO.")
        return False

    # Procurar o nome e a senha correspondente
    usuario_encontrado = False
    senha_correta = ""
    for i in range(len(linhas)):
        linha = linhas[i].strip().lower()
        if linha.startswith("|nome:"):
            nome_arquivo = linha.replace("|nome:", "").replace("|", "").strip()
            if nome_arquivo == nome_login:
                usuario_encontrado = True
                # Procurar a senha do mesmo usuário (assumindo que está algumas linhas abaixo)
                for j in range(i, i+5):  # Procurar nas próximas 5 linhas
                    if j < len(linhas):
                        linha_senha = linhas[j].strip().lower()
                        if linha_senha.startswith("|senha:"):
                            senha_correta = linha_senha.replace("|senha:", "").replace("|", "").strip()
                            break
                break

    if not usuario_encontrado:
        print("USUÁRIO NÃO ENCONTRADO.\n")
        return False

    # Verificar senha com até 3 tentativas
    tentativas = 1
    while senha_login != senha_correta:
        print("SENHA INCORRETA!\n")
        tentativas += 1
        if tentativas > 3:
            print(">>> TENTATIVAS EXCEDIDAS. ACESSO BLOQUEADO!")
            return False
        senha_login = input("TENTE NOVAMENTE -->: ")

    print("\n>>> LOGIN BEM-SUCEDIDO! <<<\n")
    return True

def Menu_do_ADM():
    print(">>>>>>>| MENU DO ADMINISTRADOR |<<<<<<<\n")
    print(" --> SELECIONE UMA DAS OPÇÕES\n")
    print(" (1) - CADASTRAR PRODUTO ")
    print(" (2) - BUSCAR PRODUTO")
    print(" (3) - EXCLUIR ")
    print(" (4) - VOLTAR MENU PRINCIPAL\n")
    
    opcoes_validas = ('1', '2', '3', '4')
    escolha = input("DIGITE UMA DAS OPÇÕES -->: ")
    
    while escolha not in opcoes_validas:
        print('-->>> ERRO! POR FAVOR, DIGITE UMA DAS OPÇÕES APRESENTADAS! <<<--\n')
        escolha = input("DIGITE UMA DAS OPÇÕES APRESENTADAS ACIMA -->: ") 
    
    return escolha

def Listagem_de_produtos():
    print("---->>> LISTA DE PRODUTOS DISPONÍVEIS <<<----")

    # Abrir o arquivo no modo leitura
    arquivo = open("produtos3.txt", "r", encoding="utf-8")
    dados_lista = arquivo.readlines()
    arquivo.close()

    lista_prod.clear()

    if dados_lista == []:
        print("----> NÃO TEM NENHUM PRODUTO DISPONÍVEL NESTE MOMENTO\n")
    else:
        print("CÓDIGO | DESCRIÇÃO | VALOR UNITÁRIO")
        for linha in dados_lista:
            partes = linha.strip().split(";")
            if len(partes) == 3:
                lista_prod.append(partes)

        for produto in lista_prod:
            print(f"{produto[0]} | {produto[1]} | R$ {produto[2]}")

def busca_cod():
    #prod = [Cod; Desc; Valor_u]
    #prod = (cod + ';' + desc + ';' + valor + '\n') -> ['100',';','hot-dog',';','28','/n']
    #*prod = [100;hot-dog;28]
    #**prod[0] = 100
    #**prod[1] = hot-dog
    #**prod[2] = 28
    codigo = 0
    arquivo = open('produtos3.txt', 'r', encoding='utf-8')
    dados = arquivo.readlines()
    arquivo.close()
    if dados == []:
        codigo = 100
    else:
        for i in range(len(dados)):
            dados[i] = dados[i].strip('\n')# *
            dados[i] = dados[i].split(';')# **
            temp.append(dados[i][0])
 
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        numeros = set(temp)
        esperado = set(range(100, max(numeros) + 1))
        faltantes = sorted(esperado - set(numeros))
        if faltantes == []:
            codigo = str(max(numeros) + 1)
        else:
            for numero in faltantes:
                tempo_codigo.append(numero)
            codigo = str(tempo_codigo[0])
    return codigo

def Gravar_txt(lista_prod):
    #prod = [Cod; Desc; Valor_u]
    arquivo = open('produtos3.txt', 'w', encoding='utf-8')
    for i in range(len(lista_prod)):
        arquivo.write(lista_prod[i][0] + ";" + lista_prod[i][1] + ";" + lista_prod[i][2] + "\n")
    arquivo.close()
    return lista_prod

def Buscar_indice(Lista_prod):
    #prod = [Cod; Desc; Valor_u]
    for i in range(len(Lista_prod)):
        codigo_ind.append(Lista_prod[i][0])
    op = input('Escolha o código do produto que você deseja\n')
    # validando a escolha do usuário
    while op not in codigo_ind:  
        Listagem_de_produtos()
        op = input('Escolha um código válido\n')
    codigo = codigo_ind.index(op)
    return codigo

def cadastrar():
    #prod = [Cod; Desc; Valor_u]
    print("Rotina para cadastrar produtos\n")
    cont_cad = 1
    #Cadastro de codigos
    while cont_cad != 2:
        #Criação da instancia da variável arquivo para criar o produtos.txt
        arquivo = open('produtos3.txt', 'a+', encoding='utf-8')
        #Controle da geração do código dos produtos
        cod = busca_cod()
        print("Código do produto a ser cadastrado: %s" %(cod))
        #Cadastro da descrição do produto
        desc = input("Insira a descrição do produto a ser cadastrado\n")
        while desc == "":
            print("Insira uma descrição válida")
            desc = input('Digite o produto que deseja inserir para o código %s\n' %(cod))
        #Cadastro de valores
        valor = input('Digite o valor que deseja para o(a) %s\n' %(desc))
        while (valor == "" or valor.isalpha()):
            print("Insira um valor válido\n")  
            valor = input('Digite o valor que deseja para o(a) %s\n' %(desc))
        #Cadastro do produto
        conf_cad = input('Deseja confirmar o cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n\n')
        while (conf_cad != "1" and conf_cad != "2"):
            print("Insira uma opção válida\n")
            conf_cad = input('Deseja confirmar o cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n\n')
        if conf_cad == "1":
            arquivo = open('produtos3.txt', 'r', encoding='utf-8')
            dados = arquivo.readlines()
            arquivo.close()
            # Verifica se o arquivo está vazio
            arquivo = open('produtos3.txt', 'a+', encoding='utf-8')
            if dados == []:
                arquivo.write(str(cod) + ';' + desc + ';' + str(valor) + '\n')
                arquivo.close()
            else:
                for i in range(len(dados)):
                    dados[i] = dados[i].strip('\n').split(';') # Adiciona os produtos existentes à lista
                dados.append([cod, desc, valor])  # Adiciona o novo produto à lista
                lista_cad = sorted(dados, key=lambda x: int(x[0]))  # Ordena a lista por código
                arquivo = open('produtos3.txt', 'w', encoding='utf-8')
                for i in range(len(lista_cad)):
                    arquivo.write(str(lista_cad[i][0]) + ";" + str(lista_cad[i][1]) + ";" + str(lista_cad[i][2]) + "\n")
                arquivo.close()   
            print("Item cadastrado com sucesso!!\n\n")   
            cont_cad = 2          
        elif conf_cad == "2":
            print("Cadastro cancelado\n")
            cont_cad = 2
            
def excluir_produto():
    codigo_excluir = input("Digite o código do produto que deseja excluir: ").strip()

    arquivo = open('produtos3.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()

    if linhas == []:
        print("Arquivo vazio, não há produtos para excluir.")
        return

    produto_encontrado = False
    novo_conteudo = ""

    for linha in linhas:
        linha_limpa = linha.strip()
        if linha_limpa == "":
            novo_conteudo += linha
        else:
            partes = linha_limpa.split(";")
            if len(partes) >= 1:
                codigo_atual = partes[0].strip()
                if codigo_atual == codigo_excluir:
                    produto_encontrado = True
                    # Não adiciona essa linha (produto será excluído)
                else:
                    novo_conteudo += linha
            else:
                novo_conteudo += linha  # Linha mal formatada, mantém

    if not produto_encontrado:
        print(f"Produto com código {codigo_excluir} não encontrado.")
    else:
        arquivo = open('produtos3.txt', 'w', encoding='utf-8')
        arquivo.write(novo_conteudo)
        arquivo.close()
        print(f"Produto com código {codigo_excluir} excluído com sucesso.")


#>>>>>>>>>>>> / CODIGO PRINCIPAL \ <<<<<<<<<<<<<<

while Iniciar == 1:
    option = Menu_de_Entrada()
    if option == "1":
       autenticado = Autenticacao_do_ADM()
       if autenticado:
            while True:
                menuzete = Menu_do_ADM()
                if menuzete == '1':
                    print("OPÇÃO SELECIONADA FOI : ",menuzete)
                    cadastrar()
                elif menuzete == '2':
                    print("OPÇÃO SELECIONADA FOI : ",menuzete)
                    Buscar_indice(lista_prod)
                elif menuzete == '3':
                    print("OPÇÃO SELECIONADA FOI : ",menuzete)
                    excluir_produto()
                    menuzete = Menu_do_ADM()
                elif option == '4':
                    print("OPÇÃO SELECIONADA FOI : ",option)
    elif option == "2":
        print("OPÇÃO SELECIONADA FOI : ",option)
        op1 = Confirmação_de_Cadastro()
        if op1 == "sim":
            print("OPÇÃO SELECIONADA FOI : ",op1)
            senha_correta = Buscar_cadastro()
            if senha_correta:
                print(" VAMOS CONFIRMAR SUA SENHA ! ")
                senha_OK = Confirmação_de_senha(senha_correta) 
                if senha_OK:
                    print(" USUARIO CONFIRMADO !!!")
                    print(" VAMOS REALIZAR O SEU PEDIDO ! ")
                    Ped = Pedido()
        elif op1 == "não":
            cad_usua = Cadastro_de_usuario()
            cad_usua =True
            print("CADASTRO REALIZADO! AGORA VOCÊ PODE FAZER SEU PEDIDO!")
            Ped = Pedido()
    elif option == '3':
        Cad_adm = Cadastro_do_ADM()
        option = Menu_de_Entrada()
    else:
        print("****| FIM DO PROGRAMA |****")
        break  
