from math import ceil, log2
from random import randrange, choice

number = int(input("Enter a number: "))  # Die Zahl die man testen will


# Geht nicht für die Zahl 462376535723, obwohl Prim


def miller_robin(p):
    r = 0  # Zähler
    a = randrange(2, p - 1)  # Random Zahl
    s = p - 1  # Exponent von a, benötigt für Berechnung

    print("a = " + str(a))
    # Zerlge p-1 = 2^r*s
    while s % 2 == 0:
        s = s // 2
        r = r + 1
    print("p-1 = " + str((p - 1)) + " = " + "2^" + str(r) + "*" + str(s))

    # Falls y =  +-1 mod p
    y = pow(a, s, p)
    print(str(a) + "^" + str(s) + " = " + str(y) + " mod " + str(p))
    if y == 1:
        return True
    if y == -1:
        return True

    while r > 0:
        s *= 2  # Nur fürs Print
        y2 = (y * y) % p
        print(str(a) + "^" + str(s) + " = " + str(y2) + " mod " + str(p))
        if y2 == 1:
            return False
        if y2 == -1:
            return True
        y = y2
        r -= 1
    return False


def sieb_erstellen():
    bit_length = 1024

    # Berechne die kleinste und größte Zahl mit der gegebenen Bitlänge
    min_number = pow(2, bit_length - 1)  # 10...0
    max_number = pow(2, bit_length) - 1  # 11...0

    # Erstelle einen Zahlenbereich als Generator
    sieve_numbers = (num for num in range(min_number, max_number + 1))

    for _ in range(10):
        binary = bin(next(sieve_numbers))[2:]
        if len(binary) == 1024:
            print(next(sieve_numbers))


######MAIN######

#if miller_robin(number):
#    print("evtl. Primzahl")
#else:
#    print("Keine Primzahl")

sieb_erstellen()
