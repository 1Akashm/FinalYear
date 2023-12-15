from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict')
def predict():
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


if __name__ == '__main__':
   app.run(debug = True)