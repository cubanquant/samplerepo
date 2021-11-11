from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
app = Flask(__name__)


@app.route('/adder/<x>/<y>')
def adder(x, y):
    result = float(x) + float(y)
    return f'{x} + {y} = {result}'


@app.route('/hello/<name>')
def hello_name(name):
    mylist = [2, 45, 6, 32, 2354, 66, 6]
    return render_template('helloname.html', the_name=name, lst=mylist)


@app.route('/helloaction', methods=['GET', 'POST'])
def hello_action():
    if request.method == "POST":
        name = request.form['name']
    else:
        name = request.args.get('name', '')
    return render_template('helloname.html', the_name=name)


@app.route('/helloform')
def hello_form():
    return render_template('helloform.html')


@app.route('/helloworld')
def hello_world():
    return render_template('helloworld.html')


@app.route('/')
def main():
    return redirect(url_for('hello_world'))


if __name__ == "__main__":
    app.run(debug=True)
