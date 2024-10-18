import pandas as pd

df = pd.read_csv("reseau_en_arbre.csv")

df_cleaned = df.drop_duplicates(subset=["id_batiment", "infra_id", "nb_maisons", "longueur", "infra_type"])

# Réappliquons maintenant la logique de filtrage pour a_remplacer
df_a_remplacer = df_cleaned[df_cleaned["infra_type"] == "a_remplacer"]

# Regrouper les données par 'infra_id' et calculer le nombre total de maisons pour chaque infrastructure
total_maisons_par_infra = df_a_remplacer.groupby('infra_id')['nb_maisons'].sum().reset_index()

# Fusionner ces informations avec le DataFrame des infrastructures à remplacer
a_remplacer_cleaned_merged = pd.merge(df_a_remplacer, total_maisons_par_infra, on='infra_id', suffixes=('', '_total'))

# Recalculer la longueur par maison en divisant par le nombre total de maisons pour chaque 'infra_id'
a_remplacer_cleaned_merged['difficulté'] = a_remplacer_cleaned_merged['longueur'] / a_remplacer_cleaned_merged['nb_maisons_total']

# a_remplacer_cleaned_merged['priorite'] = pd.cut(
#     a_remplacer_cleaned_merged['longueur_par_maison'], 
#     bins=[float(0.195617), float(0.334317), float(1.219881), float(4.928491), float(42.114422)+1],  # Définir les seuils de longueur_par_maison
#     labels=[1, 2, 3, 4]  # Attribuer des priorités : 1 (petites valeurs) à 4 (grandes valeurs)
# )

# Trier les résultats en fonction de la nouvelle colonne 'longueur_par_maison'
reseau_trie = a_remplacer_cleaned_merged.sort_values(by='difficulté', ascending=True)

reseau_trie_final = reseau_trie.drop_duplicates(subset=[ "infra_id"])
#Afficher les 50 premières lignes pour vérifier
# print(reseau_trie_final.head(150))

# Regrouper les données par 'id_batiment' et calculer le total des difficultés pour chaque batiment

total_difficulté_par_batiment = reseau_trie_final.groupby('id_batiment')['difficulté'].sum().reset_index()

# Fusionner ces informations avec le DataFrame des infrastructures à remplacer
total_difficulté_par_batiment_merged = pd.merge(reseau_trie_final, total_difficulté_par_batiment, on='id_batiment', suffixes=('', '_total'))


print(total_difficulté_par_batiment_merged.head(150))
