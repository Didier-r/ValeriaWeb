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
    return render_template('planesEntrenamiento.html')

@app.route('/clases-grupales')
def clases_grupales():
    return render_template('ClasesGrupales.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
