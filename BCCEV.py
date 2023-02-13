# Importa as bibliotecas necessárias para o código.
import pickle
import os

#____________________________________________________________________________________________________________________________#

# Esta função será utilizada dentro de loops, para impedir que o loop traga a nova tela, deixando a visualização mais clara.
def esperar_tecla():
    input("\n\n\n\nPressione qualquer tecla para continuar...")






#____________________________________________________________________________________________________________________________#
#_________________________________________________________Veicular___________________________________________________________#
#__________________________________Parte do código referente a parte veicular do programa____________________________________#
#____________________________________________________________________________________________________________________________#






# Define a classe veiculo, e seus atributos.
class Veiculo:
    def __init__(self, modelo, marca, ano, capacidade, tipo):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.capacidade = capacidade
        self.tipo = tipo

veículos = []


# Função para cadastrar veículos.
def cadastrar_veiculo():
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    ano = int(input("Ano: "))
    capacidade = float(input("Capacidade em kWh da Bateria: "))
    tipo = input("Tipo: ")
    veiculo = Veiculo(modelo, marca, ano, capacidade, tipo)


    # Verifica se o veículo já existe na lista
    existe = False
    for v in veículos:
        if v.modelo == modelo and v.marca == marca and v.capacidade == capacidade:
            existe = True
            break
    if existe:
        print("Veículo já cadastrado.")
    else:
        veículos.append(veiculo)
        print("Veículo cadastrado com sucesso!")


# Função para listar os veículos já cadastrados.
def listar_veículos():
    if not veículos:
        print("Não há veículos cadastrados!")
        return
    for i, veiculo in enumerate(veículos):
        print(f"{i+1}. Modelo: {veiculo.modelo} | Marca: {veiculo.marca} | Ano: {veiculo.ano} | Capacidade kWh: {veiculo.capacidade} | Tipo: {veiculo.tipo}")


# Função para pesquisar pelo veiculo.
def pesquisar_veiculo():
    if not veículos:
        print("Não há veículos cadastrados!")
        return
    else:
        modelo = input("Modelo do veículo: ")
        for i, veiculo in enumerate(veículos):
            if veiculo.modelo.lower() == modelo.lower():
                print(f"Veículo encontrado: {i+1}. Modelo: {veiculo.modelo} | Marca: {veiculo.marca} | Ano: {veiculo.ano} | Capacidade kWh: {veiculo.capacidade} | Tipo: {veiculo.tipo}")
                return i
        print("Veículo não encontrado.")
        return -1


# Função para editar o veiculo.
# Dentro da função editar também é utilizado a função escolher veiculo.
def editar_veiculo():
    if not veículos:
        print("Não há veículos cadastrados!")
        return
    veiculo = escolher_veiculo()
    if veiculo is None:
        return
    modelo = input("Novo modelo (deixe em branco para manter o mesmo): ")
    if modelo:
        veiculo.modelo = modelo
    marca = input("Nova marca (deixe em branco para manter o mesmo): ")
    if marca:
        veiculo.marca = marca
    ano = int(input("Novo ano (deixe em branco para manter o mesmo): "))
    if ano:
        veiculo.ano = int(ano)
    capacidade = float(input("Nova capacidade (deixe em branco para manter o mesmo): "))
    if capacidade:
        veiculo.capacidade = float(capacidade)
    tipo = input("Novo tipo (deixe em branco para manter o mesmo): ")
    if tipo:
        veiculo.tipo = tipo
    print("Veículo editado com sucesso!")


# Salva as alterações no banco de dados veículos.bin
def salvar_veículos():
    with open("veículos.bin", "wb") as arquivo:
        pickle.dump(veículos, arquivo)


# Carrega as informações do bando de dados veículos.bin para o programa.
def carregar_veículos():
    global veículos
    try:
        with open("veículos.bin", "rb") as arquivo:
            veículos = pickle.load(arquivo)
    except FileNotFoundError:
        veículos = []


# Função excluir veiculo
# Dentro da função excluir também é utilizado a função escolher veiculo.
def excluir_veiculo():
    if not veículos:
        print("Não há veículos cadastrados!")
        return
    veiculo = escolher_veiculo()
    if veiculo is None:
        return
    veículos.remove(veiculo)
    print("Veículo excluído com sucesso!")






