# -*- coding: utf-8 -*-
import unittest
from ..trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.sanalista = ["Tässä", "on", "todella", "tärkeää", "tekstiä", ".",
        "tärkeää", "tekstiä", ",", "jota", "ei", "saa",
        "hukata", ".", "ei", "milloinkaan", "."]
        self.trie = Trie(self.sanalista, 2)
    
    def test_kaaren_lisays_2_aste(self):
        self.trie.lisaa_kaari("kissa ja", "koira")
        self.assertEqual(self.trie.sanakirja["kissa ja"], {"koira":1})
    
    def test_oikeat_avaimet_2_aste(self):
        apulista = []
        for i in range(len(self.sanalista)-1):
            if self.sanalista[i]+" " not in apulista:
                apulista.append(self.sanalista[i] + " ")
            if i+1 < len(self.sanalista)-1:
                if self.sanalista[i] + " " + self.sanalista[i+1] + " " not in apulista:
                    apulista.append(self.sanalista[i] + " " + self.sanalista[i+1] + " ")
        avaimet = sorted(self.trie.sanakirja.keys())
        apulista = sorted(apulista)
        self.assertEqual(avaimet, apulista)
    
    def test_oikeat_arvot_sanakirjassa_2_aste(self):
        self.sanalista = ["Tässä", "on", "todella", "tärkeää", "tekstiä", ".",]
        self.trie = Trie(self.sanalista, 2)
        arvot = list(self.trie.sanakirja.values())
        apulista = [{'on': 1}, {'todella': 1}, {'todella': 1}, {'tärkeää': 1},
        {'tärkeää': 1}, {'tekstiä': 1}, {'tekstiä': 1}, {'.': 1}, {'.': 1}]
        self.assertEqual(arvot, apulista)

    def test_kolmas_aste_avaimet(self):
        self.trie = Trie(["kissat", "on", "tosi", "suloisia"], 3)
        apulista = ["kissat ", "kissat on ", "kissat on tosi ", "on ", "on tosi "]
        self.assertEqual(list(self.trie.sanakirja.keys()), apulista)
