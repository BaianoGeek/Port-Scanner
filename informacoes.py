def escolher_portas():
    top_10_ports = [20, 21, 22, 23, 25, 25, 50, 53, 67, 68]
    top_15_ports = [20, 21, 22, 23, 25, 25, 50, 53, 67, 68, 69, 80, 110, 123, 137]
    top_20_ports = [20, 21, 22, 23, 25, 25, 50, 53, 67, 68, 69, 80, 110, 123, 137, 138, 139, 143, 161, 443]

    print ("\nSelecione uma lista de portas a ser Utilizada: ")
    print ("1 - Lista com 10 portas")
    print ("2 - Lista com 15 portas")
    print ("3 - Lista com 20 portas")

    escolha = input("\n >>> ")

    lista_escolhida = []

    if (escolha == '1'):
        lista_escolhida = top_10_ports
        return lista_escolhida
    elif(escolha == '2'):
        lista_escolhida = top_15_ports
        return lista_escolhida
    else:
        lista_escolhida = top_20_ports
        return lista_escolhida
