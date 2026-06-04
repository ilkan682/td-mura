u = 1  # Valeur initiale u0

# On pousse la boucle jusqu'à 1000 itérations
for i in range(1000):
    u = (2 * u ** 2 + 1) / (u ** 2 + 1)

    # On affiche uniquement les étapes cibles
    if i == 9:  # Équivaut à u10
        print(f"u10   = {u}")
    elif i == 99:  # Équivaut à u100
        print(f"u100  = {u}")
    elif i == 999:  # Équivaut à u1000
        print(f"u1000 = {u}")

# ==============================================================================
# COMPARAISON DE L'EXÉCUTION (Récursif vs Itératif) :
# L'approche itérative (la boucle for) est infiniment plus efficace.
# - La version récursive sature la mémoire et plante dès que n dépasse 30.
# - La version itérative met à jour une seule variable en temps réel.
#   Elle calcule u1000 de manière instantanée sans aucun effort pour la machine.
# ==============================================================================

# ==============================================================================
# OBSERVATION POUR LES GRANDES VALEURS DE N :
# On observe une convergence très rapide de la suite.
# Dès le terme u6, la valeur se stabilise et reste strictement identique
# pour u10, u100 et u1000 (1.618033988749895).
# La suite tend vers une limite finie qui est le Nombre d'Or : (1 + sqrt(5)) / 2.
# ==============================================================================