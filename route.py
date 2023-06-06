from flask import Flask, render_template
import os


app = Flask(__name__)
app.static_folder = 'static'

# two decorators, same function
@app.route('/')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/dashboard')
def symbol():
    return render_template('dashboard.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('index.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
