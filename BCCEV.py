import pickle

##Veicular

class Veiculo:
    def __init__(self, modelo, marca, ano, capacidade, tipo):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.capacidade = capacidade
        self.tipo = tipo

veiculos = []

def cadastrar_veiculo():
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    ano = int(input("Ano: "))
    capacidade = float(input("Capacidade em kWh da Bateria: "))
    tipo = input("Tipo: ")
    veiculo = Veiculo(modelo, marca, ano, capacidade, tipo)

    # Verifica se o veículo já existe na lista
    existe = False
    for v in veiculos:
        if v.modelo == modelo and v.marca == marca and v.capacidade == capacidade:
            existe = True
            break
    if existe:
        print("Veículo já cadastrado.")
    else:
        veiculos.append(veiculo)
        print("Veículo cadastrado com sucesso!")

def listar_veiculos():
    if not veiculos:
        print("Não há veiculos cadastrados!")
        return
    for i, veiculo in enumerate(veiculos):
        print(f"{i+1}. Modelo: {veiculo.modelo} | Marca: {veiculo.marca} | Ano: {veiculo.ano} | Capacidade kWh: {veiculo.capacidade} | Tipo: {veiculo.tipo}")

def pesquisar_veiculo():
    if not veiculos:
        print("Não há veiculos cadastrados!")
        return
    else:
        modelo = input("Modelo do veículo: ")
        for i, veiculo in enumerate(veiculos):
            if veiculo.modelo.lower() == modelo.lower():
                print(f"Veículo encontrado: {i+1}. Modelo: {veiculo.modelo} | Marca: {veiculo.marca} | Ano: {veiculo.ano} | Capacidade kWh: {veiculo.capacidade} | Tipo: {veiculo.tipo}")
                return i
        print("Veículo não encontrado.")
        return -1

def editar_veiculo():
    if not veiculos:
        print("Não há veiculos cadastrados!")
        return
    indice = pesquisar_veiculo()
    if indice != -1:
        veiculo = veiculos[indice]
        modelo = input("Novo modelo (deixe em branco para manter o mesmo): ")
        if modelo:
            veiculo.modelo = modelo
        marca = input("Nova marca (deixe em branco para manter o mesmo): ")
        if marca:
            veiculo.marca =marca
        ano = input("Novo ano (deixe em branco para manter o mesmo): ")
        if ano:
             veiculo.ano = int(ano)
        capacidade = input("Nova capacidade (deixe em branco para manter o mesmo): ")
        if capacidade:
            veiculo.capacidade = int(capacidade)
        tipo = input("Novo tipo (deixe em branco para manter o mesmo): ")
        if tipo:
            veiculo.tipo = tipo
        print("Veículo editado com sucesso!")


def salvar_veiculos():
    with open("veiculos.bin", "wb") as arquivo:
        pickle.dump(veiculos, arquivo)


def carregar_veiculos():
    global veiculos
    try:
        with open("veiculos.bin", "rb") as arquivo:
            veiculos = pickle.load(arquivo)
    except FileNotFoundError:
        veiculos = []



def excluir_veiculo():
    if not veiculos:
        print("Não há veiculos cadastrados!")
        return
    indice = pesquisar_veiculo()
    if indice != -1:
        veiculos.pop(indice)
        print("Veículo excluído com sucesso!")


##
##
##
##
##
##
##
##
##
##Carregador
class Carregador:
    def __init__(self, modelo, marca, potência, ligação):
        self.modelo = modelo
        self.marca = marca
        self.potência = potência
        self.ligação = ligação


carregadores = []

def cadastrar_carregador():
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    potência = int(input("Potência kW: "))
    ligação = input("Esquema de ligação: ")
    carregador = Carregador(modelo, marca, potência, ligação)

    #Verifica se o carregador já existe na lista
    existe = False
    for v in carregadores:
        if v.modelo == modelo and v.marca == marca and v.potência == potência:
            existe = True
            break
    if existe:
        print("Carregador já cadastrado.")
    else:
        carregadores.append(carregador)
        print("Carregador cadastrado com sucesso.")

def listar_carregadores():
    if not carregadores:
        print("Não há carregadores cadastrados!")
        return
    for i, carregador in enumerate(carregadores):
        print(f"{i+1}. Modelo: {carregador.modelo} | Marca: {carregador.marca} | Potência kW: {carregador.potência} | Esquema de Ligação: {carregador.ligação}")

def pesquisar_carregador():
    if not carregadores:
        print("Não há carregadores cadastrados!")
        return
    else:
        modelo = input("Modelo do carregador: ")
        for i, carregador in  enumerate(carregadores):
            if carregador.modelo.lower() == modelo.lower():
                print(f"Carregador encontrado: {i+1}. Modelo: {carregador.modelo} | Marca: {carregador.marca} | Potência kW: {carregador.potência} | Esquema de Ligação: {carregador.ligação}")
                return i
        print("Carregador não encontrado.")
        return -1

