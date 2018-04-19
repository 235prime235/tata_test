from bottle import Bottle
from config import *
from app_home.controller import app_home
from app_accounts.controller import app_accounts
from app_colors.controller import app_colors

app_root = Bottle()

setup_database()

if __name__ == '__main__':
    app_root.merge(app_home)
    app_root.merge(app_accounts)
    app_root.merge(app_colors)
    
    #debug server start-up
    app_root.run(debug=True, reloader=True)

    #production server start-up
    #app_root.run(host='178.62.11.182', port=8080, debug=False)