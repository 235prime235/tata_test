from bottle import Bottle
from app_colors.views.view_colors import view_colors

app_colors = Bottle()

@app_colors.route('/colors')
def app_colors_index():
    return view_colors()