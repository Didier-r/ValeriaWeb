from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para proteger el formulario

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Cambia esto por tu usuario de MySQL
app.config['MYSQL_PASSWORD'] = '123'  # Cambia esto por tu contraseña de MySQL
app.config['MYSQL_DB'] = 'db_ventas'  # Cambia esto por tu base de datos

mysql = MySQL(app)

# Define el formulario con Flask-WTF y WTForms
class RegisterForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    fechaNacimiento = StringField("Fecha de Nacimiento", validators=[DataRequired()])
    correo = StringField("Correo Electrónico", validators=[DataRequired(), Email()])
    cedula = StringField("Cédula", validators=[DataRequired()])
    descripcion = TextAreaField("Descripción (indique lesiones o detalles adicionales)")
    plan = SelectField("Plan", choices=[('amigos', 'Plan de Amigos'), ('individual', 'Plan Individual')], validators=[DataRequired()])
    submit = SubmitField("Enviar")

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

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = RegisterForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        fechaNacimiento = form.fechaNacimiento.data
        correo = form.correo.data
        cedula = form.cedula.data
        descripcion = form.descripcion.data
        plan = form.plan.data
        
        # Conectar a la base de datos y almacenar los datos
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO registros (nombre, apellido, fecha_nacimiento, correo, cedula, descripcion, plan)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nombre, apellido, fechaNacimiento, correo, cedula, descripcion, plan))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('success'))

    return render_template('formulario.html', form=form)

@app.route('/success')
def success():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
