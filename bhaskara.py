def Bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("\nValor de x1: {0}".format(x1))
    print("\nValor de x2: {0}".format(x2))

if __name__ == "__main__":
    while True:
        print("Calculando as raízes de uma equação do 2° grau\n")

        a = float(input("Digite um valor para A: "))
        b = float(input("Digite um valor para B: "))
        c = float(input("Digite um valor para C: "))

        Bhaskara(a, b, c)

        continua = input("\nDeseja sair? Digite S ou Enter para um novo cálculo: \n")
        if (continua == "S"):
            break