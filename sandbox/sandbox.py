import pandas as pd

reseauArbre = pd.read_csv("reseau_en_arbre.csv")

a_remplacer = reseauArbre[reseauArbre["infra_type"] == "a_remplacer"]
intact = reseauArbre[reseauArbre["infra_type"] == "infra_intacte"]

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

a_remplacer.drop_duplicates(['id_batiment', "id_batiment",  "nb_maisons", "infra_id",   "infra_type",  "longueur"], inplace=True)
print(a_remplacer.groupby("infra_id").sum().value_counts().head(588))

nouveau_reseau_arbre = pd.merge(left=reseauArbre, right=a_remplacer, on="infra_id", suffixes=('', '_y'))
colonnes_a_garder = [col for col in nouveau_reseau_arbre.columns if not col.endswith('_y')]

reseau_arbre_final = nouveau_reseau_arbre[colonnes_a_garder]
reseau_arbre_final["longueur_par_maison"] = reseau_arbre_final["longueur"]/reseau_arbre_final["nb_maisons"]

reseau_trie = reseau_arbre_final.sort_values(by="longueur_par_maison", ascending=True)
print(reseau_trie.describe())
