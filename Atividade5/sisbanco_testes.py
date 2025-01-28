from sisbanco_bugs import Conta, ContaAbstrata, ContaEspecial, ContaImposto, ContaPoupanca, Banco
import unittest


class TesteContaAbstrata(unittest.TestCase):
    def testa_saldo(self):
        conta = ContaAbstrata("123")
        self.assertEqual(conta.get_numero(), "123")
        self.assertEqual(conta.get_saldo(), 0.0)
    
    def testa_creditar(self):
        conta = ContaAbstrata("123")
        conta.creditar(5)
        self.assertEqual(conta.get_saldo(), 5)
        conta.creditar(20)
        self.assertEqual(conta.get_saldo(), 25)
    
class TesteConta(unittest.TestCase):
    def testa_debitar(self):
        conta = Conta("123")
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), -5)
        conta.creditar(10)
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), 5)
    
class TesteContaPoupanca(unittest.TestCase):
    def testa_renderjuros(self):
        conta = ContaPoupanca("123")
        conta.creditar(10)
        conta.render_juros(0.1)
        self.assertEqual(conta.get_saldo(), 11)
    
class TesteContaEspecial(unittest.TestCase):
    def teste_renderbonus(self):
        conta = ContaEspecial("123")
        conta.creditar(100)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 101)
    
    def teste_creditar(self):
        conta = ContaEspecial("123")
        conta.creditar(100)
        self.assertEqual(conta.get_saldo(), 100)
    
class TesteContaImposto(unittest.TestCase):
    def teste_taxa(self):
        conta = ContaImposto("123")
        self.assertEqual(conta.get_taxa(), 0.001)
        conta.set_taxa(0.1)
        self.assertEqual(conta.get_taxa(), 0.1)
    
    def teste_debitar(self):
        conta = ContaImposto("123")
        conta.creditar(10)
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), 4.995)

class TesteBanco(unittest.TestCase):
    def teste_procurar(self):
        banco = Banco()
        self.assertEqual(banco.procurar("123"), None)
    
    def teste_cadastrar(self):
        banco = Banco()
        conta = Conta("123")
        banco.cadastrar(conta)
        self.assertEqual(banco.procurar("123"), conta)
    
    def teste_creditar(self):
        banco = Banco()
        conta = Conta("123")
        banco.cadastrar(conta)
        banco.creditar("123", 10)
        self.assertEqual(banco.saldo("123"), 10)

    def teste_saldo(self):
        banco = Banco()
        conta = Conta("123")
        banco.cadastrar(conta)
        self.assertEqual(banco.saldo("123"), conta.get_saldo())
        banco.creditar("123", 10)
        self.assertEqual(banco.saldo("123"), 10)

    def teste_debitar(self):
        banco = Banco()
        conta = Conta("123")
        banco.cadastrar(conta)
        banco.debitar('123', 5)
        self.assertEqual(conta.get_saldo(), -5)
        banco.creditar('123', 10)
        banco.debitar("123", 5)
        self.assertEqual(conta.get_saldo(), 0.0)
    
    def teste_transferir(self):
        banco = Banco()
        contao = Conta("123")
        contad = Conta("234")
        banco.cadastrar(contao)
        banco.cadastrar(contad)
        contao.creditar(10)
        banco.transferir("123", "234", 5)
        self.assertEqual(contao.get_saldo(), 5)
        self.assertEqual(contad.get_saldo(), 5)
    
    def teste_taxas(self):
        banco = Banco()
        conta = ContaImposto("123")
        banco.cadastrar(conta)
        self.assertEqual(banco.get_taxa_imposto(), 0.001)
        self.assertEqual(banco.get_taxa_poupanca(), 0.001)
        banco.set_taxa_imposto(0.1)
        self.assertEqual(banco.get_taxa_imposto(), 0.1)
        banco.set_taxa_poupanca(1)
        self.assertEqual(banco.get_taxa_poupanca(), 1)
    
    def teste_render(self):
        banco = Banco()
        conta = ContaEspecial("123")
        banco.cadastrar(conta)
        banco.creditar("123", 100)
        banco.render_bonus("123")
        self.assertEqual(conta.get_saldo(), 101)

        contap = ContaPoupanca("234")
        banco.cadastrar(contap)
        banco.creditar("234", 100)
        banco.set_taxa_poupanca(0.1)
        banco.render_juros("123")
        self.assertEqual(banco.saldo("123"), 110)
    

def main():
    try:
        banco = TesteBanco()
        banco.teste_cadastrar()
        banco.teste_creditar()
        banco.teste_debitar()
        banco.teste_procurar()
        banco.teste_render()
        banco.teste_saldo()
        banco.teste_taxas()
        banco.teste_transferir()
    except:
        print("Falhou em Banco!")
    try:  
        conta = TesteConta()
        conta.testa_debitar()
    except:
        print("Falhou em Conta!")
    try:
        contaa = TesteContaAbstrata()
        contaa.testa_creditar()
        contaa.testa_saldo()
    except:
        print("Falhou em ContaAbstrata!")
    try:
        contae = TesteContaEspecial()
        contae.teste_creditar()
        contae.teste_renderbonus()
    except:
        print("Falhou em ContaEspecial!")
    try:
        contap = TesteContaPoupanca()
        contap.testa_renderjuros()
    except:
        print("Falhou em ContaPoupanca!")
    try:
        contai = TesteContaImposto()
        contai.teste_debitar()
        contai.teste_taxa()
    except:
        print("Falhou em ContaImposto")
main()