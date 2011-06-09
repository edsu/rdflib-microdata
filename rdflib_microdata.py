import microdata

from rdflib import URIRef
from rdflib.plugin import register
from rdflib.parser import Parser

register("microdata", Parser, "rdflib_microdata", "MicrodataParser")

class MicrodataParser(Parser):

    def parse(self, source, sink, **kwargs):
        # TODO: something not right here with source :-(
        items = microdata.get_items(source)
        # build the graph now :-)
