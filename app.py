from flask import Flask
from flask import render_template
from flask_htmx import HTMX
from bokeh.plotting import figure, curdoc
from bokeh.embed import components
import numpy as np

app = Flask(__name__)
htmx = HTMX(app)


@app.route("/")
def plot_to_web():
    curdoc().theme = "night_sky"
    p = figure(title="dark_minimal", width=400, height=400)
    p.circle([1,2,3,6,8], [7,5,2,8,1], size=10)

    script, div = components(p)

    return render_template("index.html", script=script, div=div)
