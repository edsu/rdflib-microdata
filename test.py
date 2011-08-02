from unittest import TestCase

from rdflib import Graph, URIRef, Namespace, RDF, BNode

import rdflib_microdata

class MicrodataParserTest(TestCase):

    def test_parse(self):
        g = Graph()
        g.parse(open("example.html"), format="microdata")
        g.serialize(open("example.rdf", "w"))
      
        # seem to be the right amount of assertions?
        self.assertEqual(len(g), 15)

        # is there an person?
        s = URIRef("http://www.xyz.edu/~jane")
        person = Namespace("http://schema.org/Person#")
        self.assertEqual(g.value(s, RDF.type), URIRef("http://schema.org/Person"))
        self.assertEqual(g.value(s, person.telephone), "(425) 123-4567")

        # is the person attached to an address?
        addr = Namespace("http://schema.org/PostalAddress#")
        a = BNode(g.value(s, person.address))
        self.assertEqual(g.value(a, RDF.type), URIRef("http://schema.org/PostalAddress"))
        self.assertEqual(g.value(a, addr.postalCode), "98052")

        # TODO: test dates?
