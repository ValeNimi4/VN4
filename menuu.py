import os
class Menuu:
    def vaikimisi_tuhjendaja(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    def __init__(self):
        self.tiitel = "Menuu"
        self.valikud = []
        self.saa_klahv = lihtne_klahvisaaja
        self.kirjuta_tiitel = tiitlikirjutaja
        self.ules = ["w"]
        self.alla = ["s"]
        self.vali = [" ", ""]
        self.tuhjenda = self.vaikimisi_tuhjendaja
        self.prindi = print
        self.valik = 0
    def start(self):
        self.kaib = True
        while self.kaib:
            self.tuhjenda()
            self.kirjuta_tiitel(self.tiitel)
            for i in range(len(self.valikud)):
                if self.valik == i:
                    self.prindi(self.valikud[i]["valitud"])
                else:
                    self.prindi(self.valikud[i]["tavaline"])
            klahv = self.saa_klahv()
            if klahv in self.ules and self.valik > 0:
                self.valik -= 1
            elif klahv in self.vali:
                if self.valikud[self.valik]["funktsioon"]:
                    self.valikud[self.valik]["funktsioon"]()
                    self.kaib = False
            elif klahv in self.alla and self.valik < len(self.valikud) - 1:
                self.valik += 1
def tee_valik(tavaline,  funktsioon=None, lisa_kohta=False, valitud=None):
    if not valitud:
        valitud = tavaline + " <"
    valik = {"tavaline": tavaline, "valitud": valitud, "funktsioon": funktsioon}
    if lisa_kohta:
        lisa_kohta.valikud.append(valik)
    else:
        return valik
def lihtne_klahvisaaja():
    sisend = input()
    if sisend != "":
        return sisend[0]
    else:
        return ""
def tiitlikirjutaja(tiitel):
    tiitel += "\n"
    for i in range(len(tiitel) - 1):
        tiitel += "-"
    print(tiitel)