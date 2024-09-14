from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienesSomos.html')

@app.route('/planes-entrenamiento')
def planes_entrenamiento():
    return render_template('planes_entrenamiento.html')

@app.route('/clases-grupales')
def clases_grupales():
    return render_template('clases_grupales.html')

if __name__ == '__main__':
    app.run(debug=True)
