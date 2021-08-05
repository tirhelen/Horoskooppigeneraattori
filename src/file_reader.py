# -*- coding: utf-8 -*-

def read_file(file):
    """Funktio lukee tekstitiedoston, jossa opetusdata on.
    Palauttaa listan datassa esiintyneista sanoista (ja valimerkeista)
    Args:
        filename (string): opetusdatatiedoston nimi
    Returns:
        list : lista sanoista ja valimerkeista
    """

    file = open(file, "r")
    content = file.read()
    content = content.replace("\n", " ")
    content = content.replace(".", " .")
    content = content.replace(",", " ,")
    list = content.split(" ")
    for word in list:
        if len(word) < 1:
            list.remove(word)
    file.close()
    return list
