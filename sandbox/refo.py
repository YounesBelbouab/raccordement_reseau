import pandas as pd

reseauArbre = pd.read_csv("reseau_en_arbre.csv")

df_unique = reseauArbre.drop_duplicates(["id_batiment",  "nb_maisons", "infra_id",   "infra_type",  "longueur"])
a_remplacer = df_unique[df_unique["infra_type"] == "a_remplacer"]

reseau_arbre_nettoyer = a_remplacer.groupby("infra_id").sum(numeric_only=True)

reseau_arbre_nettoyer["longueur_par_maison"] = reseau_arbre_nettoyer["longueur"]/reseau_arbre_nettoyer["nb_maisons"]
dataframe_sorted = reseau_arbre_nettoyer.sort_values(by="longueur_par_maison", ascending=True)

jour_un = []
jour_deux = []
jour_trois = []
jour_quatre = []

for i in range(0, len(dataframe_sorted)):
    if 0 < dataframe_sorted["longueur_par_maison"][i] <6:
        jour_un.append(dataframe_sorted["longueur_par_maison"][i])
    elif 6 < dataframe_sorted["longueur_par_maison"][i] < 9:
        jour_deux.append(dataframe_sorted["longueur_par_maison"][i])
    elif 9 < dataframe_sorted["longueur_par_maison"][i] < 11:
        jour_trois.append(dataframe_sorted["longueur_par_maison"][i])
    elif 11 < dataframe_sorted["longueur_par_maison"][i]:
        jour_quatre.append(dataframe_sorted["longueur_par_maison"][i])

print(len(jour_un))
print(len(jour_deux))
print(len(jour_trois))
print(len(jour_quatre))
