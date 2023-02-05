def primo_linear(n):
    primos = [2]
    if n < 2:
        return "Valor inválido!"
    for i in range(3, n + 1):
        primo = 1 # primo começa com um valor verdadeiro
        x = int(i ** (1 / 2)) + 1
        for j in range(2, x):
            if i % j == 0:
                primo = 0 # se não for primo ele passa a ser um valor negativo
                break
        if primo:
            primos.append(i)
    return primos


def menu():
    n = int(input('Valor de N: '))
    print(primo_linear(n))


while True:
    menu()
