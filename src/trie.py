class TrieNode:
    """luokka trie-solmulle, ei viela valmis tai kaytossa
    """
    def __init__(self, word):
        self.word = word
        self.appeared = 0

class Trie:
    """luokka Trie-puurakenteelle, tallentaa solmun ja sen lapset sanakirjaan
    """
    def __init__(self):
        """rakenteen konstruktori, luo tyhjan sanakirjan
        """
        self.hashmap = {}

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
