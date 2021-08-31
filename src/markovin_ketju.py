# -*- coding: utf-8 -*-
import random


def luo_ennustus(sanakirja, alku, ennustus, aste, apulista, pituus):
    """luo ennustuksen käyttäen syötteenä annettavaa pituutta ja ketjun astetta

    Args:
        sanakirja (sanakirja): käytettävä trie, johon aineisto on tallennettu
        alku (string): virkkeen aloitussana tai myöhemmin seuraava valittu sana
        ennustus (list): lista, johon muodostettava lause kootaan
        aste (int): käytettävä markovin ketjun aste
        apulista (list): apulista, jota käytetään uuden avaimen valitsemiseksi
        lenght (int): ennustuksen pituus virkkeinä

    Returns:
        ennustus (list): ennustus listana
    """

    if ennustus.count(". ") == pituus:
        return ennustus

    valittavat = []
    for x in sanakirja[alku]:
        for j in range(sanakirja[alku][x]):
            if x not in ["JOUSIMIES", "KAKSONEN", "RAPU", "LEIJONA",
                            "VESIMIES", "NEITSYT", "SKORPIONI", "HÄRKÄ",
                            "OINAS", "VAAKA", "KAURIS", "KALAT"]:
                valittavat.append(x)
            else:
                valittavat.append(".")

    seuraava = random.choice(valittavat) + " "

    if seuraava == ". " and alku[-2] == ".":
        return luo_ennustus(sanakirja, ". ", ennustus, aste, [], pituus)

    ennustus.append(seuraava)
    apulista.append(seuraava)

    if len(apulista) == aste+1:
        apulista.pop(0)

    seuraava = ''.join(map(str, apulista))

    return luo_ennustus(sanakirja, seuraava, ennustus, aste, apulista, pituus)
