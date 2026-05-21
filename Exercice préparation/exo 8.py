# Initialisation des données
adherents = 500
cotisation_mensuelle = 10
total_cotisations = 0
nb_mois = 24  # 2 ans = 24 mois

print("--- ÉVOLUTION DES ADHÉRENTS MOIS PAR MOIS ---")
for mois in range(1, nb_mois + 1):
    # 1. Calcul du montant perçu ce mois-ci et ajout au total
    total_cotisations += adherents * cotisation_mensuelle

    # 2. Évolution du nombre d'adhérents pour le mois suivant
    # (-5% de départs, +30 arrivées)
    adherents = adherents * 0.95 + 30

    print(f"Mois {mois:2d} : {int(adherents)} adhérents")

print("-" * 45)
print(f"Montant total des cotisations perçues : {total_cotisations} euros")

# ==============================================================================
# RÉPONSES AUX QUESTIONS DE L'EXERCICE :
#
# 1. MONTANT TOTAL DES COTISATIONS PERÇUES EN 2 ANS :
# Le programme cumule chaque mois (le nombre d'adhérents actifs * 10 euros).
# On obtient un total de 127 758 euros perçus sur les 24 mois.
#
# 2. NOUVEAU MONTANT DE L'ADHÉSION POUR FINANCER L'INSTALLATION (20 000 €) :
# Attention au piège : l'installation coûte 20 000 euros AU TOTAL. Comme
# l'association gagne déjà 127 758 euros avec une adhésion à 10 euros, elle
# couvre déjà largement cette dépense !
#
# Si la question signifie "Quel doit être le prix pour obtenir EXACTEMENT
# 20 000 euros en 2 ans ?", on utilise une règle de trois (proportionnalité) :
# Le nombre total de "cotisations mensuelles individuelles" perçues en 2 ans
# est de 12 775,8 (car 127 758 € / 10 €).
#
# Nouveau tarif = Budget ciblé / Nombre total de cotisations
# Nouveau tarif = 20 000 / 12 775.8 approx 1.57 euro par mois.
#
# Si l'adhésion est fixée à seulement 1.57 euro par mois, l'association
# récoltera exactement les 20 000 euros nécessaires en 2 ans.
# ==============================================================================