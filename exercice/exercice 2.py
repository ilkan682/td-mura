# ==============================================================================
# Exercice 2 : Calcul des intérêts sur un placement (Suites récurrentes)
# ==============================================================================

# Affiche le titre de l'exercice dans la console
print("Calcul du capital acquis et de ses intérêts versés...")

# input() reçoit la saisie sous forme de texte.
# float() convertit ce texte en nombre à virgule pour faire les calculs.
placement_depart = float(input("Entrer le placement de départ: "))

# Récupère la somme injectée chaque mois (ex: 45 euros)
versement_mensuel = float(input("Entrer le montant du versement mensuel: "))

# Récupère le taux d'intérêt (ex: 2.3 pour 2.3%)
taux_annuel_pourcent = float(input("Entrer le taux annuel en %: "))

# int() convertit la saisie en nombre entier pour les années (ex: 8 ans)
annees = int(input("Entrer le nombre d'années: "))

# Calcule l'argent réel que tu as sorti de ta poche sans aucune aide de la banque.
# Formule : Placement initial + (Versements mensuels * 12 mois * Nombre d'années)
capital_sans_interets = placement_depart + (versement_mensuel * 12 * annees)


# ==============================================================================
# QUESTION 1 : Les intérêts sont calculés UNE FOIS PAR AN
# ==============================================================================
print("\n" + "-"*50)
print("Question 1 : Intérêts calculés une fois par an")
print("-"*50)

# On initialise le capital de la Question 1 avec les 300 € de départ
capital_q1 = placement_depart

# Convertit le pourcentage en valeur décimale mathématique (2.3 / 100 = 0.023)
taux_annuel = taux_annuel_pourcent / 100

# Convertit les années en mois (8 ans * 12 mois = 96 mois) car la boucle tourne au mois par mois
nombre_de_mois = annees * 12

# Boucle 'for' qui va se répéter 96 fois (du mois 1 au mois 96 inclus)
# La variable 'mois' augmente de 1 à chaque tour de boucle
for mois in range(1, nombre_de_mois + 1):
    
    # À chaque début de mois, on ajoute notre versement de 45 € dans la cagnotte
    capital_q1 += versement_mensuel
    
    # L'opérateur '%' (modulo) donne le reste de la division du mois en cours par 12.
    # Si le reste est égal à 0, cela signifie qu'une année complète (12 mois) vient de passer.
    if mois % 12 == 0:
        # On calcule les intérêts annuels accumulés sur tout l'argent présent dans le capital
        interets_annuels = capital_q1 * taux_annuel
        # On injecte directement ces intérêts dans le capital (ils s'ajoutent à la somme)
        capital_q1 += interets_annuels

# Calcule le bénéfice net : Capital final obtenu - Ton argent versé sans intérêts
interets_gagnes_q1 = capital_q1 - capital_sans_interets

# Affiche les résultats de la Q1. 
# {capital_q1:.2f} force l'affichage de deux chiffres après la virgule.
# {versement_mensuel:.0f} et {capital_sans_interets:.0f} affichent des nombres ronds (0 après la virgule).
print(f"Le capital acquis avec intérêts est de {capital_q1:.2f} euros au bout de {annees} ans avec des versements mensuels de {versement_mensuel:.0f} euros.")
print(f"Les intérêts gagnés au taux annuel de {taux_annuel_pourcent:.1f} % sont de {interets_gagnes_q1:.2f} euros.")
print(f"Sans placement avec intérêts le capital acqui serait de {capital_sans_interets:.0f} euros.")


# ==============================================================================
# QUESTION 2 : Les intérêts sont calculés UNE FOIS PAR MOIS
# ==============================================================================
print("\n" + "-"*50)
print("Question 2 : Intérêts calculés une fois par mois")
print("-"*50)

# On réinitialise un capital propre à la Question 2 avec les 300 € de départ
capital_q2 = placement_depart

# Comme la banque calcule les intérêts tous les mois, on divise le taux annuel par 12
# (2.3% / 100) / 12 = 0.0019166... d'intérêts appliqués chaque mois
taux_mensuel = (taux_annuel_pourcent / 100) / 12

# On relance la même boucle 'for' qui va tourner 96 fois (mois par mois)
for mois in range(1, nombre_de_mois + 1):
    
    # 1. On commence par ajouter le versement mensuel obligatoire de 45 €
    capital_q2 += versement_mensuel
    
    # 2. CHAQUE MOIS (sans condition 'if'), on applique directement le taux mensuel.
    # On calcule les intérêts générés ce mois-ci sur le capital actuel.
    interets_du_mois = capital_q2 * taux_mensuel
    # On ajoute immédiatement ces intérêts dans le capital pour le mois suivant
    capital_q2 += interets_du_mois

# Calcule le bénéfice net pour la méthode mensuelle
interets_gagnes_q2 = capital_q2 - capital_sans_interets

# Affiche les résultats de la Q2 avec le même formatage que la première partie
print(f"Le capital acquis avec intérêts est de {capital_q2:.2f} euros au bout de {annees} ans avec des versements mensuels de {versement_mensuel:.0f} euros.")
print(f"Les intérêts gagnés au taux annuel de {taux_annuel_pourcent:.1f} % sont de {interets_gagnes_q2:.2f} euros.")
print(f"Sans placement avec intérêts le capital acqui serait de {capital_sans_interets:.0f} euros.")