#____________________________________________________________________________________________________________________________#
#_________________________________________________________Carregador_________________________________________________________#
#_____________________________Parte do código referente a parte sobre o equipamento no programa______________________________#
#____________________________________________________________________________________________________________________________#






# Define a classe do carregador e seus atributos.
class Carregador:
    def __init__(self, modelo, marca, potência, ligação):
        self.modelo = modelo
        self.marca = marca
        self.potência = potência
        self.ligação = ligação


carregadores = []


# Função para cadastrar carregador.
def cadastrar_carregador():
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    potência = float(input("Potência kW: "))
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

# Função para listar os carregadores já cadastrados.
def listar_carregadores():
    if not carregadores:
        print("Não há carregadores cadastrados!")
        return
    for i, carregador in enumerate(carregadores):
        print(f"{i+1}. Modelo: {carregador.modelo} | Marca: {carregador.marca} | Potência kW: {carregador.potência} | Esquema de Ligação: {carregador.ligação}")


# Função para pesquisar pelo carregador.
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


# Função para editar o carregador.
# Dentro da função editar também é utilizado a função escolher carregador.
def editar_carregador():
    if not carregadores:
        print("Não há carregadores cadastrados!")
        return
    carregador = escolher_carregador()
    if carregador is None:
        return
    modelo = input("Novo modelo (deixe em branco para manter o mesmo): ")
    if modelo:
        carregador.modelo = modelo
    marca = input("Nova marca (deixe em branco para manter o mesmo): ")
    if marca:
        carregador.marca =marca
    potência = float(input("Novo ano (deixe em branco para manter o mesmo): "))
    if potência:
        carregador.potência = float(potência)
    ligação = input("Nova capacidade (deixe em branco para manter o mesmo): ")
    if ligação:
        carregador.ligação = (ligação)
    print("Veículo editado com sucesso!")


# Salva as alterações no banco de dados carregadores.bin
def salvar_carregadores():
    with open("carregadores.bin", "wb") as arquivo:
        pickle.dump(carregadores, arquivo)


# Carrega as informações do banco de dados carregadores.bin para o programa.
def carregar_carregadores():
    global carregadores
    try:
        with open("carregadores.bin", "rb") as arquivo:
            carregadores = pickle.load(arquivo)
    except FileNotFoundError:
        carregadores = []


# Função excluir carregador
# Dentro da função excluir também é utilizado a função escolher carregador.
def excluir_carregador():
    if not carregadores:
        print("Não há carregadores cadastrados!")
        return
    carregador = escolher_carregador()
    if carregador is None:
        carregadores.remove(carregador)
        print("Carregador excluído com sucesso!")






#____________________________________________________________________________________________________________________________#
#______________________________________________________Funções gerais________________________________________________________#
#____________________________________________________________________________________________________________________________#






# Função para escolher um veículos a partir de uma lista na tela, pois o identificador
# principal das classes é o "modelo" do equipamento/carro, e 
# por vezes um mesmo modelo em anos diferentes tem especificações técnicas diferentes.
# Isto gera uma serie de problemas na hora de alterar ou excluir itens. Poderia ter sido resolvido de outra maneira
# porem eu percebi que selecionar um item para exclusão ou alteração a parte de uma tabela pode ser mais produtivo.
def escolher_veiculo():
    listar_veículos()
    try:
        escolha = int(input("Escolha um veículo pelo número: "))
        if escolha < 1 or escolha > len(veículos):
            raise ValueError("Veículo inválido.")
    except ValueError as e:
        print(e)
        return None
    return veículos[escolha-1]


# Função para escolher carregador a partir de uma lista na tela.
# Os comentários das linhas 277 a 280 também se aplicam a está função.
def escolher_carregador():
    listar_carregadores()
    try:
        escolha = int(input("Escolha um carregador pelo número: "))
        if escolha < 1 or escolha > len(carregadores):
            raise ValueError("Carregador inválido.")
    except ValueError as e:
            print(e)
            return None
    return carregadores[escolha-1]


