

pocet_znamek = 0
soucet = 0

while True:
    aktualni_znamka = int(input("Napis jednu ze znamek: "))
    if (aktualni_znamka == 0):
        break
    vaha = int(input("Napis vahu dane znamky: "))
    
    soucet += (aktualni_znamka*vaha)
    pocet_znamek += vaha

print(soucet/pocet_znamek)
