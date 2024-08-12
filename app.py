from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/local_celulares'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Proveedor, Fabricante, Modelo, Caracteristica, Accesorio, Stock, Equipo

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/marca", methods=['POST', 'GET'])
def marcas():
    marcas = Marca.query.all()
    
    if request.method == 'POST':
        nombre_categoria = request.form['nombre_categoria']
        nueva_marca = Marca(nombre_categoria=nombre_categoria)
        db.session.add(nueva_marca)
        db.session.commit()
        return redirect(url_for('marcas'))
    
    return render_template('marca.html', marcas=marcas)

@app.route("/marca/<id>/eliminar", methods=['POST', 'GET'])
def eliminar_marcas(id):
    marca = Marca.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(marca)
        db.session.commit()
        return redirect(url_for('marcas'))

    return render_template("eliminar_marca.html", marca=marca)

@app.route("/marca/<id>/editar", methods=['POST', 'GET'])
def editar_marcas(id):
    marca = Marca.query.get_or_404(id)

    if request.method == 'POST':
        marca.nombre_categoria = request.form['nombre_categoria']
        db.session.commit()
        return redirect(url_for('marcas'))
    
    return render_template("editar_marca.html", marca=marca)

@app.route("/proveedor", methods=['POST', 'GET'])
def proveedor():
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        nombre_proveedor = request.form['nombre_proveedor']
        contacto = request.form['contacto']
        nuevo_proveedor = Proveedor(nombre_proveedor=nombre_proveedor, contacto=contacto)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return redirect(url_for('proveedor'))
    
    return render_template('proveedor.html', proveedores=proveedores)

@app.route("/proveedor/<id>/eliminar", methods=['POST', 'GET'])
def eliminar_proveedor(id):
    proveedor = Proveedor.query.get(id)

    if request.method == 'POST':
        db.session.delete(proveedor)
        db.session.commit()
        return redirect(url_for('proveedor'))
    
    return render_template("eliminar_proveedor.html", proveedor=proveedor)

@app.route("/proveedor/<id>/editar", methods=['POST', 'GET'])
def editar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)

    if request.method == 'POST':
        proveedor.nombre_proveedor = request.form['nombre_proveedor']
        proveedor.contacto = request.form['contacto']
        db.session.commit()
        return redirect(url_for('proveedor'))
    
    return render_template("editar_proveedor.html", proveedor=proveedor)

@app.route("/fabricante", methods=['POST', 'GET'])
def fabricantes():
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        nombre_fabricante = request.form['nombre_fabricante']
        pais_origen = request.form['pais_origen']
        nuevo_fabricante = Fabricante(nombre_fabricante=nombre_fabricante, pais_origen=pais_origen)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('fabricantes'))
    
    return render_template('fabricante.html', fabricantes=fabricantes)

@app.route("/fabricante/<id>/eliminar", methods=['POST', 'GET'])
def eliminar_fabricante(id):
    fabricante = Fabricante.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(fabricante)
        db.session.commit()
        return redirect(url_for('fabricantes'))
    
    return render_template("eliminar_fabricante.html", fabricante=fabricante)

@app.route("/fabricante/<id>/editar", methods=['POST', 'GET'])
def editar_fabricante(id):
    fabricante = Fabricante.query.get_or_404(id)

    if request.method == 'POST':
        fabricante.nombre_fabricante = request.form['nombre_fabricante']
        fabricante.pais_origen = request.form['pais_origen']
        db.session.commit()
        return redirect(url_for('fabricantes'))
    
    return render_template("editar_fabricante.html", fabricante=fabricante)

@app.route("/modelo", methods=['POST', 'GET'])
def modelos():
    modelos = Modelo.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_modelo = Modelo(nombre=nombre)
        db.session.add(nuevo_modelo)
        db.session.commit()
        return redirect(url_for('modelos'))

    return render_template('modelo.html', modelos=modelos)

