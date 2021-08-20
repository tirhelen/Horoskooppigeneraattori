# -*- coding: utf-8 -*-
import unittest
from ..markov_chain import create_sentence
from ..trie import Trie


class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.list = ["KAKSONEN", "Olet", "tänään", "iloinen", ".",
        "Tulet", "näkemään", "tänään", "koiran", ".", "koiran", ",",
        "joka", "on", "suloisin", "koira", "ikinä", "."]
        self.trie = Trie(self.list, 2)
    
    def test_right_lenght(self):
        sentence = create_sentence(self.trie.hashmap, "KAKSONEN ", [], 2, [], 3)
        self.assertEqual(sentence.count(". "), 3)
