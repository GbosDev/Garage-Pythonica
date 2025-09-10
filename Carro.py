# CRIAÇÃO DAS CLASSES

class Carro:
    def __init__(self, modelo, ano, cor, cilindros_motor, potencia_motor, combustivel_motor,
                 tamanho_pistao, material_pistao, marca_roda, diametro_roda, pressao_roda, tipo_roda,
                 capacidade_tanque, nivel_combustivel):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.motor = self.Motor(cilindros_motor, potencia_motor, combustivel_motor, tamanho_pistao, material_pistao)
        self.roda = self.Roda(marca_roda, diametro_roda, pressao_roda, tipo_roda)
        self.tanque = self.Tanque(capacidade_tanque, nivel_combustivel)

    def mostrar_informacoes(self):
        print("\nINFORMAÇÕES DO CARRO")
        print("=====================")
        print(f"Modelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}")
        self.motor.mostrar_motor()
        self.motor.pistao.mostrar_pistao()
        self.roda.mostrar_roda()
        self.tanque.mostrar_tanque()

    class Motor:
        def __init__(self, cilindros, potencia, tipo_combustivel, tamanho_pistao, material_pistao):
            self.cilindros = cilindros
            self.potencia = potencia
            self.tipo_combustivel = tipo_combustivel
            self.pistao = self.Pistao(tamanho_pistao, material_pistao)

        def mostrar_motor(self):
            print("\nINFORMAÇÕES DO MOTOR")
            print("=====================")
            print(
                f"Cilindros: {self.cilindros}\nPotência: {self.potencia} cv\nTipo de combustível: {self.tipo_combustivel}")

        class Pistao:
            def __init__(self, tamanho, material):
                self.tamanho = tamanho
                self.material = material

            def mostrar_pistao(self):
                print("\nINFORMAÇÕES DO PISTÃO")
                print("=====================")
                print(f"Tamanho do pistão: {self.tamanho}\nMaterial do pistão: {self.material}")

    class Roda:
        def __init__(self, marca, diametro, pressao, tipo):
            self.marca = marca
            self.diametro = diametro
            self.pressao = pressao
            self.tipo = tipo

        def mostrar_roda(self):
            print("\nINFORMAÇÕES DAS RODAS")
            print("=====================")
            print(
                f"Marca: {self.marca}\nDiâmetro: {self.diametro} polegadas\nPressão: {self.pressao} bar\nTipo: {self.tipo}")

    class Tanque:
        def __init__(self, capacidade, nivel_combustivel):
            self.capacidade = capacidade
            self.nivel_combustivel = nivel_combustivel

        def mostrar_tanque(self):
            print("\nINFORMAÇÕES DO TANQUE")
            print("=====================")
            print(f"Capacidade: {self.capacidade} litros\nNível de combustível: {self.nivel_combustivel} litros")


# UTILIZAÇÃO

carro1 = Carro(
    "Lamborghini Aventador SVJ", 2024, "Verde escuro perolado",
    "12(V12)", 770, "Gasolina", 95, "Alumínio forjado",
    "Pirelli", 21, 2.2, "Esportiva Liga Leve", 90, 60
)

carro1.mostrar_informacoes()
