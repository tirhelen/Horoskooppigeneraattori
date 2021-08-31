# -*- coding: utf-8 -*-

def siisti_teksti(teksti):
    """siistii ennustetekstin helposti luettavaan muotoon
    Args:
        teksti (list): lista, joka sisältää ennustukseen kuuluvat sanat
    Returns:
        string: siistitty ennusteteksti joka voidaan tulostaa käyttäjälle
    """

    for i in range(len(teksti)-1):
        if teksti[i+1] == ". " or teksti[i+1] == ", ":
            teksti[i] = teksti[i][:-1]
    string = ''.join(map(str, teksti))
    return string
