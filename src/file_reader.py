import os
from trie import Trie

def read_file(filename):
    """Funktio lukee tekstitiedoston, jossa opetusdata on.
    Palauttaa listan datassa esiintyneista sanoista (ja valimerkeista)
    Args:
        filename (): opetusdatatiedoston nimi
    Returns:
        list : lista sanoista ja valimerkeista
    """
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.split(current_dir)[0]
    file = os.path.join(parent_dir, filename)
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

if __name__ == "__main__":
    list = read_file("aineisto.txt")
    trie = Trie()
    print(len(list))
    for i in range(len(list)-1):
        trie.add_edge(list[i], list[i+1])

    for key in trie.hashmap:
        print(key)
        print("-")
        for x in trie.hashmap[key]:
            print(x)
        print("----")
