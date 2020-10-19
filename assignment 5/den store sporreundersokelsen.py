from sys import exit

antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_ITGK = 0
antall_timer_lekser = 0

def sjekk_svar(spm):
    if spm.lower() == "hade":
        skriv_statistikk()
        exit()

def les_streng(spm):
    if spm.lower() == "f":
        GLOBAL antall_kvinner
        antall_kvinner += 1
    elif spm.lower() == "m":
        GLOBAL antall_menn
        antall_menn += 1

def les_ja_nei(spm):
    if spm == medlem_ITGK and spm == "ja":
        GLOBAL antall_ITGK
        antall_ITGK+=1
    elif spm == fag and spm == "ja":
        GLOBAL antall_fag
        antall_fag+=1

def les_tall(spm):
    GLOBAL antall_timer_lekser
    antall_timer_lekser +=1


def skriv_statistikk():
    print("Resultat av undersøkelse!")
    print("Antall kvinner:", antall_kvinner)
    print("Antall menn:", antall_menn)
    print("Antall personer som tar fag:", antall_fag)
    print("Antall personer som tar ITGK:", antall_ITGK)
    print("Antall timer i snitt brukt på lekser:", antall_timer_lekser)




def sporreundersokelse():
    while True:
        print("Velkommen til spørreundersøkelsen!")
        print("")

        while kjonn.lower() != "f" or kjonn.lower() != "m":
            kjonn = input("Hvilket kjønn er du? [f/m]: ")
            sjekk_svar(kjonn)
            les_streng(kjonn)

        while not ininstance(alder, str):
            alder = int(input("Hvor gammel er du? "))
            sjekk_svar(alder)
        if alder < 16 or alder > 25:
            print("Du kan dessverre ikke ta denne undersøkelsen")
            print("")
            sporreundersokelse()

        while fag.lower() != "ja" or fag.lower() != "nei":
            fag = input("Tar du et eller flere fag? [ja/nei ]: ")
            sjekk_svar(fag)
            if fag.lower() == "nei":
                sporreundersokelse()
            les_ja_nei(fag)
            if alder >= 22:
                medlem_ITGK = input = ("Tar du virkelig ITGK? [ja/nei]: ")
            else:
                medlem_ITGK = input = ("Tar du ITGK? [ja/nei]: ")
            sjekk_svar(medlem_ITGK)
            les_ja_nei(medlem_ITGK)

        timer_lekser = float(input("Hvor mange timer bruker du daglig (i snitt) på lekser?:" ))
        sjekk_svar(timer_lekser)
        les_tall(timer_lekser)

sporreundersokelse()


