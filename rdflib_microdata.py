import microdata

from rdflib import URIRef, Literal, BNode, Namespace, RDF
from rdflib.plugin import register
from rdflib.parser import Parser

register("microdata", Parser, "rdflib_microdata", "MicrodataParser")

class MicrodataParser(Parser):

    def parse(self, source, sink, **kwargs):
        """
        Pass in a file or file-like object containing html5 microdata
        and populate the sink graph with triples.
        """
        for item in microdata.get_items(source.getByteStream()):
            self._add_item(item, sink)

    def _add_item(self, item, sink):
        # the URI to hang our assertions off of
        if item.itemid:
            s = URIRef(item.itemid.string)
        else:
            s = BNode()

        # MUST have a profile for the item to convert to rdf data model
        if not item.itemtype:
            return

        # create a vocab namespace, appending a # if it isn't a hash or slash 
        # already
        ns = str(item.itemtype)
        if ns.endswith("#") or ns.endswith("/"):
            ns = Namespace(item.itemtype)
        else:
            ns = Namespace(ns + "#")

        # type the resource
        sink.add((s, RDF.type, str(item.itemtype)))

        # go through each property/value and add triples to the graph
        for item_property, item_values in item.props.items():
            p = ns[item_property]
            for v in item_values:
                if isinstance(v, microdata.Item):
                    o = self._add_item(v, sink) 
                elif isinstance(v, microdata.URI):
                    o = URIRef(v.string)
                else:
                    o = Literal(v)
                # TODO: handle dates
                sink.add((s, p, o))

        return s
