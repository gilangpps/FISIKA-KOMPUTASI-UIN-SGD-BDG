# Fungsi metode bisection
def bisection(f, a, b, tol):
    if f(a) * f(b) > 0:
        print("a dan b tidak mengurung akar, tentukan nilai lain")
        return None

    c = (a + b) / 2

    while abs(f(c)) > tol:
        c = (a + b) / 2
        if f(a) * f(c) > 0:
            a = c
        else:  # Ini adalah perbaikan dari bagian logika
            b = c

    return c

# Fungsi persamaan kuadrat f(x) = x^2 - 4
def f(x):
    return x**2 - 4

# Input nilai awal
a = float(input('Tebakan Awal a = '))
b = float(input('Tebakan Awal b = '))
tol = float(input('Toleransi = '))

# Memanggil metode bisection
x = bisection(f, a, b, tol)

# Menampilkan hasil
if x is not None:
    print("Akar persamaan x = {:.6f}".format(x))
