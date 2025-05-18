# Pythoni raamistik VN4
**VN4** sisaldab stopperit ja lihtsat terminali menüüd.
Kui oled VN4 peale tõmmanud, võid näidisprogrammi käivitamiseks kirjutada:

```
import VN4
VN4.kaivita_naide()
```
### menuu

####Klassid

**Menuu**

Funktsioonid:

*__init__() - Teeb menüü*

*kaivita() - Kuvab menüü*

*vaikimisi_tuhjendaja() - tühjendab ekraani*

Omandused:

*tiitel - Menüü tiitel vaikimisi "Menuu"*

*valikud - Menüü valikud  vaikimisi []*

*saa_klahv - Klahvisaaja vaikimisi menuu.lihtne_klahvisaaja*

*ules - klahvid, mille vajutamisel läheb valik üles vaikimisi ["w"]*

*alla - alla klahvid vaikimisi ["s"]*

*vali - valimisklahvid vaikimisi [" ", ""]*

*tuhjenda - ekraani tuhjendaja. vaikimisi klassi vaikimisi_tuhjendaja*

*prindi - printija. vaikimisi print*

*self.valik - mitmes valik on valitud vaikimisi 0*

*self.kaib - kas menüü käib*

####Funktsioonid

*tee_valik(tavaline,  funktsioon=None, lisa_kohta=False, valitud=None) - teeb valiku*

*lihtne_klahvisaaja() - lihtne klahvisaaja*

*tiitlikirjutaja(tiitel) - kirjutab tiitli*

### stopper

####Klassid

**Stopper**

Funktsioonid:

*__init__() - teeb ja käivitab stopperi*

*peata() - peata stopper*

*aeg(umarda=True) - tagastab kui kaua on stopper käinud.*

*on_peatunud() - tagastab, kas on peatunud*

*saa_peatumisaeg() - tagastab, kui kaua on stopper peatunud olnud*

*saa_alustusaeg() - saa aeg millal stopper alustati*



# Näide

```
from VN4 import menuu, stopper
from time import sleep
def saa_aeg():
    if not stopper.on_peatunud(): #kui stopper pole peatunud
        print(stopper.aeg()) # ütle stopperi aeg
        sleep(3) # oota kolm sekundit.
    else:
        print("Käivita stopper!") # ütle käivita stopper
        sleep(3) # oota kolm sekundit
stopper = stopper.Stopper() # stopper
stopperi_menuu = menuu.Menuu() # menüü
stopperi_menuu.tiitel = "Stopper" # paneb menüüle tiitliks Stopper
menuu.tee_valik("Stopper pausile", stopper.peata, stopperi_menuu) # Teeb valiku stopper pausile(lihtsam variant)
menuu.tee_valik("Võta stopper pausilt ära", stopper.jatka, stopperi_menuu) # Teeb valiku stopper pausilt ära võtmiseks. (lihtsaim variant)
stopperi_menuu.valikud.append(menuu.tee_valik("Aeg", saa_aeg)) # Lihtsuselt keskmine variant
stopperi_menuu.valikud.append({"tavaline": "Välju", "valitud": "Välju <", "funktsioon": exit}) # Raskeim variant
while True:
    stopperi_menuu.start() # oota alati valikut.
```

