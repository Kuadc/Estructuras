from Persona import Persona

import random
from HashBucket import HashBucket
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def proximo_primo(n):
    n += 1
    while not es_primo(n):
        n +=1
    return n

if __name__ == "__main__":
    #tabla = HashTable(9000)
    n = 90
    m=proximo_primo(n)
    print(f"{m}")
    num = 76399

    band = True
    if not band:
        for i in range(10):
            n = random.randint(10100, 11900)
            print(f"{n}")

    n = 100
    c = 3
    m = n//0.7
    total =int((n//3) * 1.2)
    print(f"n_{n}")
    print(f"c_{c}")
    print(f"m_{m}")
    print(f"total_{total}")
    hash = num %n
    print("primer hash:", hash)






