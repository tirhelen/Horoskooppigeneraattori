# -*- coding: utf-8 -*-
class Trie:
    """luokka Trie-puurakenteelle, tallentaa solmun ja sen lapset sanakirjaan
    """
    def __init__(self, lista):
        """rakenteen konstruktori, luo sanakirjan, joka täytetään create-funktion avulla
        """
        self.hashmap = {}
        self.lista = lista
        self.create()

    def add_edge(self, a, b):
        """lisaa kaaren kahden solmun
        eli perakkain esiintyvien sanojen valille

        Args:
            a (string): jokin tekstissa esiintyva sana
            b (string): a:ta seuraava sana
        """
        if a not in self.hashmap:
            self.hashmap[a] = [[b, 1]]
        else:
            found = False
            for x in self.hashmap[a]:
                if x[0] == b:
                    x[1] += 1
                    found = True
                    break
            if found is False:
                self.hashmap[a].append([b,1])


    def create(self):
        """funktio, joka täyttää sanakirjan aineistosta muodostetun listan perusteella.
            sanakirjaan lisätään avaimiksi jokainen sana ja merkki sekä aina kaksi
            peräkkäin esiintyvää sanaa/merkkiä
        """
        for i in range(len(self.lista)-1):
            self.add_edge(self.lista[i], self.lista[i+1])

        for i in range(len(self.lista)-1):
            if self.lista[i+1] != ".":
                a = self.lista[i] + " " + self.lista[i+1]
                self.add_edge(a, self.lista[i+2])

            elif self.lista[i] == "." or self.lista[i] in ["JOUSIMIES", "KAKSONEN", "RAPU",
                                                "LEIJONA", "VESIMIES", "NEITSYT", "SKORPIONI",
                                                "HÄRKÄ", "OINAS", "VAAKA", "KAURIS", "KALAT"]:
                self.add_edge(self.lista[i], self.lista[i+1])
        