def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

a = int(input("Value a: "))
b = int(input("Value b: "))

try:
    d = modinv(a, b)
    print(f"Euclid of {a} module {b} is: {d}")
except Exception as e:
    print(e)
