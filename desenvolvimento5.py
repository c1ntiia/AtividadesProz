def calculadora_interativa():
    while True:
        print("\n1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        opcao = input("\nDigite o número para a operação correspondente: ")
        
        if opcao == "0":
            print("Sistema encerrado.")
            break
            
        if opcao not in ["1", "2", "3", "4"]:
            print("Essa opção não existe")
            continue
            
        try:
            val1 = float(input("Insira o primeiro valor: "))
            val2 = float(input("Insira o segundo valor: "))
            
            if opcao == "1":
                print(f"Resultado: {val1 + val2}")
            elif opcao == "2":
                print(f"Resultado: {val1 - val2}")
            elif opcao == "3":
                print(f"Resultado: {val1 * val2}")
            elif opcao == "4":
                if val2 == 0:
                    print("Erro: Não é possível dividir por zero.")
                else:
                    print(f"Resultado: {val1 / val2}")
                    
        except ValueError:
            print("Erro: Insira apenas valores numéricos válidos.")

calculadora_interativa()