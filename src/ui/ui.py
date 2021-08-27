# -*- coding: utf-8 -*-
import os
from file_reader import lue_tiedosto
from trie import Trie
from markov_chain import luo_ennustus


class UI:
    def __init__(self):
        """ käyttöliittymän konstruktori, joka valmistelee aineiston listaksi
        """

        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.split(current_dir)[0]
        parent_dir = os.path.split(parent_dir)[0]
        file = os.path.join(parent_dir, "aineisto.txt")
        self.sanalista = lue_tiedosto(file)


    def komennot(self):
        """kysyy käyttäjältä horoskoopin, ennustuksen ja käytettävän ketjun pituuden,
            luo trien ja ennustuksen käyttäjän syötteen mukaan
        Returns:
            prediction (string): lopullinen ennustus siistityssä muodossa
        """
        käynnissä = True
        print("Tervetuloa käyttämään horoskooppigeneraattoria!")
        self.luo_ennustus_k()
        while käynnissä:

            print(" ")
            print("Komennot:")
            print("1 Luo uusi ennustus samoilla asetuksilla")
            print("2 Luo uusi ennustus uusilla asetuksilla")
            print("3 Sulje sovellus")
            komento = int(input())
            print(" ")
            if komento == 3:
                käynnissä = False
            elif komento == 2:
                self.luo_ennustus_k()
            elif komento == 1:
                ennustus = luo_ennustus(self.trie.sanakirja, self.horoskooppi,
                [self.horoskooppi], self.aste, [], self.pituus)
                print(ennustus)


    def luo_ennustus_k(self):
        while True:
            horoskooppi = input("Kirjoita horoskooppimerkki, jolle haluat ennustuksen: ")
            self.horoskooppi = horoskooppi.upper()

            if self.horoskooppi_syotetty_oikein(self.horoskooppi):
                self.horoskooppi += " "
                break
            print(f"{self.horoskooppi} ei ole horoskooppi tai kirjoitit sen väärin")

        while True:
            try:
                self.pituus = int(input("Kuinka monta virkettä haluat?: "))
                break
            except ValueError:
                print("! Kirjoita määrä numeroina !")

        while True:
            try:
                self.aste = int(input("Valitse Markovin ketjun aste: "))
                break
            except ValueError:
                print("! Kirjoita määrä numeroina !")

        self.trie = Trie(self.sanalista, self.aste)
        ennustus = luo_ennustus(self.trie.sanakirja, self.horoskooppi,
        [self.horoskooppi], self.aste, [], self.pituus)
        print(" ")
        print(ennustus)


    def horoskooppi_syotetty_oikein(self, horoskooppi):
        if horoskooppi not in ["JOUSIMIES", "KAKSONEN", "RAPU", "LEIJONA",
                            "VESIMIES", "NEITSYT", "SKORPIONI", "HÄRKÄ",
                            "OINAS", "VAAKA", "KAURIS", "KALAT"]:
            return False
        return True

