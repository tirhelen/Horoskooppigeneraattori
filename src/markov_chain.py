# -*- coding: utf-8 -*-
import random
import os
from trie import Trie
from file_reader import read_file


def create_sentence(dict, start, sentence):
    if start == "x":
        return sentence
    elif sentence.count(".") >= 3:
        return sentence
    else:
        choices = []
        for x in dict[start]:
            for i in range(x[1]):
                if x[0] not in ["JOUSIMIES", "KAKSONEN", "RAPU", "LEIJONA",
                                "VESIMIES", "NEITSYT", "SKORPIONI", "HÄRKÄ",
                                "OINAS", "VAAKA", "KAURIS", "KALAT"]:
                    choices.append(x[0])
        next = random.choice(choices)
        if next != "x":
            sentence.append(next)
        return create_sentence(dict, next, sentence)


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.split(current_dir)[0]
    file = os.path.join(parent_dir, "aineisto.txt")

    list = read_file(file)
    trie = Trie()

    for i in range(len(list)-1):
        if list[i] == ".":
            trie.add_edge(list[i], "x")
        trie.add_edge(list[i], list[i+1])
    x = create_sentence(trie.hashmap, "NEITSYT", ["NEITSYT"])
    print(" ".join(x))
