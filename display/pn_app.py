import panel as pn


from .app1 import ResultsViewer


def app(doc):
    rb = ResultsViewer()
    row = pn.Row(rb.panel())
    row.server_doc(doc)


