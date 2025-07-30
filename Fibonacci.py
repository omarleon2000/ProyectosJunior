while True:
    limite = int(input("Digite um número limte: "))
    a, b = 0, 1
    while a <= limite:
        print(a, end=" ")
        a, b = b, a + b
    print()
    continuar = input("Desea continuar? (s/n)")
    if continuar != "s":
        break