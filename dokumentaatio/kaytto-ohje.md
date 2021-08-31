# Käyttöohje

## Käynnistäminen
- Lataa projektin lähdekoodi 
- Ennen ohjelman käynnistämistä, syötä komento:
> poetry install

- Käynnistä ohjelma komennolla:
> poetry run invoke start

## Käyttö
- Ohjelma kysyy syötteiksi horoskooppimerkkiä (stringinä), ennustuksen pituutta virkkeinä (numeroina)
 ja
Markovin ketjun astetta (numeroina). 
- Ohjelma generoi horoskooppiennustuksen syötteen perusteella ja tulostaa sen näkyviin.
- Tämän jälkeen voi valita haluaako generoida uuden ennustuksen samalla tai eri syötteillä tai sulkea ohjelman syöttämällä numeron ohjeen mukaan.
- Lisäksi:
- voi suorittaa testit:
> poetry run invoke test
- tarkistaa testikattavuuden:
> poetry run invoke coverage-report
- tai tarkastella koodin laatua:
> poetry run invoke lint
