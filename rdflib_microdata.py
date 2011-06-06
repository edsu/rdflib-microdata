import xml.dom.minidom

from html5lib import HTMLParser, treebuilders

from rdflib import URIRef
from rdflib.plugin import register
from rdflib.parser import Parser

register("microdata", Parser, "rdflib_microdata", "MicrodataParser")

class MicrodataParser(Parser):

    def parse(self, source, sink, **kwargs):
        parser = HTMLParser(tree=treebuilders.getTreeBuilder("dom"))
        tree = parser.parse(source)
        self._build_graph(tree, sink, 0)

    def _build_graph(self, e, sink, depth):
        print e, depth
        #if isinstance(e, xml.dom.minidom.Element):
        #    if e.hasAttribute('itemscope'):
        #        if e.hasAttribute('itemtype'):
        #            print e.getAttribute('itemtype')

        for child in e.childNodes:
            self._build_graph(child, sink, depth + 1)

        #sink.add((URIRef("foo"), URIRef("bar"), URIRef("baz")))
