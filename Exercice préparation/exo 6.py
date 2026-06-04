n = int(input("Entrer n : "))

# Initialisation des trois sommes à 0
S = 0
T = 0
U = 0

# La boucle commence à 1 car on ne peut pas diviser par i=0
for i in range(1, n + 1):
    S = S + 1 / i          # 1 + 1/2 + 1/3 + ... + 1/n
    T = T + 1 / (i ** 2)   # 1 + 1/2² + 1/3² + ...+ 1/n²
    U = U + 1 / (2 ** i)   # 1/2¹ + 1/2² + 1/2³ + ...+ 1/2^n

# Attention : pour la suite U, l'énoncé commence à 1 (qui correspond à 1/(2^0)).
# Comme notre boucle a démarré à i=1, on rajoute manuellement le "1" initial à la fin.
U = U + 1

# Affichage des résultats cachés derrière les calculs
print(f"Pour n = {n} :")
print(f"Somme S = {S}")
print(f"Somme T = {T}")
print(f"Somme U = {U}")

# ==============================================================================
# CONJECTURES POUR LES TROIS SUITES (À COLLER SOUS LE CODE) :
#
# 1. POUR LA SOMME S (Série Harmonique) :
# Quand n devient très grand, la somme S continue de grandir lentement, sans
# jamais s'arrêter. On conjecture que la suite DIVERGE vers +infini.
#
# 2. POUR LA SOMME T (Problème de Bâle) :
# Quand n augmente, la somme T se stabilise très vite autour de 1.6449...
# On conjecture que la suite CONVERGE vers une limite finie.
# (Les mathématiciens ont prouvé que cette limite exacte est pi² / 6).
#
# 3. POUR LA SOMME U (Série Géométrique de raison 1/2) :
# Plus n est grand, plus la somme U s'approche de la valeur 2, sans la dépasser.
# On conjecture que la suite CONVERGE vers la limite finie 2.
# ==============================================================================