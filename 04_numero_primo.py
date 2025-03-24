
#  Escribe un programa que se encargue de comprobar si un número es o no primo.
#  Hecho esto, imprime los números primos entre 1 y 100.


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_del_1_al_100():
    for n in range(1, 101):
        if es_primo(n):
            print(f"{n} es primo.")
        else:
            print(f"{n} no es primo.")

primos_del_1_al_100()