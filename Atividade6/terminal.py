from sisbanco import *

def terminal():
   sisbanco = Banco()
   while(True):
      print("\nSisBanco::Bem-Vindo!")
      print(".::Opcoes::.")
      print("[0] Cadastrar Conta")
      print("[1] Creditar")
      print("[2] Debitar")
      print("[3] Transferir")
      print("[4] Consultar Saldo")
      print("[5] Render Juros")
      print("[6] Render Bonus")
      print("[7] Alterar Taxa_Juros")      
      print("[8] Alterar Taxa_Imposto")
      print("[9] Sair\n")
      opcao = input("Digite:")
      if opcao.isdigit():
         opcao = int(opcao)
      else:
         print("Opção Inválida!")
         continue
      if opcao == 0:
         pass
         #qual tipo de conta a ser criada: 
         print("S - Simples  | P - Poupanca | E - Especial | I - Imposto")
         tipo = str(input("Tipo de Conta: ")).capitalize()
         #solicite o numero da conta a ser criada
         numero = str(input("Número da conta: "))
         #instancie uma conta do tipo selecionado com esse numero
         if tipo == "S":
            conta = Conta(numero)
         elif tipo == "P":
            conta = ContaPoupanca(numero)
         elif tipo == "E":
            conta = ContaEspecial(numero)
         elif tipo == "I":
            conta = ContaImposto(numero)
         else:
            print("Opção inválida!")
         #cadastre a conta no sisbanco
         try:
            sisbanco.cadastrar(conta)
         except CEException as e:
            e.print_mensagem_erro()
         except VIException as e:
            e.print_mensagem_erro()

      elif opcao == 1:
         pass
         #solicite o numero da conta alvo
         conta = str(input("Número da Conta: "))
         #solicite o valor a ser creditado
         valor = float(input("Valor creditado: "))
         #realize a operacao de credito no sisbanco
         try:
            sisbanco.creditar(conta, valor)
         except CIException as e:
            e.print_mensagem_erro()
         except VIException as e:
            e.print_mensagem_erro()


      elif opcao == 2:
         pass
         #solicite o numero da conta alvo
         conta = str(input("Número da Conta: "))
         #solicite o valor a ser debitado
         valor = float(input("Valor Debitado: "))
         #realize a operacao de debito no sisbanco
         try:
            sisbanco.debitar(conta, valor)
         except CIException as e:
            e.print_mensagem_erro()
         except VIException as e:
            e.print_mensagem_erro()
         except SIException as e:
            e.print_mensagem_erro()
         

      elif opcao == 3:
         pass
         #solicite o numero da conta origem
         conta_origem = str(input("Conta Origem: "))
         #solicite o numero da conta destino
         conta_destino = str(input("Conta Destino: "))
         #solicite o valor a ser transferido
         valor = float(input("Valor: "))
         #realize a operacao de transferencia no sisbanco
         try:
            sisbanco.transferir(conta_origem, conta_destino, valor)
         except CIException as e:
            e.print_mensagem_erro()
         except VIException as e:
            e.print_mensagem_erro()
         except SIException as e:
            e.print_mensagem_erro()


      elif opcao == 4:
         pass
         #solicite o numero da conta alvo
         conta = str(input("Número da conta: "))
         #realize a operacao de obtencao de saldo no sisbanco
         try:
            saldo = sisbanco.saldo(conta)
            #exiba o saldo na tela
            print(f"O Saldo na conta é de {saldo:.2f} reais!")
         except CIException as e:
            e.print_mensagem_erro()
      
      elif opcao == 5:
         pass
         #solicite o numero da conta alvo
         conta = str(input("Número da Conta: "))
         #realize a operacao correcao da poupanca no sisbanco
         try:
            sisbanco.render_juros(conta)
         except CIException as e:
            e.print_mensagem_erro()
         except TJIException as e:
            e.print_mensagem_erro()
      
      elif opcao == 6:
         pass
         #solicite o numero da conta alvo
         conta = str(input("Número da Conta: "))
         #realize a operacao conversao/rendimento de bonus no sisbanco
         try:
            sisbanco.render_bonus(conta)
         except CIException as e:
            e.print_mensagem_erro()
      
      elif opcao == 7:
         pass
         #solicite a nova taxa de correcao da poupanca]
         taxa = float(input("Nova Taxa: "))
         #realize a operacao de alteracao da taxa no sisbanco
         try:
            sisbanco.set_taxa_poupanca(taxa)
         except TJIException as e:
            e.print_mensagem_erro()

      elif opcao == 8:
         pass
         #solicite a nova taxa de imposto
         try:
            taxa = float(input("Nova Taxa: "))
         #realize a operacao de alteracao da taxa no sisbanco
            sisbanco.set_taxa_imposto(taxa)
         except TJIException as e:
            e.print_mensagem_erro()
         except TypeError:
            print("Error\nDigite um número válido! ")
      elif opcao == 9:
         print("SisBanco::Bye!")
         break

if __name__ == "__main__":
   terminal()