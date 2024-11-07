from src.Batiment import Batiment
from src.Infrastructure import Infra
import pandas as pd

df = pd.read_csv("final_infra.csv")

dict_infra = {}

for i in range(0,len(df)):
    dict_infra[df["infra_id"][i]] = Infra(df["infra_id"][i], df["longueur"][i], df["infra_type"][i], df["nb_maisons"][i])

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