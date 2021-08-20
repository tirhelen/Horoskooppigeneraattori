# -*- coding: utf-8 -*-

class Trie:
    """luokka Trie-puurakenteelle, tallentaa solmun ja sen lapset sanakirjaan
    """
    def __init__(self, lista, degree):
        """rakenteen konstruktori, joka muodostaa aineistosta sanakirjan
            käytettävän asteen mukaan

        Args:
            lista (list): lista aineistossa esiintyvistä sanoista
            degree (int): markovin ketjun aste
        """
        self.hashmap = {}
        self.lista = lista
        self.degree = degree
        self.create()

    def add_edge(self, a, b):
        """lisää kaaren kahden solmun
        eli peräkkäin esiintyvien sanojen välille

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
            sanakirjaan lisätään avaimiksi jokainen sana ja merkki sekä aina n (valittu aste)
            peräkkäin esiintyvää sanaa/merkkiä
        """
        help_list = []

        for i in range(self.degree+1):
            help_list.append(self.lista[i])
        for i in range(len(self.lista)-self.degree+1):
            key = ""
            for j in range(len(help_list)-1):
                key += help_list[j] + " "
                self.add_edge(key, help_list[j+1])
            help_list.pop(0)
            if i+self.degree+1 < len(self.lista):
                help_list.append(self.lista[i+self.degree+1])
