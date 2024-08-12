# mi-proyecto

CLONAR EL REPOSITORIO

INSTALAR REQUERIMIENTOS

pip install -r requirements.txt

Instalar Flask, Flask-SQLAlchemy, Flask-Migrate y PyMySQL
pip install Flask Flask-SQLAlchemy Flask-Migrate PyMySQL

CREAR EL ENTORNO VIRTUAL

python3 -m venv env

ACTIVAR EL ENTORNO VIRTUAL

source env/bin/activate

CONFIGURA LA BASE DE DATOS

INICIALIZA LA BASE DE DATOS

flask db init

COMANDO PARA HACER UNA MIGRACIÓN

flask db migrate -m "Initial migration"

COMANDO PARA ACTUALIZAR LA MIGRACIÓN

flask db upgrade

EJECUTA LA APLICACIÓN

flask run --reload
