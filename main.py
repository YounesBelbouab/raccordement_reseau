import pandas as pd

reseauArbre = pd.read_csv("reseau_en_arbre.csv")

reseauArbre_cleaned = reseauArbre.drop_duplicates(subset=["id_batiment", "infra_id", "nb_maisons", "longueur", "infra_type"])

# Now reapplying the filtering logic for a_remplacer
a_remplacer_cleaned = reseauArbre_cleaned[reseauArbre_cleaned["infra_type"] == "a_remplacer"]

# Calculer la colonne longueur_par_maison
a_remplacer_cleaned["longueur_par_maison"] = a_remplacer_cleaned["longueur"] / a_remplacer_cleaned["nb_maisons"]

# Trier les données par longueur_par_maison en ordre croissant
reseau_trie_cleaned = a_remplacer_cleaned.sort_values(by="longueur_par_maison", ascending=True)

# Afficher les 20 premières lignes pour vérifier
print(reseau_trie_cleaned.head(20))
