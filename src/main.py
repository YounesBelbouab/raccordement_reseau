from Batiment import Batiment
from Infrastructure import Infra
import pandas as pd

df = pd.read_csv("final_infra.csv")
#print(df.head())

dict_infra = {}

for i in range(0,len(df)):
    dict_infra[df["infra_id"][i]] = Infra(df["infra_id"][i], df["longueur"][i], df["infra_type"][i], df["nb_maisons_total"][i])

liste_batiment = []
batiment_fini = []
infra_fini = []


for i, y in df.groupby(by="id_batiment"):
    liste_infra = [dict_infra[infra_id] for infra_id in y["infra_id"].values]
    liste_batiment.append(Batiment(i, liste_infra))

liste_batiment.sort(key=lambda bat: bat.get_batiment_difficulty())


while liste_batiment:
    liste_batiment.sort(key=lambda bat: bat.get_batiment_difficulty())
    batiment = liste_batiment.pop(0)
    
    for infra in batiment.liste_infra:
        infra.repair_infra()
        infra_fini.append(infra)
    
    batiment_fini.append(batiment)


