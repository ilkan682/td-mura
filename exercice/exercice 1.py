# ==============================================================================
# Exercice 1 : Calcul des mensualités et tableau d'amortissement d'un prêt
# ==============================================================================

print("Calcul d'un prêt immobilier ou d'un crédit à la consommation.")

# ------------------------------------------------------------------------------
# 1. SAISIE DES DONNÉES PAR L'UTILISATEUR
# ------------------------------------------------------------------------------
# On récupère le montant du capital emprunté (converti en nombre décimal 'float')
capital_initial = float(input("Entrer le montant du prêt ou crédit: "))

# On récupère le taux d'intérêt annuel en pourcentage (ex: 3 pour 3%)
taux_annuel_pourcent = float(input("Entrer le taux annuel en %: "))

# On récupère la durée du crédit en années (convertie en entier 'int')
annees = int(input("Entrer le nombre d'années: "))

# ------------------------------------------------------------------------------
# 2. CALCULS PRÉLIMINAIRES
# ------------------------------------------------------------------------------
# Conversion du taux annuel de pourcentage en valeur décimale mensuelle
# Exemple : 3% annuel -> 3 / 100 = 0.03 -> 0.03 / 12 = 0.0025 par mois
taux_mensuel = (taux_annuel_pourcent / 100) / 12

# Calcul du nombre total de mensualités (le nombre de mois de remboursement)
nombre_mois = annees * 12

# Calcul de la mensualité constante à l'aide de la formule financière standard :
# Mensualité = Capital * [ taux_mensuel / (1 - (1 + taux_mensuel)^(-nombre_mois)) ]
mensualite = capital_initial * (taux_mensuel / (1 - (1 + taux_mensuel)**(-nombre_mois)))

# ------------------------------------------------------------------------------
# 3. CALCUL DES INTÉRÊTS TOTAUX (Pour l'affichage du résumé)
# ------------------------------------------------------------------------------
# Pour calculer le total des intérêts remboursés sur toute la durée du prêt,
# on simule l'amortissement en boucle en amont.
total_interets = 0
capital_restant_simulation = capital_initial

for mois in range(1, nombre_mois + 1):
    # Les intérêts du mois sont calculés sur le capital restant dû au début du mois
    interet_du_mois = capital_restant_simulation * taux_mensuel
    total_interets += interet_du_mois
    
    # Le capital remboursé ce mois-ci est la mensualité moins les intérêts du mois
    capital_rembourse_du_mois = mensualite - interet_du_mois
    
    # On met à jour le capital restant dû pour le mois suivant
    capital_restant_simulation -= capital_rembourse_du_mois

# ------------------------------------------------------------------------------
# 4. AFFICHAGE DU RÉSUMÉ DU CRÉDIT
# ------------------------------------------------------------------------------
# On affiche les résultats globaux arrondis selon le format de l'image exemple
print(f"La mensualité avec intérêts est de {mensualite:.2f} euros")
print(f"Le montant des intérêts remboursés sont de {total_interets:.2f} euros.")
print(f"Le taux mensuel est de {taux_mensuel:.4f}") # Affichage de base du taux
print() # Ligne vide pour aérer la console

# ------------------------------------------------------------------------------
# 5. GÉNÉRATION ET AFFICHAGE DU TABLEAU D'AMORTISSEMENT
# ------------------------------------------------------------------------------
print("Tableau d'amortissement :")
# Affichage de la ligne d'en-tête du tableau avec les séparateurs " - "
print("Mois - Mensualité - Intérêts - Capital remboursé - Capital restant du - Intérêts remboursés")

# Réinitialisation des variables pour le vrai affichage du tableau
capital_restant = capital_initial
cumul_interets = 0

# Boucle 'for' pour parcourir chaque mois un par un, de 1 jusqu'au nombre total de mois
for mois in range(1, nombre_mois + 1):
    
    # A. Calcul des intérêts pour le mois en cours
    interet_du_mois = capital_restant * taux_mensuel
    
    # B. Cumul des intérêts payés jusqu'à ce mois-ci (dernière colonne)
    cumul_interets += interet_du_mois
    
    # C. Calcul de la part de capital remboursé dans la mensualité de ce mois
    capital_rembourse_du_mois = mensualite - interet_du_mois
    
    # D. Mise à jour du capital restant dû à la banque
    capital_restant -= capital_rembourse_du_mois
    
    # E. AJUSTEMENT DE SÉCURITÉ POUR LE DERNIER MOIS
    # À cause des arrondis informatiques sur les nombres flottants, le capital restant 
    # du dernier mois peut afficher -0.01 ou 0.01 au lieu de strictement 0.
    if mois == nombre_mois:
        capital_restant = 0.0

    # F. AFFICHAGE DE LA LIGNE DU MOIS EN COURS
    # Les valeurs sont formatées à une décimale (.1f) pour correspondre au visuel demandé,
    # excepté pour le cumul des intérêts qui conserve deux décimales (.2f).
    print(f" {mois}  -   {mensualite:.1f}   -   {interet_du_mois:.1f}   -     {capital_rembourse_du_mois:.1f}     -       {capital_restant:.1f}     -   {cumul_interets:.2f}")