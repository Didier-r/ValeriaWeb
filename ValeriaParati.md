Codigo que se usaran para la ejecucion 

Primero lo que hariamos seria instalar el entorno virtual  de la siguente manera 

pip install virtualenv

y luego creariamos el entorno virtual

virtualenv venv

luego seguimos con iniciar el entorno virtual

.\venv\Scripts\activate

y luego seguimos con la instalacion de flask

pip install flask

y ahi seguimos con la instalacion de flask-wtf

pip install Flask-wtf

y de ahi luego seguimos con la instalcion de  WTForms 

pip install WTForms 

y de ahi continuamos con la instalacion de Flask-MySQLdb

pip install Flask-MySQLdb

y lo siguente para instalar es esto email_validator

pip install email_validator


Creacion de la tabla para la base de datos 
CREATE TABLE registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    correo VARCHAR(255) NOT NULL,
    cedula VARCHAR(50) NOT NULL,
    descripcion TEXT,
    plan ENUM('amigos', 'individual') NOT NULL
);