@app.route("/modelo/<id>/eliminar", methods=['POST', 'GET'])
def eliminar_modelo(id):
    modelo = Modelo.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(modelo)
        db.session.commit()
        return redirect(url_for('modelos'))
    
    return render_template("eliminar_modelo.html", modelo=modelo)

@app.route("/modelo/<id>/editar", methods=['POST', 'GET'])
def editar_modelo(id):
    modelo = Modelo.query.get_or_404(id)

    if request.method == 'POST':
        modelo.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('modelos'))
    
    return render_template("editar_modelo.html", modelo=modelo)

@app.route("/caracteristicas", methods=['POST', 'GET'])
def caracteristicas():
    caracteristicas = Caracteristica.query.all()

    if request.method == 'POST':
        tamanio_pantalla = request.form['tamanio_pantalla']
        capacidad_bateria = request.form['capacidad_bateria']
        camara = request.form['camara']
        memoria = request.form['memoria']
        color = request.form['color']
        descripcion = request.form['descripcion']
        nuevas_caracteristicas = Caracteristica(tamanio_pantalla=tamanio_pantalla, capacidad_bateria=capacidad_bateria, camara=camara, memoria=memoria, color=color, descripcion=descripcion)
        db.session.add(nuevas_caracteristicas)
        db.session.commit()
        return redirect(url_for('caracteristicas'))
    
    return render_template('caracteristicas.html', caracteristicas=caracteristicas)

@app.route("/caracteristicas/<id>/eliminar", methods=['POST', 'GET'])
def eliminar_caracteristica(id):
    caracteristica = Caracteristica.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(caracteristica)
        db.session.commit()
        return redirect(url_for('caracteristicas'))
    
    return render_template("eliminar_caracteristica.html", caracteristica=caracteristica)

@app.route("/caracteristicas/<id>/editar", methods=['POST', 'GET'])
def editar_caracteristica(id):

    caracteristica = Caracteristica.query.get_or_404(id)

    if request.method == 'POST':
        caracteristica.tamanio_pantalla = request.form['tamanio_pantalla']
        caracteristica.capacidad_bateria = request.form['capacidad_bateria']
        caracteristica.camara = request.form['camara']
        caracteristica.memoria = request.form['memoria']
        caracteristica.color = request.form['color']
        caracteristica.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('caracteristicas'))
    
    return render_template("editar_caracteristica.html", caracteristica=caracteristica)

@app.route("/accesorio", methods=['POST', 'GET'])
def accesorio():
    accesorios = Accesorio.query.all()

    if request.method == 'POST':
        tipo_accesorio = request.form['tipo_accesorio']
        tipo_accesorio2 = request.form['tipo_accesorio2']
        nuevo_accesorio = Accesorio(tipo_accesorio=tipo_accesorio, tipo_accesorio2=tipo_accesorio2)
        db.session.add(nuevo_accesorio)
        db.session.commit()
        return redirect(url_for('accesorio'))
    
    return render_template('accesorio.html', accesorios=accesorios)

@app.route("/accesorio/<id>/eliminar", methods=['POST', 'GET'])
def eliminar_accesorio(id):
    accesorio = Accesorio.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(accesorio)
        db.session.commit()
        return redirect(url_for('accesorio'))
    
    return render_template("eliminar_accesorio.html", accesorio=accesorio)

@app.route("/accesorio/<id>/editar", methods=['POST', 'GET'])
def editar_accesorio(id):
    accesorio = Accesorio.query.get_or_404(id)

    if request.method == 'POST':
        accesorio.tipo_accesorio = request.form['tipo_accesorio']
        accesorio.tipo_accesorio2 = request.form['tipo_accesorio2']
        db.session.commit()
        return redirect(url_for('accesorio'))
    
    return render_template("editar_accesorio.html", accesorio=accesorio)

