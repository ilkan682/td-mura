# ==============================================================================
# Exercice 1 : Calcul des mensualités et tableau d'amortissement d'un prêt
# ==============================================================================

# Affiche le message d'introduction de l'application dans la console
print("Calcul d'un prêt immobilier ou d'un crédit à la consommation.")

# ------------------------------------------------------------------------------
# 1. SAISIE DES DONNÉES PAR L'UTILISATEUR
# ------------------------------------------------------------------------------

# input() reçoit la saisie sous forme de texte.
# float() transforme ce texte en nombre décimal (ex: 20000.0) pour pouvoir faire des calculs précis.
capital_initial = float(input("Entrer le montant du prêt ou crédit: "))

# Récupère le taux d'intérêt annuel saisi par l'utilisateur (ex: 3 pour 3%)
taux_annuel_pourcent = float(input("Entrer le taux annuel en %: "))

# int() transforme le texte saisi en nombre entier car une durée de crédit s'exprime en années pleines (ex: 6)
annees = int(input("Entrer le nombre d'années: "))

# ------------------------------------------------------------------------------
# 2. CALCULS PRÉLIMINAIRES
# ------------------------------------------------------------------------------

# On divise par 100 pour passer du pourcentage à la valeur décimale (3 % -> 0.03).
# Puis on divise par 12 pour obtenir le taux applicable chaque mois (0.03 / 12 = 0.0025).
taux_mensuel = (taux_annuel_pourcent / 100) / 12

# Calcule la durée totale en mois en multipliant les années par 12 (ex: 6 ans * 12 mois = 72 mois).
nombre_mois = annees * 12

# Formule financière standard pour obtenir une mensualité constante (fixe) :
# Le symbole '**' représente la puissance en Python (ex: (1 + taux)^(-nombre_mois)).
# Cela permet d'obtenir le montant exact à payer chaque mois comprenant à la fois une part d'intérêts et de capital.
mensualite = capital_initial * (taux_mensuel / (1 - (1 + taux_mensuel)**(-nombre_mois)))

# ------------------------------------------------------------------------------
# 3. CALCUL DES INTÉRÊTS TOTAUX (Pour l'affichage du résumé)
# ------------------------------------------------------------------------------

# On crée un compteur pour cumuler la somme totale des intérêts, initialisé à 0.
total_interets = 0

# On duplique le capital de départ dans une variable temporaire dédiée à la simulation en arrière-plan.
capital_restant_simulation = capital_initial

# Boucle 'for' qui simule le déroulement du crédit mois par mois pour calculer les intérêts totaux en amont.
# range(1, 73) va faire tourner la boucle du mois 1 jusqu'au mois 72 (si 6 ans).
for mois in range(1, nombre_mois + 1):
    
    # La banque calcule les intérêts du mois sur la base de ce qu'il te reste à rembourser.
    interet_du_mois = capital_restant_simulation * taux_mensuel
    
    # On ajoute les intérêts découverts ce mois-ci au compteur global des intérêts cumulés.
    total_interets += interet_du_mois
    
    # Ce que tu rembourses réellement à la banque (capital), c'est ta mensualité fixe moins la part d'intérêts.
    capital_rembourse_du_mois = mensualite - interet_du_mois
    
    # On met à jour le capital restant dû en soustrayant la part de capital qui vient d'être remboursée.
    capital_restant_simulation -= capital_rembourse_du_mois

# ------------------------------------------------------------------------------
# 4. AFFICHAGE DU RÉSUMÉ DU CRÉDIT
# ------------------------------------------------------------------------------

# Affiche la mensualité calculée. Le format ':.2f' force l'affichage de deux chiffres après la virgule (ex: 303.87).
print(f"La mensualité avec intérêts est de {mensualite:.2f} euros")

# Affiche le montant cumulé de tous les intérêts que la banque aura perçus à la fin du crédit.
print(f"Le montant des intérêts remboursés sont de {total_interets:.2f} euros.")

# Affiche le taux appliqué chaque mois. Le format ':.4f' affiche quatre chiffres après la virgule (ex: 0.0025).
print(f"Le taux mensuel est de {taux_mensuel:.4f}")

# Affiche une ligne vide dans la console pour aérer la présentation avant le tableau.
print() 

# ------------------------------------------------------------------------------
# 5. GÉNÉRATION ET AFFICHAGE DU TABLEAU D'AMORTISSEMENT
# ------------------------------------------------------------------------------

# Imprime le titre de la section du tableau
print("Tableau d'amortissement :")

# Imprime la ligne d'en-tête qui sert de titres pour les colonnes du tableau, séparés par des " - "
print("Mois - Mensualité - Intérêts - Capital remboursé - Capital restant du - Intérêts remboursés")

# On réinitialise la variable qui va suivre la diminution du capital réel au fur et à mesure de l'affichage.
capital_restant = capital_initial

# On réinitialise un compteur pour afficher la progression des intérêts remboursés ligne par ligne.
cumul_interets = 0

# Deuxième boucle 'for' qui va, cette fois-ci, calculer ET afficher chaque ligne du tableau dans la console.
for mois in range(1, nombre_mois + 1):
    
    # A. Calcule les intérêts dus pour le mois actuel en fonction du capital restant à rembourser.
    interet_du_mois = capital_restant * taux_mensuel
    
    # B. Ajoute les intérêts du mois en cours au cumul total affiché dans la toute dernière colonne.
    cumul_interets += interet_du_mois
    
    # C. Calcule la part de la mensualité dédiée à amortir (rembourser) la dette de base.
    capital_rembourse_du_mois = mensualite - interet_du_mois
    
    # D. Calcule la nouvelle dette restante en soustrayant le capital fraîchement remboursé.
    capital_restant -= capital_rembourse_du_mois
    
    # E. AJUSTEMENT DE SÉCURITÉ POUR LE DERNIER MOIS :
    # Les ordinateurs ayant du mal avec les arrondis des chiffres infinis après la virgule (les "floats"),
    # le capital restant au dernier mois pourrait afficher '0.01' ou '-0.01'. Cet 'if' force la valeur à pile '0.0'.
    if mois == nombre_mois:
        capital_restant = 0.0

    # F. AFFICHAGE DE LA LIGNE DU MOIS EN COURS :
    # La lettre 'f' devant les guillemets permet d'injecter des variables au milieu du texte à l'aide des accolades {}.
    # Le suffixe ':.1f' arrondit la valeur à 1 chiffre après la virgule pour coller au modèle de la feuille de TD.
    # Seul 'cumul_interets' garde ':.2f' pour afficher les centimes exacts dans la dernière colonne.
    print(f" {mois}  -   {mensualite:.1f}   -   {interet_du_mois:.1f}   -     {capital_rembourse_du_mois:.1f}     -       {capital_restant:.1f}     -   {cumul_interets:.2f}")