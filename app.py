from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    
    if request.method == 'POST':
        selected_model = request.form['model']
        prediction = ""

        if selected_model == 'logistic':
            # Perform logistic regression prediction and get result
            prediction = "Prediction result for Logistic Regression is"
        elif selected_model == 'svm':
            # Perform SVM prediction and get result
            prediction = "Prediction result for Support Vector Machine is"

        return render_template('predict.html',prediction= prediction)
    return render_template('predict.html')


@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/image', methods=['GET','POST'])
def image():
    prediction=""
    if request.method== 'POST':
        prediction = "image success"
        return render_template('image.html',prediction= prediction)

    return render_template('image.html',prediction="")


if __name__ == '__main__':
   app.run(debug = True)