import os
from trie import TrieNode

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
    print(len(list))
    nodelist = []
    for i in range(len(list)-1):
        if i-1 < 0:
            node = TrieNode(list[i], "x")
        else:
            node = TrieNode(list[i], list[i-1])
        nodelist.append(node)
    for node in nodelist:
        print(node.prev, node.word)
        