# Em todo sistema a energia de saída é sempre menor que a energia de entrada, pois há sempre alguma perda no processo de transformação,
# em teoria o tempo de carregamento seria: (Tempo de carregamento = Capacidade da bateria / Potência entregue pelo carregador)
# Porem neste processo há diversas perdas, por efeito joule, por potencia reativa, por perdas na transformação da corrente de CA >> CC,
# dentre outros. Além disso há também o controle que o próprio carregador realiza na velocidade de carga, a corrente de carga não é constante na
# maioria dos casos, pois acarretaria a bateria há um grande stresse e desgaste prematuro, logo se corrente não é constante a velocidade da carga não é constante,
# pois em grande maioria das vezes os carregadores veiculares mantém a tensão fixa, ou com variações moderadas, ocasionando assim uma variação na corrente absorvida 
# pela bateria devido a DDP entre carregador e bateria.
# Logo, a o rendimento é na verdade um fator genérico que inclui a eficiência e o rendimento do carregador. Pelas minhas a analises em diversos datasets de carregadores
# cheguei a este valor aproximado, porem dependendo da marca este valor varia de 0.70 até 0.85.
# Mas de toda forma este será um ponto de melhoria futura no código, porem ainda está sendo levantada informações mais detalhadas junto aos fabricantes, pois
# em alguns destes casos foi chegado a este resultado por formulas e exemplos práticos fornecidos pelos fabricantes.#
rendimento = (0.70)


# Função que realiza o calculo da estimativa de tempo.
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






#____________________________________________________________________________________________________________________________#
#______________________________________________________Menu Geral____________________________________________________________#
#____________________________________________________________________________________________________________________________#







while True:
    print("""

    #############################################################
    #\t\tBCCEV - Battery Charger Calculator\t\t#
    #\t\tFor Electric Vehicles - BCCEV\t\t\t#
    #\t\tDeveloped by github.com/tomegatherion\t\t#
    #___________________________________________________________#
    #\t\tEscolha uma Opção Abaixo.\t\t\t#
    #\t\t 1.\tCarregar Database.\t\t\t#
    #\t\t 2.\tRealizar Calculo.\t\t\t#
    #\t\t 3.\tCadastrar Veículos.\t\t\t#
    #\t\t 4.\tListar Veículos.\t\t\t#
    #\t\t 5.\tPesquisar Veículos.\t\t\t#
    #\t\t 6.\tEditar Veículos.\t\t\t#
    #\t\t 7.\tExcluir Veículos.\t\t\t#
    #\t\t 8.\tCadastrar Carregador.\t\t\t#
    #\t\t 9.\tListar Carregador.\t\t\t#
    #\t\t10.\tPesquisar Carregador.\t\t\t#
    #\t\t11.\tEditar Carregador.\t\t\t#
    #\t\t12.\tExcluir Carregador.\t\t\t#
    #\t\t13.\tAjuda.\t\t\t\t\t#
    #\t\t 0.\tSair\t\t\t\t\t#
    #############################################################
    """)

    opção = int(input("Opção: "))
    if opção == 1:
        carregar_carregadores()
        carregar_veículos()
        print("Base de dados Carregada!")
        esperar_tecla()
    elif opção == 2:
        capacidade_dividido_por_potência()
        esperar_tecla()
    elif opção == 3:
        cadastrar_veiculo()
        salvar_veículos()
        esperar_tecla()
    elif opção == 4:
        listar_veículos()
        esperar_tecla()
    elif opção == 5:
        pesquisar_veiculo()
        esperar_tecla()
    elif opção == 6:
        editar_veiculo()
        esperar_tecla()
    elif opção == 7:
        excluir_veiculo()
        salvar_veículos()
        esperar_tecla()
    elif opção == 8:
        cadastrar_carregador()
        salvar_carregadores()
        esperar_tecla()
    elif opção == 9:
        listar_carregadores()
        esperar_tecla()
    elif opção == 10:
        pesquisar_carregador()
        esperar_tecla()
    elif opção == 11:
        editar_carregador()
        salvar_carregadores()
        esperar_tecla()
    elif opção == 12:
        excluir_carregador()
        salvar_carregadores()
        esperar_tecla()
    elif opção == 13:
        with open("help.txt", "r", encoding='utf-8') as arquivo:
            conteúdo = arquivo.read()
            print(conteúdo)
            while True:
                tecla = input("Pressione 'q' Para Sair...")
                if tecla == 'q':
                    break

    elif opção == 0:
        break
    else:
        print("Digite uma Opção Valida!!!")
    os.system("cls")



#____________________________________________________________________________________________________________________________#