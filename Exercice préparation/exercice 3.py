def u(n):
    # calcule le terme u_n = n^2 - n + 1
    return n**2 - n + 1

n = 0
# boucle tant que u(n) est strictement inférieur à 1000
while u(n) < 1000:
    # affiche la valeur actuelle de u(n)
    print(u(n))
    # passe au rang suivant
    n = n + 1

# lorsque la boucle s'arrête, n est le premier entier tel que u(n) >= 1000
# on l'affiche
print(n)
