from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
DATABASE = 'path/to/bincom_test.sql'
app.config['DATABASE'] = DATABASE


def get_db():
    db = getattr(app, '_database', None)
    if db is None:
        db = app._database = sqlite3.connect(app.config['DATABASE'])
    return db

# Question 1: Display Result for an Individual Polling Unit


@app.route('/polling_unit/<int:polling_unit_id>')
def polling_unit_results(polling_unit_id):
    results = get_polling_unit_results(polling_unit_id)
    return render_template('polling_unit_results.html', results=results)


def get_polling_unit_results(polling_unit_id):
    query = f"SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid = {polling_unit_id};"
    cursor = get_db().cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results

# Question 2: Display Summed Total Result for Polling Units in a Local Government


@app.route('/summed_total_results')
def summed_total_results():
    lgas = get_all_lgas()
    return render_template('summed_total_results.html', lgas=lgas)


def get_all_lgas():
    query = "SELECT * FROM lga;"
    cursor = get_db().cursor()
    cursor.execute(query)
    lgas = cursor.fetchall()
    return lgas


if __name__ == '__main__':
    app.run(debug=True)
