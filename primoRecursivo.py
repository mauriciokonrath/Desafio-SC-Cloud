def primo_recursivo(n, comeco=2, lista=None):
    if lista is None:
        lista = []
    if n < 2:
        return "Valor inválido!"
    if comeco > n:
        return lista
    primo = 1
    for i in range(2, comeco):
        if (comeco % i) == 0:
            primo = 0
            break
    if primo:
        lista.append(comeco)
    return primo_recursivo(n, comeco + 1, lista)


def menu():
    n = int(input('Valor de N: '))
    print(primo_recursivo(n))


while True:
    menu()
