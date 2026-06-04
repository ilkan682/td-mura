# u(n) = (2n²-1)/(n²+2)  →  quand n→∞, la limite est 2
def u(n):
    # on retourne directement la formule pour le rang n
    return (2*n**2 - 1) / (n**2 + 2)

# on teste avec des grands n pour observer la limite
print(u(10))    # 1.98...
print(u(100))   # 1.9998...
print(u(1000))  # 1.999998...  →  tend vers 2