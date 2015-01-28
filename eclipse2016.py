from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.debug = True
app.secret_key = 'aw.. a secret key'

@app.route('/')
def index():
    return render_template('gerhana2016.html')

@app.route('/gerhana')
def gerhana():
    return render_template('gerhana.html')

@app.route('/pengamatan')
def pengamatan():
    return render_template('pengamatan.html')

if __name__ == "__main__":
    app.run()
