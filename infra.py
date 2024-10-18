import pandas

df = pandas.read_csv('reseau_en_arbre.csv', sep=",")

df.drop_duplicates(["id_batiment",  "nb_maisons", "infra_id",   "infra_type",  "longueur"], inplace=True)

df = df[df["infra_type"] == "a_remplacer"]
df = df[['infra_id', "infra_type", "longueur"]]
# df.to_csv("infra_state.csv")


reseau_arbre = pandas.read_csv("reseau_en_arbre.csv")


df_unique = reseau_arbre.drop_duplicates(["id_batiment",  "nb_maisons", "infra_id",   "infra_type",  "longueur"])
a_remplacer = df_unique[df_unique["infra_type"] == "a_remplacer"]

reseau_arbre_nettoyer = a_remplacer.groupby("infra_id").sum(numeric_only=True)[["nb_maisons"]]

df = df.join(reseau_arbre_nettoyer, on="infra_id")
df["metrique_difficulte"] = df["longueur"] / df["nb_maisons"] 
print(len(df))
df.drop_duplicates(["infra_id"], inplace=True)
print(len(df))

df.to_excel("infra_state.xlsx", index=False)
