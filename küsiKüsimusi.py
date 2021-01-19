import random

küsimused = ['Kuidas sul läheb?', 'Mis päev täna on?', 'Mis teed?']

#Meil oleks vaja luua funktsioon, mis valib sellest listist suvalise küsimuse ja prindib selle

def valiSuvalineKüsimus():
    listiPikkus = len(küsimused) - 1
    suvalineIndeks = random.randint(0, listiPikkus)
    suvalineKüsimus = küsimused[suvalineIndeks]

    return suvalineKüsimus

print(valiSuvalineKüsimus())