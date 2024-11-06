from Batiment import Batiment
from Infrastructure import Infra
import pandas as pd

df = pd.read_csv("reseau_en_arbre.csv")
df = df[df["infra_type"] == "a_remplacer"].drop_duplicates()

dict_infra = {}

for i, y in df.groupby(by="infra_id"):
    longueur = y["longueur"].iloc[0]
    infra_type = y["infra_type"].iloc[0]
    nbr_maisons = y["nb_maisons"].sum()
    dict_infra[i] = Infra(i, longueur,infra_type, nbr_maisons)

liste_batiment = []
batiment_fini = []
infra_fini = []

for batiment_id in df["id_batiment"].unique():
    infra_id_df = df[df["id_batiment"] == batiment_id]["infra_id"]
    liste_infra = [dict_infra[infra_id] for infra_id in infra_id_df if infra_id in dict_infra]
    batiment = Batiment(batiment_id, liste_infra)
    liste_batiment.append(batiment)


liste_batiment.sort(key=lambda batiment: batiment.get_batiment_difficulty())


while liste_batiment:
    liste_batiment.sort(key=lambda batiment: batiment.get_batiment_difficulty())
    batiment = liste_batiment.pop(0)
    
    for infra in batiment.liste_infra:
        infra.repair_infra()
        infra_fini.append(infra)
    
    batiment_fini.append(batiment)


print(liste_batiment)
print([batiment.id_bat for batiment in batiment_fini])