def editar_carregador():
    if not carregadores:
        print("Não há carregadores cadastrados!")
        return
    indice = pesquisar_carregador()
    if indice != -1:
        carregador = carregadores[indice]
        modelo = input("Novo modelo (deixe em branco para manter o mesmo): ")
        if modelo:
            carregador.modelo = modelo
        marca = input("Nova marca (deixe em branco para manter o mesmo): ")
        if marca:
            carregador.marca =marca
        potência = input("Novo ano (deixe em branco para manter o mesmo): ")
        if potência:
            carregador.potência = int(potência)
        ligação = input("Nova capacidade (deixe em branco para manter o mesmo): ")
        if ligação:
            carregador.ligação = (ligação)
        print("Veículo editado com sucesso!")

def salvar_carregadores():
    with open("carregadores.bin", "wb") as arquivo:
        pickle.dump(carregadores, arquivo)

def carregar_carregadores():
    global carregadores
    try:
        with open("carregadores.bin", "rb") as arquivo:
            carregadores = pickle.load(arquivo)
    except FileNotFoundError:
        carregadores = []



def excluir_carregador():
    if not carregadores:
        print("Não há carregadores cadastrados!")
        return
    indice = pesquisar_carregador()
    if indice != -1:
        carregadores.pop(indice)
        print("Carregador excluído com sucesso!")

##
##
##
##
##
##
##
##
##
##Calculo


def escolher_veiculo():
    listar_veiculos()
    escolha = int(input("Escolha um veículo pelo número: "))
    if escolha < 1 or escolha > len(veiculos):
        print("Veículo inválido.")
        return None
    return veiculos[escolha-1]

def escolher_carregador():
    listar_carregadores()
    escolha = int(input("Escolha um carregador pelo número: "))
    if escolha < 1 or escolha > len(carregadores):
        print("Carregador inválido.")
        return None
    return carregadores[escolha-1]


rendimento = (0.70)

def capacidade_dividido_por_potência():
    veiculo = escolher_veiculo()
    if veiculo is None:
        return
    carregador = escolher_carregador()
    if carregador is None:
        return
    tempo_carregamento = veiculo.capacidade / carregador.potência / rendimento
    horas, minutos = divmod(tempo_carregamento * 60, 60)
    print(f"Tempo de carregamento Aproximado: {int(horas)} horas e {int(minutos)} minutos.")




##
##
##
##
##
##
##
##
##Menu

ajuda = "teste"

while True:
    print("""

    #############################################################
    #\t\tBCCEV - Battery Charger Calculator\t\t#
    #\t\tFor Electric Vehicles - BCCEV\t\t\t#
    #\t\tDeveloped by github.com/tomegatherion\t\t#
    #___________________________________________________________#
    #\t\tEscolha uma Opção Abaixo.\t\t\t#
    #\t\t01.\tCarregar Database.\t\t\t#
    #\t\t02.\tReazilar Calculo.\t\t\t#
    #\t\t03.\tCadastrar Veículos.\t\t\t#
    #\t\t04.\tListar Veículos.\t\t\t#
    #\t\t05.\tPesquisar Veículos.\t\t\t#
    #\t\t06.\tEditar Veículos.\t\t\t#
    #\t\t07.\tExcluir Veículos.\t\t\t#
    #\t\t08.\tadastrar Carregador.\t\t\t#
    #\t\t09.\tListar Carregador.\t\t\t#
    #\t\t10.\tPesquisar Carregador.\t\t\t#
    #\t\t11.\tEditar Carregador.\t\t\t#
    #\t\t12.\tExcluir Carregador.\t\t\t#
    #\t\t00.\tAjuda.\t\t\t\t\t#
    #\t\t 0.\tSair\t\t\t\t\t#
    #############################################################
    """)

    opcao = int(input("Opção: "))
    if opcao == 1:
        carregar_carregadores()
        carregar_veiculos()
    elif opcao == 2:
        capacidade_dividido_por_potência()
    elif opcao == 3:
        cadastrar_veiculo()
        salvar_veiculos()
    elif opcao == 4:
        listar_veiculos()
    elif opcao == 5:
        pesquisar_veiculo()
    elif opcao == 6:
        editar_veiculo()
    elif opcao == 7:
        excluir_veiculo()
        salvar_veiculos()
    elif opcao == 8:
        cadastrar_carregador()
        salvar_carregadores()
    elif opcao == 9:
        listar_carregadores()
    elif opcao == 10:
        pesquisar_carregador()
    elif opcao == 11:
        editar_carregador()
        salvar_carregadores()
    elif opcao == 12:
        excluir_carregador()
        salvar_carregadores()
    elif opcao == 00:
        with open("help.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
            while True:
                tecla = input("Pressione 'q' Para Sair...")
                if tecla == 'q':
                    break

    elif opcao == 0:
        break
    else:
        print("Digite uma Opção Valida!!!")

