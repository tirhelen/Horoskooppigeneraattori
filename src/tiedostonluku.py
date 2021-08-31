# -*- coding: utf-8 -*-

def lue_tiedosto(tiedosto):
    """Funktio lukee tekstitiedoston, jossa opetusdata on.
    Palauttaa listan datassa esiintyneista sanoista (ja välimerkeistä)
    Args:
        tiedosto (string): opetusdatatiedoston nimi
    Returns:
        lista (list): lista sanoista ja välimerkeistä
    """

    tiedosto = open(tiedosto, "r")
    sisalto = tiedosto.read()
    sisalto = sisalto.replace("\n", " ")
    sisalto = sisalto.replace(".", " .")
    sisalto = sisalto.replace(",", " ,")
    lista = sisalto.split(" ")
    for word in lista:
        if len(word) < 1:
            lista.remove(word)
    tiedosto.close()
    return lista
