# -*- coding: utf-8 -*-
import os
from file_reader import read_file
from trie import Trie
from markov_chain import create_sentence


class UI:
    def __init__(self):
        """ käyttöliittymän konstruktori, joka muodostaa trien aineistosta
        """
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.split(current_dir)[0]
        file = os.path.join(parent_dir, "aineisto.txt")
        self.word_list = read_file(file)

    def commands(self):
        """kysyy käyttäjältä horoskoopin ja ennustuksen pituuden
            (vielä käyttäjän syötettä ei tarkisteta)

        Returns:
            prediction (sting): lopullinen ennustus siistityssä muodossa
        """
        horoscope = input("Kirjoita CAPSILLA horoskooppimerkki, jolle haluat ennustuksen: ")
        horoscope += " "
        amount = int(input("Kuinka monta virkettä haluat?: "))
        degree = int(input("Valitse Markovin ketjun aste: "))
        self.trie = Trie(self.word_list, degree)
        text_list = create_sentence(self.trie.hashmap, horoscope, [horoscope], degree, [], amount)
        prediction = self.output(text_list)
        return prediction

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


if __name__ == "__main__":
    ui = UI()
    print(ui.commands())
