class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

  

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

   
cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
cliente = Cliente('VICTOR')
cliente.inserir_endereco('RUA 13 M', 54)
cliente.inserir_endereco('Rua  VICTOR', 6745)

# cliente1
print(cliente1.nome)
print(cliente1.enderecos[0].rua,cliente1.enderecos[0].numero)
print(cliente1.enderecos[1].rua,cliente1.enderecos[1].numero)
cliente1.lista_enderecos()
print()

# CLIENTE2
print(cliente.nome)
print(cliente.enderecos[0].rua,cliente1.enderecos[0].numero)
print(cliente.enderecos[1].rua,cliente1.enderecos[1].numero)
cliente.lista_enderecos()
