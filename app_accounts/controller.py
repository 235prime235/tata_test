from bottle import Bottle

app_accounts = Bottle()

@app_accounts.route('/accounts')
def app_accounts_index():
    return 'App HomePage'