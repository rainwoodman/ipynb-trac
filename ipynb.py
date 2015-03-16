# -*- coding: utf-8 -*-
#
# Copyright (C) 2004-2009 Edgewall Software
# Copyright (C) 2004 Oliver Rutherfurd
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://trac.edgewall.org/wiki/TracLicense.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at http://trac.edgewall.org/log/.
#
# Author: Yu Feng yfeng1@berekley.edu
#
# Trac support for reStructured Text, including a custom 'trac' directive
#
# 'trac' directive code by Oliver Rutherfurd, overhauled by cboos.
#
# Inserts `reference` nodes for TracLinks into the document tree.

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
        node = nbformat.reader.read(content)
        result = nbconvert.export_html(node, config=dict(template='basic'))
        return """%s""" % str(result[0])
