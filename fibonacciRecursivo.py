def fibonacci(n):
    if n < 0:
        return "Valor inválido! Tente com um número inteiro e positivo."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = int(input("Valor de N: "))
    print(fibonacci(n))


while True:
    main()
