# Exercício 1: Exercício de Classe, Atributo e Método (Nível Básico): Conta Bancária

# Você está criando um programa para representar contas bancárias. Cada conta bancária tem um
# número de conta, um titular da conta e um saldo. Você precisa criar uma classe ContaBancaria para representar essas contas e 
# fornecer métodos para realizar operações básicas, como depósito e saque.

# Instruções:

# Crie uma classe chamada ContaBancaria com os seguintes atributos:

#numero_conta: o número da conta (um número inteiro). titular_conta: o nome do
# titular da conta (uma string). saldo: o saldo da conta (um número decimal, inicialmente 
# definido como 0).

#Implemente os seguintes métodos na classe ContaBancaria:

# __init__(self, numero_conta, titular_conta): O construtor que inicializa os atributos 
# da conta. depositar(self, valor): Um método que permite ao titular da conta depositar
# dinheiro na conta. sacar(self, valor): Um método que permite ao titular da conta sacar 
# dinheiro da conta, desde que haja saldo suficiente.

class ContaBancaria:
    def __init__(self, numero_conta, titular_conta):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = 0.0 # saldo inicial definido com 0.0
    
    def depositar(self, valor):
        if valor > 0:
            text = f'Valor depositado de R${valor}, realizado com sucesso.'
            self.saldo =+ valor   # self.saldo = self.saldo + valor
            print(text)
        else:
            print('O valor do depósito deve ser maior que 0')
        
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso')
            else: 
                print("saldo insuficiente para realizar o saque")
        else:
            print("O valor do saque deve ser maior que zero.")
            

contaKerlla = ContaBancaria(202301, "Kerlla Regina")

contaKerlla.depositar(100)

contaKerlla.sacar(10)

print(f'Saldo:{contaKerlla.saldo}')




