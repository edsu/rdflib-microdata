from unittest import TestCase

import rdflib
import rdflib_microdata

class MicrodataParserTest(TestCase):

    def test_parse(self):
        g = rdflib.Graph()
        g.parse(open("example.html"), format="microdata")
        self.assertTrue(len(g) > 0)

