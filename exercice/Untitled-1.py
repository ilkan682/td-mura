print("calcul d'un pret immobilier")
s = float(input("entrer le montant du pret ou credit: "))
t = float(input("entrer le taux annuel en %: "))
n = int(input("entrer le nombre d'années: "))

tm = t / 12 / 100
# Correction de l'exposant : 12 * n (et non 12**n)
a = (1 + tm) ** (12 * n)
m = s * tm * a / (a - 1)

# Calcul du total des intérêts sur toute la durée du prêt
total_interets = (m * n * 12) - s

print("\n--- Résumé du prêt ---")
print("La mensualité avec intérêt est de :", round(m, 2), "euros")
print("Le montant total des intérêts remboursés sera de :", round(total_interets, 2), "euros")
print("Le taux mensuel est de :", round(tm, 5))

print("\nTableau d'amortissement :")
print("Mois | Mensualité | Intérêts | Capital Remboursé | Capital Restant Dû | Intérêts Cumulés")
print("-" * 90)

ir = 0.0
for j in range(n * 12):
    i = tm * s          # Intérêts du mois
    cr = m - i          # Capital remboursé ce mois-ci
    crd = s - cr        # Capital restant dû après ce mois
    ir = ir + i         # Cumul des intérêts remboursés
    
    # Affichage de la ligne du mois
    print(f" {j+1:<3} | {round(m, 2):<10} | {round(i, 2):<8} | {round(cr, 2):<17} | {round(max(0, crd), 2):<19} | {round(ir, 2)}")
    
    # CRUCIAL : On met à jour le capital restant dû pour le mois suivant
    s = crd