# -*- coding: utf-8 -*-
import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.list = ["Tässä", "on", "todella", "tärkeää", "tekstiä", ".",
        "tärkeää", "tekstiä", ",", "jota", "ei", "saa",
        "hukata", ".", "ei", "milloinkaan", "."]
        self.trie = Trie(self.list)

    def test_correct_key_values(self):
        # Huom! Tämä testi ei ole vielä päivitetty vastaamaan trien nykyistä toimintaa
        help_list = []
        for i in range(len(self.list)-1):
            if self.list[i] not in help_list:
                help_list.append(self.list[i])
            if self.list[i] + " " + self.list[i+1] not in help_list and self.list[i+1] != ".":
                help_list.append(self.list[i] + " " + self.list[i+1])
        keys = sorted(self.trie.hashmap.keys())
        help_list = sorted(help_list)
        self.assertEqual(keys, help_list)
    
