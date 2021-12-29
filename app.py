from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sample_data')
def sample_data():
    return render_template('website.html')


if __name__ == '__main__':
    app.run(debug=True)