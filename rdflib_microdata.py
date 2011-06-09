import microdata

from rdflib import URIRef
from rdflib.plugin import register
from rdflib.parser import Parser

register("microdata", Parser, "rdflib_microdata", "MicrodataParser")

class MicrodataParser(Parser):

    def parse(self, source, sink, **kwargs):
        items = microdata._build_graph(source)
        # build the graph now :-)
