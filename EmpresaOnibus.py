class Onibus:
    def __init__(self):
        self.janela = [0]*24
        self.corredor = [0]*24

    def vender_passagem(self, tipo):
        if tipo == 'janela':
            disponiveis = [i+1 for i, ocupada in enumerate(self.janela) if not ocupada]
            if disponiveis:
                print('Poltronas disponíveis na janela:', disponiveis)
                poltrona = int(input('Escolha o número da poltrona que deseja reservar: ')) - 1
                if self.janela[poltrona] == 0:
                    self.janela[poltrona] = 1
                    print(f'Poltrona {poltrona+1} na janela reservada.')
                else:
                    print('Poltrona já está ocupada.')
            else:
                print('Desculpe, todas as poltronas na janela estão ocupadas.')
        elif tipo == 'corredor':
            disponiveis = [i+1 for i, ocupada in enumerate(self.corredor) if not ocupada]
            if disponiveis:
                print('Poltronas disponíveis no corredor:', disponiveis)
                poltrona = int(input('Escolha o número da poltrona que deseja reservar: ')) - 1
                if self.corredor[poltrona] == 0:
                    self.corredor[poltrona] = 1
                    print(f'Poltrona {poltrona+1} no corredor reservada.')
                else:
                    print('Poltrona já está ocupada.')
            else:
                print('Desculpe, todas as poltronas no corredor estão ocupadas.')
        else:
            print('Tipo de poltrona inválido. Escolha entre "janela" e "corredor".')

    def verificar_disponibilidade(self):
        if 0 in self.janela or 0 in self.corredor:
            print('Há poltronas disponíveis.')
        else:
            print('Desculpe, o ônibus está completamente cheio.')

    def poltronas_ocupadas(self):
        ocupadas_janela = [i+1 for i, ocupada in enumerate(self.janela) if ocupada]
        ocupadas_corredor = [i+1 for i, ocupada in enumerate(self.corredor) if ocupada]
        print('Poltronas ocupadas na janela:', ocupadas_janela)
        print('Poltronas ocupadas no corredor:', ocupadas_corredor)

# Exemplo de uso
onibus = Onibus()
while True:
    tipo = input('Você deseja poltrona no corredor ou na janela? ')
    onibus.vender_passagem(tipo)
    onibus.verificar_disponibilidade()
    onibus.poltronas_ocupadas()
    continuar = input('Deseja reservar outra poltrona? (s/n) ')
    if continuar.lower() != 's':
        break


