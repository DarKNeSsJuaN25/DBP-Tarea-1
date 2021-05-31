import re
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Softjuandius_25@localhost:3306/ejercicio2db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Seccion(db.Model):
    __tablename__ = 'seccion'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(2),nullable=False)
    profesor_id = db.relationship('Profesor',backref='salon')
    curso_id = db.relationship('Curso',backref='salon')   
    estudiante = db.relationship('Estudiante',backref='salon')

    def __repr__(self):
        return f'ID: {self.id}, Letra: {self.name}, Datos del profesor: {self.profesor_id},    Datos del curso: {self.curso_id},   Datos del estudiante: {self.estudiante}\n'        


class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    lastname = db.Column(db.String(80),nullable=False)
    codigo = db.Column(db.Integer,nullable = False)
    id_seccion = db.Column(db.Integer, db.ForeignKey('seccion.id'))
    def __repr__(self):
        return f'ID: {self.id}, Nombre: {self.name},    Apellido: {self.lastname},  Codigo: {self.codigo}, ID de la seccion: {self.id_seccion}\n'

class Profesor(db.Model):
    __tablename__ = 'profesor'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    lastname = db.Column(db.String(80),nullable=False)
    edad = db.Column(db.Integer,nullable =False)
    id_seccion = db.Column(db.Integer,db.ForeignKey('seccion.id'))
    id_curso = db.Column(db.Integer,db.ForeignKey('curso.id'))

    def __repr__(self):
        return f'ID: {self.id}, Nombre: {self.name},    Apellido: {self.lastname},  Edad: {self.edad},  ID de la seccion: {self.id_seccion}, ID del curso: {self.id_curso} \n'

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    duracion = db.Column(db.String(20),nullable=False)
    id_salon = db.Column(db.Integer,db.ForeignKey('seccion.id'))
    profesor = db.relationship('Profesor',backref='curso')
    def __repr__(self):
        return f'ID: {self.id}, Nombre: {self.name},    Duracion: {self.duracion},  ID del salon: {self.id_salon},   Datos del profesor: {self.profesor}\n'


db.create_all()

@app.route("/") #Decorator
def index():
    return render_template("table.html",data_alumnos = Estudiante.query.all(),data_profesores = Profesor.query.all(),data_cursos= Curso.query.all(),data_seccion =Seccion.query.all())

if __name__ == '__main__':
    app.run()

 