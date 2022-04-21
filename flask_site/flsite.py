from flask import Flask, render_template

menu = ['Математика', 'Биология', 'Информатика']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mk')
def mk():
    return render_template('math.html')

if __name__ == '__main__':
    app.run(debug=True)
