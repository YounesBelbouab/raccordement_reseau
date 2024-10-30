import pandas as pd

class Infra:
    def __init__(self, infra_id, longueur,  type, nb_maison):
        self.infra_id = infra_id
        self.longueur = longueur
        self.type = type
        self.nb_maison = nb_maison

    def get_difficulties(self):
        if self.type == "intact":
            return 0
        else:
            return self.longueur/self.nb_maison
    
    def repair_infra(self):
        self.type = "intact"

        