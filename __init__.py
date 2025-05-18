from . import stopper, menuu
versioon = 1
def kaivita_naide():
    def saa_aeg():
        if not stopper.on_peatunud():
            print(stopper.aeg())
            sleep(3)
        else:
            print("Käivita stopper!")
            sleep(3)
    stopper = stopper.Stopper()
    stopperi_menuu = menuu.Menuu()
    stopperi_menuu.tiitel = "Stopper"
    menuu.tee_valik("Stopper pausile", stopper.peata, stopperi_menuu)
    menuu.tee_valik("Võta stopper pausilt ära", stopper.jatka, stopperi_menuu)
    stopperi_menuu.valikud.append(menuu.tee_valik("Aeg", saa_aeg))
    stopperi_menuu.valikud.append({"tavaline": "Välju", "valitud": "Välju <", "funktsioon": exit})
    while True:
        stopperi_menuu.start()