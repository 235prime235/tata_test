from bottle import Bottle, get, static_file
from app_home.views.view_index import view_index
from app_home.views.view_home import view_home
from app_home.views.view_help import view_help
from app_home.views.view_about import view_about

app_home = Bottle()

@app_home.route('/')
def app_home_index():
    return view_index()

@app_home.route('/home')
def app_home_home():
    return view_home()

@app_home.route('/help')
def app_home_home():
    return view_help()

@app_home.route('/about')
def app_home_home():
    return view_about()





# Static Routes
@app_home.get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@app_home.get("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/font")

@app_home.get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg|3ds)>")
def img(filepath):
    return static_file(filepath, root="static/img")

@app_home.get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@app_home.get("/static/models/<filepath:re:.*\.3ds>")
def threeds(filepath):
    return static_file(filepath, root="static/models")