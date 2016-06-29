from flask import Flask, render_template
from bokeh.embed import autoload_server

app = Flask(__name__)


@app.route('/')
def index():
    script = autoload_server(model=None, app_path="/sliders")
    return render_template('index.html', bokeh_script=script)
