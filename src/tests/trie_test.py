import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_correct_key_values(self):
        self.list = ["Tässä", "on", "todella", "tärkeää", "tekstiä", ".",
                "tärkeää", "tekstiä", ",", "jota", "ei", "saa",
                "hukata", ".", "ei", "milloinkaan", "!"]
        help_list = []
        for i in range(len(self.list)):
            if i == len(self.list)-1:
                self.trie.add_edge(self.list[i], None)

            else:
                self.trie.add_edge(self.list[i], self.list[i+1])

            if self.list[i] not in help_list:
                help_list.append(self.list[i])

        keys = sorted(self.trie.hashmap.keys())
        help_list = sorted(help_list)
        self.assertEqual(keys, help_list)
