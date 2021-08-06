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
        word_list = read_file(file)

        self.trie = Trie(word_list)

    def commands(self):
        """kysyy käyttäjältä horoskoopin ja ennustuksen pituuden
            (vielä käyttäjän syötettä ei tarkisteta)

        Returns:
            prediction (sting): lopullinen ennustus siistityssä muodossa
        """
        horoscope = input("Kirjoita CAPSILLA horoskooppimerkki, jolle haluat ennustuksen: ")
        amount = int(input("Kuinka monta virkettä haluat? (1-10):" ))
        text = []
        first = create_sentence(self.trie.hashmap, horoscope, [horoscope])
        text.append(first)
        for i in range(amount-1):
            sentence = create_sentence(self.trie.hashmap, ".", ["."])
            text.append(sentence)
        prediction = self.output(text)
        return prediction

    def output(self, text):
        """siistii ennustetekstin helposti luettavaan muotoon

        Args:
            text (list): lista listoista, jotka sisältävät kunkin muodostetun virkkeen sanat

        Returns:
            string: siistitty ennusteteksti joka voidaan tulostaa käyttäjälle
        """
        string = ""
        for list in text:
            for i in range(len(list)-1):
                if list[i] == "." and list[i+1] != "." or list[i] == "," or i == 0:
                    string += list[i]
                else:
                    string += " " + list[i]
        return string


if __name__ == "__main__":
    ui = UI()
    print(ui.commands())
