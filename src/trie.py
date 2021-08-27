# -*- coding: utf-8 -*-

class Trie:
    """luokka Trie-puurakenteelle, tallentaa solmun ja sen lapset sanakirjaan
    """
    def __init__(self, sanalista, aste):
        """rakenteen konstruktori, joka muodostaa aineistosta sanakirjan
            käytettävän asteen mukaan

        Args:
            sanalista (list): sanalista aineistossa esiintyvistä sanoista
            aste (int): markovin ketjun aste
        """
        self.sanakirja = {}
        self.sanalista = sanalista
        self.aste = aste
        self.luo_trie()

    def lisaa_kaari(self, a, b):
        """lisää kaaren kahden solmun
        eli peräkkäin esiintyvien sanojen välille

        Args:
            a (string): jokin tekstissa esiintyva sana
            b (string): a:ta seuraava sana
        """
        if a not in self.sanakirja:
            self.sanakirja[a] = {b:1}
        else:
            if b not in self.sanakirja[a]:
                self.sanakirja[a][b] = 1
            else:
                self.sanakirja[a][b] += 1


    def luo_trie(self):
        """funktio, joka täyttää sanakirjan aineistosta muodostetun sanalistan perusteella.
            sanakirjaan lisätään avaimiksi jokainen sana ja merkki sekä aina n (valittu aste)
            peräkkäin esiintyvää sanaa/merkkiä
        """
        apulista = []

        for i in range(self.aste+1):
            apulista.append(self.sanalista[i])
        for i in range(len(self.sanalista)-self.aste+1):
            avain = ""
            for j in range(len(apulista)-1):
                avain += apulista[j] + " "
                self.lisaa_kaari(avain, apulista[j+1])
            apulista.pop(0)
            if i+self.aste+1 < len(self.sanalista):
                apulista.append(self.sanalista[i+self.aste+1])
