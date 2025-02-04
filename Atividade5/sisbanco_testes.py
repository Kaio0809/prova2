from sisbanco import *
import unittest

class TesteContaAbstrata(unittest.TestCase):
    def teste_init(self):
        conta = ContaAbstrata("123")
        self.assertEqual(conta.get_numero(), "123")
        self.assertEqual(conta.get_saldo(), 0.0)
    
    def teste_creditar(self):
        conta = ContaAbstrata("123")
        conta.creditar(10)
        self.assertEqual(conta.get_saldo(), 10.0)
        conta.creditar(2)
        self.assertEqual(conta.get_saldo(), 12.0)

class TesteConta(unittest.TestCase):
    def teste_debitar(self):
        conta = Conta("123")
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), -5)
        conta.creditar(10)
        conta.debitar(5)
        self.assertEqual(conta.get_saldo, 0.0)
    
class TesteContaPoupanca(unittest.TestCase):
    def teste_render_juros(self):
        conta = ContaPoupanca("123")
        conta.render_juros(0.1)
        self.assertEqual(conta.get_saldo(), 0.0)
        conta.creditar(10)
        conta.render_juros(0.1)
        self.assertEqual(conta.get_saldo(), 11.0)

class TesteContaEspecial(unittest.TestCase):
    def teste_creditar(self):
        conta = ContaEspecial("123")
        conta.creditar(10)
        self.assertEqual(conta.get_saldo(), 10)
    
    def teste_render_bonus(self):
        conta = ContaEspecial("123")
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 0.0)
        conta.creditar(100)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 101)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 101)
        conta.creditar(1000)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 1111)
    
class TesteContaImposto(unittest.TestCase):
    def teste_taxa(self):
        conta = ContaImposto("123")
        self.assertEqual(conta.get_taxa(), 0.001)
        conta.set_taxa(0.1)
        self.assertEqual(conta.get_taxa(), 0.1)
    
    def teste_debitar(self):
        conta = ContaImposto("123")
        conta.debitar(0)
        self.assertEqual(conta.get_saldo(), 0.0)
        conta.debitar(10)
        self.assertEqual(conta.get_saldo(), -10.01)
        conta.creditar(20.01)
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), 4.995)

class TesteBanco(unittest.TestCase):
    def teste_procurar(self):
        conta = Conta("123")
        conta2 = Conta("234")
        sisbanco = Banco()
        sisbanco.cadastrar(conta)
        self.assertEqual(sisbanco.procurar("123"), conta)
        self.assertEqual(sisbanco.procurar("234"), None)
    
    def teste_cadastrar(self):
        conta = Conta("123")
        conta2 = Conta("234")
        sisbanco = Banco()
        sisbanco.cadastrar(conta)
        sisbanco.cadastrar(conta2)
        self.assertEqual(sisbanco.procurar("123"), conta)
        self.assertEqual(sisbanco.procurar("234"), conta2)
    
    def teste_creditar(self):
        conta = Conta("123")
        conta2 = Conta("234")
        sisbanco = Banco()
        sisbanco.cadastrar(conta)
        sisbanco.creditar("123",10)
        self.assertEqual(conta.get_saldo(), 10)
        sisbanco.creditar("234", 10)
        self.assertEqual(conta2.get_saldo(), 0.0)
    
    def teste_debitar(self):
        conta = Conta("123")
        conta2 = Conta("234")
        sisbanco = Banco()
        sisbanco.cadastrar(conta)
        sisbanco.debitar("123",10)
        self.assertEqual(conta.get_saldo(), 10)
        sisbanco.debitar("234", 10)
        self.assertEqual(conta2.get_saldo(), 0.0)
    
    def teste_saldo(self):
        conta = Conta("123")
        conta2 = Conta("234")
        sisbanco = Banco()
        sisbanco.cadastrar(conta)
        sisbanco.cadastrar(conta2)
        sisbanco.creditar("123",10)
        self.assertEqual(sisbanco.saldo("123"), 10)
        sisbanco.creditar("234", 10)
        self.assertEqual(conta2.get_saldo(), sisbanco.saldo("234"))
    
    def teste_trasnferir(self):
        conta = Conta("123")
        conta2 = Conta("234")
        sisbanco = Banco()
        sisbanco.cadastrar(conta)
        sisbanco.cadastrar(conta2)
        sisbanco.creditar("123",10)
        sisbanco.transferir("123", "234", 10)
        self.assertEqual(conta2.get_saldo(), 10)
        self.assertEqual(conta.get_saldo(), 0.0)
    
    def teste_taxa_poupanca(self):
        conta = ContaPoupanca("123")
        sisbanco = Banco()
        sisbanco.cadastrar(conta)
        self.assertEqual(sisbanco.get_taxa_poupanca(), 0.001)
        sisbanco.set_taxa_poupanca(0.1)
        self.assertEqual(sisbanco.get_taxa_poupanca(), 0.1)

    def teste_taxa_imposto(self):
        conta = ContaImposto("123")
        sisbanco = Banco()
        sisbanco.cadastrar(conta)
        self.assertEqual(sisbanco.get_taxa_imposto(), 0.001)
        sisbanco.set_taxa_imposto(0.1)
        self.assertEqual(sisbanco.get_taxa_imposto(), 0.1)
    
    