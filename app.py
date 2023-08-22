import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from flask import Flask

app = Flask(__name__)


@app.route("/plot")
def plot_to_web():
    x = np.linspace(0, 2*np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    html_str = mpld3.fig_to_html(fig)
    return html_str
