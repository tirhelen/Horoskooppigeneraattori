# -*- coding: utf-8 -*-
import os
from file_reader import read_file
from markov_chain import create_sentence

class Trie:
    """luokka Trie-puurakenteelle, tallentaa solmun ja sen lapset sanakirjaan
    """
    def __init__(self, lista, degree):
        """rakenteen konstruktori, luo sanakirjan, joka täytetään create-funktion avulla
        """
        self.hashmap = {}
        self.lista = lista
        self.degree = degree
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
        help_list = []
        last = self.lista[-1]

        for i in range(self.degree+2):
            help_list.append(self.lista[i])

        for i in range(len(self.lista)-self.degree-1):
            key = ""
            for j in range(len(help_list)-2):
                key += help_list[j] + " "
            self.add_edge(key, help_list[-1])
            help_list.pop(0)
            help_list.append(self.lista[i+self.degree+1])
        return

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.split(current_dir)[0]
    file = os.path.join(parent_dir, "aineisto.txt")
    word_list = read_file(file)

    trie = Trie(word_list, 3)
    print(trie.hashmap)
    #text = []
    #first = create_sentence(trie.hashmap, ". KAKSONEN Tee ", [". KAKSONEN Tee "])
    #print(first)