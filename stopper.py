# Tegi ValeNimi4
# Info: ValeNimi4.github.io/pythonAPI
class Stopper:
    def __init__(self) -> None:
        self.ALUSTUSAEG = time.time() # Aeg, millal programm käima pandi
        self.ENNEPEATAMIST = self.ALUSTUSAEG # Aeg, millal oli programm enne peatamist
        self.PEATUNUD = 0 # Aeg, kui kaua on stopper olnud peatatu
        self.PEATATUD = False # Kas stopper on peatunud
    def peata(self) -> None:
        self.PEATATUD = True # Stopper on peatunud
        self.ENNEPEATAMIST = time.time() #Aeg, millal oli programm enne peatamist
    def aeg(self, umarda=True) -> int:
        #import time
        if self.PEATATUD == False:
            AEG = time.time() - self.ALUSTUSAEG - self.PEATUNUD # Arvutamine et teaa saada aega, mida stopper näitab
            if umarda: # Kui umarda on tõene
                AEG = round(AEG, 2) # Ümarda (jääb alles kaks kohta pärast koma
            return AEG # Väljastab aja
        else:
            raise RuntimeError("Ei saa aega arvutada, kui stopper on peatatud.") # Annab errori
    def jatka(self) -> None:
        self.PEATATUD = False # Ei ole enam peatatud
        self.PEATUNUD += time.time() - self.ENNEPEATAMIST # Lisab "PEATUNUD" muutujale aja, kui kaua oli stopper peatatud
    def on_peatunud(self) -> bool:
        return self.PEATATUD
    def saa_peatumisaeg(self) -> float:
        return self.PEATUNUD
    def saa_alustusaeg(self) -> float:
        return self.ALUSTUSAEG
import time