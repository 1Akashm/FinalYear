from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def predict():
    return render_template('predict.html')
    features = [float(x) for x in request.form.values()]
    final= [np.array(features)]

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
   app.run(debug = True)