def u(n):
    """
    Fonction récursive qui calcule le n-ième terme de la suite.
    """
    # 1. Cas de base (condition d'arrêt de la récursivité)
    if n == 0:
        return 1

    # 2. Cas récursif
    else:
        # On calcule et on stocke le terme précédent u(n-1)
        # Cela évite à l'ordinateur de refaire le même calcul deux fois
        u_prec = u(n - 1)

        # On applique la formule : (2 * u_n^2 + 1) / (u_n^2 + 1)
        numerateur = 2 * (u_prec ** 2) + 1
        denominateur = (u_prec ** 2) + 1

        return numerateur / denominateur


# Affichage des premiers termes jusqu'à u_10
print("--- Termes jusqu'à u_10 ---")
for i in range(11):  # range(11) s'arrête à 10
    print(f"u({i}) = {u(i)}")

# Affichage des termes jusqu'à u_30
print("\n--- Termes jusqu'à u_30 ---")
for i in range(31):  # range(31) s'arrête à 30
    print(f"u({i}) = {u(i)}")