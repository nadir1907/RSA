from random import randrange, getrandbits, randint
from math import gcd

from sympy import mod_inverse


# Geht nicht für die Zahl 462376535723, obwohl Prim


def miller_rabin(p):
    r = 0  # Zähler
    # Wenn p 2 wird steht hier p-1 ist 1 und dann passt 2 bis 1 nicht mehr
    a = randrange(2, p - 1)  # Random Zahl
    s = p - 1  # Exponent von a, benötigt für Berechnung

    
    #print("a = " + str(a))
    # Zerlge p-1 = 2^r*s
    while s % 2 == 0:
        s = s // 2
        r = r + 1
    #print("p-1 = " + str((p - 1)) + " = " + "2^" + str(r) + "*" + str(s))

    # Falls y =  +-1 mod p
    y = pow(a, s, p)
    #print(str(a) + "^" + str(s) + " = " + str(y) + " mod " + str(p))
    if y == 1:
        return True
    if y == -1:
        return True

    while r > 0:
        s *= 2  # Nur fürs Print
        y2 = (y * y) % p
        #print(str(a) + "^" + str(s) + " = " + str(y2) + " mod " + str(p))
        if y2 == 1:
            return False
        if y2 == -1:
            return True
        y = y2
        r -= 1
    return False


def sieve_of_eratosthenes():
    bit_length = 2048

    # Berechne die kleinste und größte Zahl mit der gegebenen Bitlänge
    min_number = pow(2, bit_length - 1)  # 10...0
    max_number = pow(2, bit_length) - 1  # 11...0

    # Erstelle einen Zahlenbereich als Generator
    sieve_numbers = (num for num in range(min_number, max_number + 1))
    prime_sieve_numbers = []

    for num in sieve_numbers:
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
            prime_sieve_numbers.append(num)

        #binary = bin(num)[2:]
        #if len(binary) == 1024:
        #    print(num)


def generate_prime(bits):
    # Generiere Random Zahl
    prime = getrandbits(bits)
    # Check ob prim
    while not miller_rabin(prime):
        prime = getrandbits(bits)
    return prime


def generate_keys(bits):
    p = generate_prime(bits)
    print("p " + str(p))
    q = generate_prime(bits)
    print(str("q " + str(q)))
    n = p * q
    e = randint(2, n - 1)
    phi = (p - 1) * (q - 1)
    print("phi = " + str(phi))

    # e muss prim sein und ggt 1
    while not miller_rabin(e) and gcd(e, phi) != 1:
        e = randint(2, n - 1)

    print("e = " + str(e))
    # Exponent d berechnen
    d = mod_inverse(e, phi)
    print("d= " + str(d))

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


def encrypt(message, public_key):
    n, e = public_key
    print("aus encrypt: " + str(n) + " " + str(e))
    cipher = pow(message, e, n)
    return cipher


def decrypt(cipher, private_key):
    n, d = private_key
    message = pow(cipher, d, n)
    return message


######MAIN######

bits = 4
public_key, private_key = generate_keys(bits)

m = "1231524"
cipher = encrypt(bits, public_key)
decrypted = decrypt(cipher, private_key)

print("Message = " + m)
print("Encrypted Message = " + str(cipher))
print("Decrypted Message = " + str(decrypted))

#number = int(input("Enter a number: "))  # Die Zahl die man testen will
#if miller_robin(number):
#    print("evtl. Primzahl")
#else:
#    print("Keine Primzahl")

#sieb()
