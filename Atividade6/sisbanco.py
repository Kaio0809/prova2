from abc import ABC, abstractmethod
from excecoes import VIException, SIException, CEException, CIException, TJIException

class ContaAbstrata(ABC):
    def __init__(self, numero:str):
        self.__numero = numero
        self._saldo = 0.0

    def creditar(self, valor:float) -> None:
        if valor >= 0:
            self._saldo += valor
        else:
            raise VIException
   
    @abstractmethod
    def debitar(self, valor:float) -> None:
        pass
   
    def get_numero(self) -> str:
        return self.__numero 
   
    def get_saldo(self) -> float:
        return self._saldo


class Conta(ContaAbstrata):
    def __init__(self, numero:str):
        super().__init__(numero)

    def debitar(self, valor:float) -> None:
        if valor >= 0:
            if self._saldo >= valor:
                self._saldo -= valor
            else:
                raise SIException
        else:
            raise VIException

class ContaPoupanca(Conta):
    def __init__(self, numero:str):
        super().__init__(numero)

    def render_juros(self, taxa:float) -> None:
        if taxa > 0:
            self.creditar(self.get_saldo() * taxa)
        else:
            raise TJIException

class ContaEspecial(Conta):
    def __init__(self, numero:str):
        super().__init__(numero)
        self.__bonus = 0 

    def render_bonus(self) -> None:
        super().creditar(self.__bonus)
        self.__bonus = 0

    def creditar(self, valor:float) -> None:
        self.__bonus += valor * 0.01
        super().creditar(valor)

class ContaImposto(ContaAbstrata):
    def __init__(self, numero:str):
        super().__init__(numero)
        self.__taxa = 0.001

    def debitar(self, valor:float) -> None:
        if valor >= 0:
            if self._saldo >= (valor + (valor*self.__taxa)):
                self._saldo -= (valor + (valor * self.__taxa))
            else:
                raise SIException
        else:
            raise VIException
        
    def get_taxa(self) -> float:
        return self.__taxa

    def set_taxa(self, taxa:float) -> None:
        self.__taxa = taxa


class Banco:
    def __init__(self, taxa_poupanca:float=0.001, taxa_imposto:float=0.001):
        self.__contas = []
        self.__taxa_poupanca = taxa_poupanca
        self.__taxa_imposto = taxa_imposto

    def cadastrar(self, conta: ContaAbstrata) -> None:
        if conta is not None and isinstance(conta, ContaAbstrata):
            if isinstance(conta, ContaImposto):
                conta.set_taxa(self.__taxa_imposto)
            if conta in self.__contas:
                raise CEException
            else:
                self.__contas.append(conta)
        else:
            raise VIException()
        
    def procurar(self, numero:str) -> ContaAbstrata:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def creditar(self, numero:str, valor:float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.creditar(valor)
        else:
            raise CIException

    def debitar(self, numero:str, valor:float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.debitar(valor)
        else:
            raise CIException

    def saldo(self, numero:str) -> float:
        conta = self.procurar(numero)
        if conta is not None:
            return conta.get_saldo()
        else:
            raise CIException

    def transferir(self, origem:str, destino:str, valor:float) -> None:
        conta_origem = self.procurar(origem)
        if conta_origem is not None:
            conta_destino = self.procurar(destino)
            if conta_destino is not None:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
            else:
                raise CIException
        else:
            raise CIException

    def get_taxa_poupanca(self) -> float:
        return self.__taxa_poupanca
      
    def set_taxa_poupanca(self, taxa:float) -> None:
        self.__taxa_poupanca = taxa

    def get_taxa_imposto(self) -> float:
        return self.__taxa_imposto
      
    def set_taxa_imposto(self, taxa:float) -> None:
        self.__taxa_imposto = taxa
        for conta in self.__contas:
            if isinstance(conta, ContaImposto):
                conta.set_taxa(self.__taxa_imposto)

    def render_juros(self, numero:str) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            if isinstance(conta, ContaPoupanca):
                conta.render_juros(self.__taxa_poupanca)
        else:
            raise CIException


    def render_bonus(self, numero:str) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            if isinstance(conta, ContaEspecial):
                conta.render_bonus()
        else:
            raise CIException
    
