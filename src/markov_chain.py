# -*- coding: utf-8 -*-
import random


def create_sentence(dict, start, sentence, degree, help_list, length):
    """luo virkkeen käyttäen toisen asteen Markovin ketjua

    Args:
        dict (dictionary): käytettävä trie, johon aineisto on tallennettu
        start (string): virkkeen aloitussana tai myöhemmin seuraava valittu sana
        sentence (list): lista, johon muodostettava lause kootaan

    Returns:
        sentence (list): lista lopullisesta lauseesta
    """
    if sentence.count(". ") == length:
        return sentence

    choices = []
    for x in dict[start]:
        for j in range(x[1]):
            if x[0] not in ["JOUSIMIES", "KAKSONEN", "RAPU", "LEIJONA",
                            "VESIMIES", "NEITSYT", "SKORPIONI", "HÄRKÄ",
                            "OINAS", "VAAKA", "KAURIS", "KALAT"]:
                choices.append(x[0])
            else:
                choices.append(".")

    next = random.choice(choices) + " "

    if next == ". " and start[-2] == ".":
        return create_sentence(dict, ". ", sentence, degree, [], length)

    sentence.append(next)
    help_list.append(next)

    if len(help_list) == degree+1:
        help_list.pop(0)

    next = ''.join(map(str, help_list))

    return create_sentence(dict, next, sentence, degree, help_list, length)
