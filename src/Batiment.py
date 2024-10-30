import pandas as pd

class Batiment:
    
    def __init__(self, id_bat, liste_infra):
        self.id_bat = id_bat
        self.liste_infra = liste_infra

    def get_batiment_difficulty(self):
        difficulty = 0
        for infra in self.liste_infra:
            difficulty += infra.get_difficulties()
        return difficulty
    
    def repair_batiment(self):
        for infra in self.liste_infra:
            infra.repair_infra()
    