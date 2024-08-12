from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre_categoria
    
class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_proveedor = db.Column(db.String(50), nullable=False)
    contacto = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre_proveedor, self.contacto

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_fabricante = db.Column(db.String(50), nullable=False)
    pais_origen = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre_fabricante, self.pais_origen
    
class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre
    
class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tamanio_pantalla = db.Column(db.String(50), nullable=False)
    capacidad_bateria = db.Column(db.String(50), nullable=False)
    camara = db.Column(db.String(50), nullable=False)
    memoria = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)

    def __str__(self) -> str:
        return self.tamanio_pantalla, self.capacidad_bateria, self.camara, self.memoria, self.color, self.descripcion
    

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_accesorio = db.Column(db.String(50), nullable=False)
    tipo_accesorio2 = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.tipo_accesorio, self.tipo_accesorio2

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    ubicacion_almacen = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.cantidad_disponible, self.ubicacion_almacen
    
class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    costo = db.Column(db.Integer, nullable=False)

    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    accesorio_id = db.Column(db.Integer, db.ForeignKey('accesorio.id'), nullable=False)


    marca = db.relationship('Marca', backref=db.backref('equipos', lazy=True))
    modelo = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))
    proveedor = db.relationship('Proveedor', backref=db.backref('equipos', lazy=True))
    fabricante = db.relationship('Fabricante', backref=db.backref('equipos', lazy=True))
    caracteristica = db.relationship('Caracteristica', backref=db.backref('equipos', lazy=True))
    stock = db.relationship('Stock', backref=db.backref('equipos', lazy=True))
    accesorio = db.relationship('Accesorio', backref=db.backref('equipos', lazy=True))
