# ==============================================================================
# Exercice 1 : Version officielle du professeur (Tableau d'amortissement)
# ==============================================================================

# Affiche le titre du programme dans la console
print("calcul d'un pret immobilier")

# ------------------------------------------------------------------------------
# 1. SAISIE DES DONNÉES UTILISATEUR
# ------------------------------------------------------------------------------
# input() lit le texte tapé, float() le convertit en nombre à virgule (ex: 20000.0)
s = float(input("entrer le montant du pret ou credit: "))

# Récupère le taux d'intérêt annuel (ex: 3 pour 3%)
t = float(input("entrer le taux annuel en %: "))

# int() convertit la saisie en nombre entier pour la durée en années (ex: 6)
n = int(input("entrer le nombre d'années: "))

# ------------------------------------------------------------------------------
# 2. CALCULS DE LA MENSUALITÉ ET DES INTÉRÊTS
# ------------------------------------------------------------------------------
# Calcul du taux mensuel : on divise par 12 (mois) et par 100 (pourcentage)
# Exemple : 3% -> 3 / 12 / 100 = 0.0025
tm = t / 12 / 100

# Formule du prof pour simplifier le calcul de la mensualité :
# 'a' représente le facteur de capitalisation : (1 + taux_mensuel)^(nombre_total_de_mois)
a = (1 + tm) ** (12 * n)

# Calcul du montant de la mensualité fixe 'm' à l'aide du facteur 'a'
m = s * tm * a / (a - 1)

# Calcul global du total des intérêts qui seront payés à la banque.
# Formule : (Montant de la mensualité * Nombre d'années * 12 mois) - Capital emprunté au départ
total_interets = (m * n * 12) - s

# ------------------------------------------------------------------------------
# 3. AFFICHAGE DU RÉSUMÉ DU PRÊT
# ------------------------------------------------------------------------------
print("\n--- Résumé du prêt ---")
# round(m, 2) permet d'arrondir le résultat à 2 chiffres après la virgule
print("La mensualité avec intérêt est de :", round(m, 2), "euros")
print("Le montant total des intérêts remboursés sera de :", round(total_interets, 2), "euros")
print("Le taux mensuel est de :", round(tm, 5))

# ------------------------------------------------------------------------------
# 4. EN-TÊTE DU TABLEAU D'AMORTISSEMENT
# ------------------------------------------------------------------------------
print("\nTableau d'amortissement :")
# Affiche les titres des colonnes séparés par des barres verticales '|'
print("Mois | Mensualité | Intérêts | Capital Remboursé | Capital Restant Dû | Intérêts Cumulés")
# Trace une ligne de séparation de 90 tirets pour faire propre
print("-" * 90)

# ------------------------------------------------------------------------------
# 5. BOUCLE DU TABLEAU (MOIS PAR MOIS)
# ------------------------------------------------------------------------------
# 'ir' sert de compteur pour le cumul des intérêts remboursés au fil des mois
ir = 0.0

# Boucle 'for' qui va tourner pour le nombre total de mois (ex: 6 * 12 = 72 fois)
# La variable 'j' commence à 0 et va jusqu'à (n * 12) - 1
for j in range(n * 12):
    
    # A. Calcule les intérêts du mois sur la base du capital actuel 's'
    i = tm * s          
    
    # B. Calcule la part de capital remboursé ce mois-ci (Mensualité fixe - Intérêts du mois)
    cr = m - i          
    
    # C. Calcule le capital restant dû théorique après ce mois (Ancien capital - Ce qu'on vient de rembourser)
    crd = s - cr        
    
    # D. Ajoute les intérêts de ce mois-ci dans le compteur de cumul
    ir = ir + i         
    
    # E. AFFICHAGE DE LA LIGNE DU MOIS :
    # {j+1:<3} : affiche le numéro du mois (j commence à 0 donc on fait +1) aligné à gauche sur 3 caractères
    # :<10, :<8, etc. servent à réserver un espace fixe pour chaque colonne pour que le tableau soit bien droit.
    # max(0, crd) permet de forcer l'affichage à 0 au dernier mois si jamais 'crd' devient légèrement négatif à cause des arrondis.
    print(f" {j+1:<3} | {round(m, 2):<10} | {round(i, 2):<8} | {round(cr, 2):<17} | {round(max(0, crd), 2):<19} | {round(ir, 2)}")
    
    # F. CRUCIAL : On met à jour la variable 's' avec la valeur du capital restant dû 'crd'
    # Ainsi, au prochain tour de boucle, le calcul des intérêts (Ligne 55) se basera sur la nouvelle somme restante.
    s = crd