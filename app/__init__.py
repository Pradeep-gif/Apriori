from flask import Flask, request
from flask import render_template, send_from_directory
import os

from app.apriori import get_rules, get_transaction_data


app = Flask(__name__)
app.secret_key = 'v#wF0/N*VOmOkN^f.9Tv!3=vmWZ__Y'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        fpath = f"datasets/{request.form['database']}-out1.csv"
        transaction_data = get_transaction_data(fpath)
        min_sup = int(request.form['min_support'])
        associated_rules = get_rules(transaction_data, min_sup)
        return render_template("index.html", associated_rules=associated_rules)
