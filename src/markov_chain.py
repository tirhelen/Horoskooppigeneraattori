# -*- coding: utf-8 -*-
import random


def create_sentence(dict, start, sentence):
    """luo virkkeen käyttäen toisen asteen Markovin ketjua

    Args:
        dict (dictionary): käytettävä trie, johon aineisto on tallennettu
        start (string): virkkeen aloitussana tai myöhemmin seuraava valittu sana
        sentence (list): lista, johon muodostettava lause kootaan

    Returns:
        sentence (list): lista lopullisesta lauseesta
    """
    choices = []
    for x in dict[start]:
        for i in range(x[1]):
            if x[0] not in ["JOUSIMIES", "KAKSONEN", "RAPU", "LEIJONA",
                            "VESIMIES", "NEITSYT", "SKORPIONI", "HÄRKÄ",
                            "OINAS", "VAAKA", "KAURIS", "KALAT"]:
                choices.append(x[0])
    next = random.choice(choices)
    sentence.append(next)
    if next == ".":
        return sentence
    next = sentence[-2] + " " + sentence[-1]
    return create_sentence(dict, next, sentence)
