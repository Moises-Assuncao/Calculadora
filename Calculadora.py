def calculadora():
    while True:
        print("Calculadora Simples")
        print(" ")
        print("1. Adição")
        print("2. Multiplicação")
        print("3. Divisão")
        print("4. Subtração")
        print("s. Sair")

        operacao = input("Digite uma das opções: ")

        if operacao == "s" or operacao == "S":
            print("Sessão finalizada!")
            break

        if operacao not in ["1", "2", "3", "4"]:
            print("Erro, tente novamente!")
            continue

        numero1  = float(input("digite o primeiro nuumero: "))
        numero2  = float(input("digite o segundo nuumero: "))

        if operacao == "1":
            resultado = numero1 + numero2
            print(" o resultado da adição é: ", resultado)
        elif operacao == "2":
            resultado = numero1 * numero2
            print(" o resultado da multiplicação é: ", resultado)
        elif operacao == "4":
            resultado = numero1 - numero2
            print(" o resultado da subtração é: ", resultado)
        else:
            if numero2 == 0:
                print("erro, o numero é 0. tente novamente!")
                continue
            else:
                resultado = numero1 / numero2
                print(" o resultado da divisão é: ", resultado)

calculadora()