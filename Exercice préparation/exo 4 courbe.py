from pylab import *

# 1. On définit la fonction de notre exercice
def f(x):
    y = (2 * x**2 + 1) / (x**2 + 1)
    return y

# 2. On place des points entre 0 et 4 (on avance de 0.1 en 0.1)
# Pour faire une boucle avec des nombres décimaux, on divise i par 10
for i in range(0, 40):
    x = i / 10
    plot(x, f(x), 'b*')  # 'b*' affiche des étoiles bleues

grid(True)  # Optionnel : ajoute un quadrillage pour mieux voir
show()

# ==============================================================================
# SENS DE VARIATION DE LA FONCTION F :
# La fonction est f(x) = (2x² + 1) / (x² + 1).
# Sa dérivée est f'(x) = 2x / (x² + 1)².
# Sur [0 ; +inf[, 2x >= 0 et le dénominateur (un carré) est toujours positif.
# Donc f'(x) >= 0, ce qui prouve que f est STRICTEMENT CROISSANTE sur [0 ; +inf[.
# ==============================================================================

# ==============================================================================
# DÉMONSTRATION QUE LA SUITE EST CROISSANTE (Par récurrence) :
# - Initialisation : u0 = 1 et u1 = f(1) = 1.5, donc u0 <= u1 (Vrai).
# - Hérédité : Si un <= un+1, comme f est croissante, elle conserve l'ordre.
#   On a donc f(un) <= f(un+1), ce qui donne un+1 <= un+2.
# - Conclusion : La suite (un) est STRICTEMENT CROISSANTE.
# ==============================================================================

# ==============================================================================
# DÉMONSTRATION QUE LA SUITE EST MAJORÉE PAR 2 :
# En modifiant l'écriture de f(x), on obtient : f(x) = 2 - 1/(x² + 1).
# Comme le terme 1/(x² + 1) est toujours strictement positif, on enlève
# toujours quelque chose à 2. Donc f(x) < 2 pour tout x réel.
# Par conséquent, tous les termes de la suite sont MAJORÉS PAR 2.
# ==============================================================================

# ==============================================================================
# CONVERGENCE ET VALEUR APPROCHÉE DE LA LIMITE :
# D'après le théorème de la convergence monotone, puisque la suite (un)
# est croissante et majorée par 2, elle CONVERGE vers une limite finie L.
# Cette limite vérifie l'équation f(L) = L, soit L³ - 2L² + L - 1 = 0.
# Graphiquement et numériquement, on trouve la valeur approchée :
# L approx 1.6180339887 (qui correspond exactement au Nombre d'Or).
# ==============================================================================