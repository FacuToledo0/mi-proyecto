# mi-proyecto

CLONAR EL REPOSITORIO

Instalar requerimientos

pip install -r requirements.txt

Instalar Flask, Flask-SQLAlchemy, Flask-Migrate y PyMySQL
pip install Flask Flask-SQLAlchemy Flask-Migrate PyMySQL

Crear el entorno virtual

python3 -m venv env

Activar el entorno virtual

source env/bin/activate

Configura la Base de Datos

Inicializa la Base de Datos

flask db init

Comando para hacer una migración

flask db migrate -m "Initial migration"

Comando para actualizar la migración

flask db upgrade

Ejecuta la Aplicación

flask run --reload
