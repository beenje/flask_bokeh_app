Flask app to embed a bokeh server app
=====================================

Simple example to reproduce https://github.com/bokeh/bokeh/issues/4693

Use conda to create the environment::

    $ conda env create
    
In one terminal, run bokeh server::

    $ source activate flask_bokeh_app
    $ bokeh serve --host localhost:5000 --host localhost:5006 sliders.py

In another window, run flask::

    $ source activate flask_bokeh_app
    $ export FLASK_APP=app.py
    $ flask run

Go to http://localhost:5000/
