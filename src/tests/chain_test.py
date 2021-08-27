# -*- coding: utf-8 -*-
import unittest
from ..markov_chain import luo_ennustus
from ..trie import Trie


class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.sanalista = ["KAKSONEN", "Olet", "tänään", "iloinen", ".",
        "Tulet", "näkemään", "tänään", "koiran", ".", "koiran", ",",
        "joka", "on", "suloisin", "koira", "ikinä", "."]
        self.trie = Trie(self.sanalista, 2)
    
    def test_ennustuksen_pituus_oikein(self):
        ennustus = luo_ennustus(self.trie.sanakirja, "KAKSONEN ", [], 2, [], 3)
        self.assertEqual(ennustus.count(". "), 3)
