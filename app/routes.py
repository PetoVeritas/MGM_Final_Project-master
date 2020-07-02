from flask import render_template
from app import app

import io
import random
import pandas as pd
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Martin'}
    posts = [
        {
            'author': {'username': 'Carlos'},
            'body': 'This site looks.."great"!'
        },
        {
            'author': {'username': 'Brenna'},
            'body': 'Where are the Moops?!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/historic')
def historic():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
