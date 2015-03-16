ipynb-trac
=========

Previewing IPython Notebook attachments on Trac.

Installation
------------

  1. make sure ipython[notebook] is installed.

    .. code::

        # as root 
        easy_install ipython[notebook]

        #or as the user running trac
        easy_install --user ipython[notebook]
        
    Also, nbconvert (the notebook to html converter) depends on pandoc;
    pandoc is written in Haskell. Thus depending on the level of voodoo
    you have, install it with 'apt-get' or 'yum'

    .. code::

        su -c 'yum install pandoc'

    2. copy ipynb.py to your trac's plugin/ directory. 
       Admin shall be able to see IPythonNotebookRenderer in 
       admin/general/plugin, under the catalogue 'ipynb'. 
       Enable it.

    .. code::

        cp ipynb.py mytracdir/plugin

    2. edit conf/trac.ini. 
       Increase the max_size and also set up the mime type of .ipynb files.

    .. code:: ini

        [attachment]
        max_size = 26214400
        max_zip_size = 209715200

        [mimeviewer]
        mime_map = text/x-ipynb:ipynb
        max_preview_size = 26214400


