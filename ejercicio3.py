import re
from flask import Flask, render_template, request,redirect,url_for
from flask.scaffold import F
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.orm import query

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Softjuandius_25@localhost:5432/ejercicio3db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Registro(db.Model):
    __tablename__ = 'registro'
    id = db.Column(db.Integer,primary_key = True)
    usuario =db.Column(db.String(80),nullable=False)
    contraseña = db.Column(db.String(80),nullable=False)
    direccion = db.Column(db.String(80),nullable=False)
    telefono = db.Column(db.Integer,nullable=False)
    nombre = db.Column(db.String(80),nullable=False)
    apellido = db.Column(db.String(80),nullable=False)
    #tarjeta = db.relationship('Tarjeta',backref='id_Persona')   
    def __repr__(self):
        return f'ID: {self.id}, Nombre: {self.nombre},  Apellido: {self.apellido},  Usuario: {self.usuario},   Contraseña: {self.contraseña},   Direccion: {self.direccion},    Telefono: {self.telefono}\n'


class Pedido(db.Model):
    __tablename__ = 'pedido'    
    id = db.Column(db.Integer,primary_key = True)
    pedido = db.Column(db.String(80),nullable=False)
    def __repr__(self):
        return f'ID: {self.id}, Pedido: {self.pedido}\n'

class Tarjeta(db.Model):
    __tablename__='tarjeta'
    id = db.Column(db.Integer,primary_key =True)
    tarjeta = db.Column(db.Integer,nullable=False)
    #id_persona = db.Column(db.Integer,db.ForeignKey('registro.id'))
    def __repr__(self):
        return f'ID: {self.id}, Tarjeta: {self.tarjeta}\n'


class Envio(db.Model):
    __tablename='envio'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)  
    def __repr__(self):
        return f'ID: {self.id}, Pedido: {self.nombre}\n'



@app.route('/create',methods =['POST'])
def create_registro():
    usuario = request.form.get('usuario','')
    contraseña = request.form.get('contraseña','')
    direccion = request.form.get('direccion')
    telefono = request.form.get('telefono')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    todo1 = Registro(usuario=usuario,contraseña=contraseña,direccion =direccion,telefono=telefono,nombre=nombre,apellido=apellido)
    db.session.add(todo1)
    db.session.commit()
    return redirect(url_for('index2'))

@app.route('/orden',methods =['POST'])
def orden():
    pedido = request.form.get('pedido','')
    todo2 = Pedido(pedido = pedido)
    db.session.add(todo2)
    db.session.commit()
    return redirect(url_for('index2'))

@app.route('/')
def index():
    return render_template('index.html',data = Registro.query.all())

@app.route('/pedido')
def index2():
    return render_template('index_2.html')

@app.route('/lista')
def index3():
    return render_template('index_3.html',data = Pedido.query.all())

@app.route('/pagar',methods=['POST'])
def pago():
    tarjeta = request.form.get('tarjeta','')
    todo = Tarjeta(tarjeta = tarjeta)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index6'))

@app.route('/pago')
def index5():
    return render_template('index_4.html',data = Tarjeta.query.all())


@app.route('/envio',methods =['POST'])
def envios():
    envio =request.form.get('pedido')
    todo = Envio(nombre = envio)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index7'))

@app.route('/enviar')
def index6():
    return render_template('index_5.html',data = Tarjeta.query.all())

@app.route('/final')
def index7():
    return render_template('index_6.html',data_registro=Registro.query.all(),data_pedido=Pedido.query.all(),data_tarjeta=Tarjeta.query.all(),data_envio=Envio.query.all())


db.create_all()
if __name__ == '__main__':
    app.run()