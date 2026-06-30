def calculadora():
    while True:
        print("\n" + "="*30)
        print("      MENU DA CALCULADORA      ")
        print("="*30)
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        print("="*30)
        
        opcao = input("Escolha a opção desejada: ")
        
        if opcao == "0":
            print("\nA encerrar a calculadora. Até breve!")
            break
        
        if opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Introduza o primeiro número: "))
                num2 = float(input("Introduza o segundo número: "))
                
                if opcao == "1":
                    resultado = num1 + num2
                    print(f"\nResultado da Soma: {num1} + {num2} = {resultado}")
                
                elif opcao == "2":
                    resultado = num1 - num2
                    print(f"\nResultado da Subtração: {num1} - {num2} = {resultado}")
                
                elif opcao == "3":
                    resultado = num1 * num2
                    print(f"\nResultado da Multiplicação: {num1} × {num2} = {resultado}")
                
                elif opcao == "4":
                    if num2 == 0:
                        print("\nErro: Não é possível dividir por zero!")
                    else:
                        resultado = num1 / num2
                        print(f"\nResultado da Divisão: {num1} ÷ {num2} = {resultado}")
                        
            except ValueError:
                print("\nErro: Por favor, introduza apenas números válidos.")
        
        else:
            print("\nEssa opção não existe! Por favor, escolha um número de 0 a 4.")

calculadora()