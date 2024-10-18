import pandas as pd

reseauArbre = pd.read_csv("../reseau_en_arbre.csv")

reseauArbre_cleaned = reseauArbre.drop_duplicates(subset=["id_batiment", "infra_id", "nb_maisons", "longueur", "infra_type"])

# Réappliquons maintenant la logique de filtrage pour a_remplacer
a_remplacer_cleaned = reseauArbre_cleaned[reseauArbre_cleaned["infra_type"] == "a_remplacer"]

# Regrouper les données par 'infra_id' et calculer le nombre total de maisons pour chaque infrastructure
total_maisons_par_infra = a_remplacer_cleaned.groupby('infra_id')['nb_maisons'].sum().reset_index()

# Fusionner ces informations avec le DataFrame des infrastructures à remplacer
a_remplacer_cleaned_merged = pd.merge(a_remplacer_cleaned, total_maisons_par_infra, on='infra_id', suffixes=('', '_total'))

# Recalculer la longueur par maison en divisant par le nombre total de maisons pour chaque 'infra_id'
a_remplacer_cleaned_merged['difficulte'] = a_remplacer_cleaned_merged['longueur'] / a_remplacer_cleaned_merged['nb_maisons_total']

a_remplacer_cleaned_merged['priorite'] = pd.cut(
    a_remplacer_cleaned_merged['difficulte'], 
    bins=[float(0.195617), float(0.334317), float(1.219881), float(4.928491), float(42.114422)+1],  # Définir les seuils de longueur_par_maison
    labels=[1, 2, 3, 4]  # Attribuer des priorités : 1 (petites valeurs) à 4 (grandes valeurs)
)
# Trier les résultats en fonction de la nouvelle colonne 'longueur_par_maison'
reseau_trie_final = a_remplacer_cleaned_merged.sort_values(by='difficulte', ascending=True)

reseau_trie_final = a_remplacer_cleaned_merged.sort_values(by=['priorite', 'difficulte'], ascending=[True, True])

reseauArbreV2 = reseau_trie_final.drop_duplicates(subset=["infra_id"])


# Regrouper les données par 'id_batiment' et calculer le total des difficultés pour chaque batiment
total_difficulté_par_batiment = reseau_trie_final.groupby('id_batiment')['difficulte'].sum().reset_index()

# Fusionner ces informations avec le DataFrame des infrastructures à remplacer
total_difficulté_par_batiment_merged = pd.merge(reseau_trie_final, total_difficulté_par_batiment, on='id_batiment', suffixes=('', '_total'))

# Afficher le résultat
print(total_difficulté_par_batiment_merged)


# Afficher les 20 premières lignes pour vérifier
# print(reseau_trie_final.head(537))

# print(reseau_trie_final.describe())