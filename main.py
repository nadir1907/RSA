from random import randrange, getrandbits, randint, choice
from math import gcd
from sympy import mod_inverse
import time


# Geht nicht für die Zahl 462376535723, obwohl Prim


def miller_rabin(p):
    L = [2, 3]
    r = 0  # Zähler
    if p in L:
        return True
    else:
        a = randrange(2, p - 1)  # Random Zahl
    s = p - 1  # Exponent von a, benötigt für Berechnung

    # Zerlge p-1 = 2^r*s
    while s % 2 == 0:
        s = s // 2
        r = r + 1

    # Falls y =  +-1 mod p
    y = pow(a, s, p)
    if y == 1:
        return True
    if y == -1:
        return True

    while r > 0:
        y2 = (y * y) % p
        if y2 == 1:
            return False
        if y2 == -1:
            return True
        y = y2
        r -= 1
    return False


def sieve_of_eratosthenes():
    bit_length = 1024

    sieve_numbers = []
    while len(sieve_numbers) == 0 or len(sieve_numbers) < 2:
        for i in range(100):
            number = getrandbits(bit_length)
            sieve_numbers.append(number)

        for num in reversed(sieve_numbers):
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
                sieve_numbers.remove(num)

        for num in reversed(sieve_numbers):
            if not miller_rabin(num):
                sieve_numbers.remove(num)

    return sieve_numbers


def generate_keys():
    start = time.time()
    prime_list = sieve_of_eratosthenes()
    p = choice(prime_list)
    q = choice(prime_list)
    while p == q:
        q = choice(prime_list)
    ende = time.time() - start
    print("Time: " + str(ende))
    n = p * q
    e = randint(2, n - 1)
    phi = (p - 1) * (q - 1)

    # e muss prim sein und ggt 1
    while not miller_rabin(e) and gcd(e, phi) != 1:
        e = randint(2, n - 1)

    # Exponent d berechnen
    d = mod_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


def encrypt(message, public_key):
    n, e = public_key
    cipher = pow(message, e, n)
    return cipher


def decrypt(cipher, private_key):
    n, d = private_key
    message = pow(cipher, d, n)
    return message


def utf8_to_int(message):
    return int.from_bytes(message.encode('utf-8'), byteorder='big')


def int_to_utf8(message):
    return bytearray(message.to_bytes((message.bit_length() + 7) // 8, byteorder='big')).decode('utf-8')


def chin_rest(p, q, d, encrypt):
    m1 = q
    m2 = p
    a1 = pow(encrypt, d % (m1 - 1), m1)
    a2 = pow(encrypt, d % (m2 - 1), m2)

######MAIN######

public_key, private_key = generate_keys()

m = "Test"
if isinstance(m, str):
    message = utf8_to_int(m)
    cipher = encrypt(message, public_key)
    decrypted = decrypt(cipher, private_key)
    decrypted_message = int_to_utf8(decrypted)

    print("Message = " + str(m))
    print("Encrypted Message = " + str(cipher))
    print("Decrypted Message = " + decrypted_message)
else:
    cipher = encrypt(m, public_key)
    decrypted = decrypt(cipher, private_key)

    print("Message = " + str(m))
    print("Encrypted Message = " + str(cipher))
    print("Decrypted Message = " + str(decrypted))
