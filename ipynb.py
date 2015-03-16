# -*- coding: utf-8 -*-
#
# This software is licensed as some open-source license; which is 
# yet to be decided.
#
# Author: Yu Feng <yfeng1@berkeley.edu>
#
# Trac support for IPython Notebook attachments
#
# Loosely based on the ReST support by 
#     Daniel Lundin, Oliver Rutherfurd, and Nuutti Kotivuori.
#    (@trac/mimeview/rst.py)
#

__docformat__ = 'IPythonNotebook'

from distutils.version import StrictVersion
try:
    from IPython import __version__
    from IPython import nbconvert
    from IPython import nbformat
    has_docutils = True
except ImportError:
    has_docutils = False

from trac.core import *
from trac.env import ISystemInfoProvider
from trac.mimeview.api import IHTMLPreviewRenderer

class IPythonNotebookRenderer(Component):
    """HTML renderer for IPython Notebooks; 
        Requires IPython[notebook] (which requires pandoc)
    """
    implements(ISystemInfoProvider, IHTMLPreviewRenderer)

    can_render = False

    def __init__(self):
        self.can_render = True
    # ISystemInfoProvider methods

    def get_system_info(self):
        if has_docutils:
            yield 'Docutils', __version__

    # IHTMLPreviewRenderer methods

    def get_quality_ratio(self, mimetype):
        if self.can_render and mimetype in ('text/x-ipynb') :
            return 8
        return 0

    def render(self, context, mimetype, content, filename=None, rev=None):
        try:
            node = nbformat.reader.read(content)
            result = nbconvert.export_html(node, config=dict(template='basic'))
            return """%s""" % str(result[0])
        except Exception as e:
            return """<h2>Conversion failed</h2><pre>%s</pre>""" % str(e)
