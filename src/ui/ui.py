# -*- coding: utf-8 -*-
import os
from file_reader import read_file
from trie import Trie
from markov_chain import create_sentence


class UI:
    def __init__(self):
        """ käyttöliittymän konstruktori, joka valmistelee aineiston listaksi
        """

        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.split(current_dir)[0]
        parent_dir = os.path.split(parent_dir)[0]
        file = os.path.join(parent_dir, "aineisto.txt")
        self.word_list = read_file(file)


    def commands(self):
        """kysyy käyttäjältä horoskoopin, ennustuksen ja käytettävän ketjun pituuden,
            luo trien ja ennustuksen käyttäjän syötteen mukaan
            (vielä käyttäjän syötettä ei tarkisteta)
        Returns:
            prediction (string): lopullinen ennustus siistityssä muodossa
        """
        play = True
        print("Tervetuloa käyttämään horoskooppigeneraattoria!")
        self.create_prediction()
        while play:

            print(" ")
            print("Komennot:")
            print("1 Luo uusi ennustus samoilla asetuksilla")
            print("2 Luo uusi ennustus uusilla asetuksilla")
            print("3 Sulje sovellus")
            command = int(input())
            print(" ")
            if command == 3:
                play = False
            elif command == 2:
                self.create_prediction()
            elif command == 1:
                text_list = create_sentence(self.trie.hashmap, self.horoscope, [self.horoscope], self.degree, [], self.amount)
                prediction = self.output(text_list)
                print(prediction)


    def create_prediction(self):
        while True:
            horoscope = input("Kirjoita horoskooppimerkki, jolle haluat ennustuksen: ")
            self.horoscope = horoscope.upper()

            if self.is_valid_horoscope(self.horoscope):
                self.horoscope += " "
                break
            print(f"{self.horoscope} ei ole horoskooppi tai kirjoitit sen väärin")

        while True:
            try:
                self.amount = int(input("Kuinka monta virkettä haluat?: "))
                break
            except ValueError:
                print("! Kirjoita määrä numeroina !")

        while True:
            try:
                self.degree = int(input("Valitse Markovin ketjun aste: "))
                break
            except ValueError:
                print("! Kirjoita määrä numeroina !")

        self.trie = Trie(self.word_list, self.degree)
        text_list = create_sentence(self.trie.hashmap, self.horoscope, [self.horoscope], self.degree, [], self.amount)
        prediction = self.output(text_list)
        print(" ")
        print(prediction)


    def is_valid_horoscope(self, horoscope):
        if horoscope not in ["JOUSIMIES", "KAKSONEN", "RAPU", "LEIJONA",
                            "VESIMIES", "NEITSYT", "SKORPIONI", "HÄRKÄ",
                            "OINAS", "VAAKA", "KAURIS", "KALAT"]:
            return False
        return True


    def output(self, text):
        """siistii ennustetekstin helposti luettavaan muotoon
        Args:
            text (list): lista, joka sisältää ennustukseen kuuluvat sanat
        Returns:
            string: siistitty ennusteteksti joka voidaan tulostaa käyttäjälle
        """

        for i in range(len(text)-1):
            if text[i+1] == ". " or text[i+1] == ", ":
                text[i] = text[i][:-1]
        string = ''.join(map(str, text))
        return string