@app.route("/stock", methods=['POST', 'GET'])
def stock():
    stocks = Stock.query.all()

    if request.method == 'POST':    
        cantidad_disponible = request.form['cantidad_disponible']
        ubicacion_almacen = request.form['ubicacion_almacen']
        stocks_item = Stock(cantidad_disponible=cantidad_disponible, ubicacion_almacen=ubicacion_almacen)
        db.session.add(stocks_item)
        db.session.commit() 
        return redirect(url_for('stock'))
    
    return render_template('stock.html', stocks=stocks)

@app.route("/stock/<id>/eliminar", methods=['POST', 'GET'])
def eliminar_stock(id):
    stocks = Stock.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(stocks)
        db.session.commit()
        return redirect(url_for('stock'))
    
    return render_template("eliminar_stock.html", stocks=stocks)

@app.route("/stock/<id>/editar", methods=['POST', 'GET'])
def editar_stock(id):
    stocks = Stock.query.get_or_404(id)

    if request.method == 'POST':
        stocks.cantidad_disponible = request.form['cantidad_disponible']
        stocks.ubicacion_almacen = request.form['ubicacion_almacen']
        db.session.commit()
        return redirect(url_for('stock'))
    
    return render_template("editar_stock.html", stocks=stocks)


@app.route("/equipo", methods=['POST', 'GET'])
def equipos():
    equipos = Equipo.query.all()
    marcas = Marca.query.all()
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()
    proveedores = Proveedor.query.all()
    stocks = Stock.query.all()
    accesorios = Accesorio.query.all()
    caracteristicas = Caracteristica.query.all()

    if request.method == 'POST':
        costo = request.form['costo']
        marca = request.form['marca']
        modelo = request.form['modelo']
        nombre_fabricante = request.form['nombre_fabricante']
        nombre_proveedor = request.form['nombre_proveedor']
        cantidad_disponible = request.form['cantidad_disponible']
        color = request.form['color']
        tipo_accesorio = request.form['tipo_accesorio']
        nuevo_equipo = Equipo(costo=costo, marca_id=marca, modelo_id=modelo, fabricante_id=nombre_fabricante, proveedor_id=nombre_proveedor, stock_id=cantidad_disponible, caracteristica_id=color, accesorio_id=tipo_accesorio)
        db.session.add(nuevo_equipo)
        db.session.commit()
        return redirect(url_for('equipos'))    
    
    return render_template('equipo.html', equipos=equipos, marcas=marcas, modelos=modelos, fabricantes=fabricantes, proveedores=proveedores, stocks=stocks, accesorios=accesorios, caracteristicas=caracteristicas)

@app.route("/equipo/<id>/eliminar", methods=['POST', 'GET'])
def eliminar_equipo(id):
    equipo = Equipo.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(equipo)
        db.session.commit()
        return redirect(url_for('equipos'))
    
    return render_template("eliminar_equipo.html", equipo=equipo)

@app.route("/equipo/<id>/editar", methods=['POST', 'GET'])
def editar_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    marcas = Marca.query.all()
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()
    proveedores = Proveedor.query.all()
    stocks = Stock.query.all()
    accesorios = Accesorio.query.all()
    caracteristicas = Caracteristica.query.all()

    if request.method == 'POST':
        equipo.costo = request.form['costo']
        equipo.marca = Marca.query.get(request.form['marca'])
        equipo.modelo = Modelo.query.get(request.form['modelo'])
        equipo.nombre_fabricante = Fabricante.query.get(request.form['nombre_fabricante'])
        equipo.nombre_proveedor = Proveedor.query.get(request.form['nombre_proveedor'])
        equipo.cantidad_disponible = Stock.query.get(request.form['cantidad_disponible'])
        equipo.color = Caracteristica.query.get(request.form['color'])
        equipo.tipo_accesorio = Accesorio.query.get(request.form['tipo_accesorio'])

        db.session.commit()
        return redirect(url_for('equipos'))
    
    return render_template("editar_equipo.html", equipo=equipo, marcas=marcas, modelos=modelos, fabricantes=fabricantes, proveedores=proveedores, stocks=stocks, accesorios=accesorios, caracteristicas=caracteristicas) 