from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/hack', methods=['GET', 'POST'])
def hack():
    navn = request.form['name']
    print(navn)
    return 'Funka'


if __name__ == '__main__':
    app.run(debug=True)