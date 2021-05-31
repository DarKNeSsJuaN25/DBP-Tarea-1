import psycopg2
import mysql.connector

connection = mysql.connector.connect(host='localhost', database = 'ejercicio1db', user = 'root',password='Softjuandius_25')
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

cursor.execute('drop table if exists estudiante')
cursor.execute('''
    create table estudiante(
        id int PRIMARY KEY auto_increment NOT NULL,
        name VARCHAR(50),
        apellido VARCHAR(50),
        codigo INTEGER,
        seccion VARCHAR(1)
    );
'''
)
cursor.execute('drop table if exists profesor')
cursor.execute('''
    create table profesor(
        id int PRIMARY KEY auto_increment NOT NULL,
        name VARCHAR(50),
        apellido VARCHAR(50),
        edad INTEGER,
        seccion VARCHAR(2),
        curso VARCHAR(50)      
    );
'''
)
cursor.execute('drop table if exists curso')
cursor.execute('''
    create table curso(
        id int PRIMARY KEY auto_increment NOT NULL,
        name VARCHAR(50),
        duracion VARCHAR(50),
        profesor VARCHAR(50)
    );
'''
)

cursor.execute('drop table if exists seccion')
cursor.execute('''
    create table seccion(
        id int PRIMARY KEY auto_increment NOT NULL,
        name VARCHAR(20),
        alumno VARCHAR(30),
        profesor VARCHAR(30),
        curso VARCHAR(30)
    );
'''
)


cursor.execute('''INSERT INTO estudiante(name,apellido,codigo,seccion) VALUES('Juan','Laredo',100,'A');''')
cursor.execute('''INSERT INTO estudiante(name,apellido,codigo,seccion) VALUES('Gustavo','Delgado',101,'B');''')
cursor.execute('''INSERT INTO estudiante(name,apellido,codigo,seccion) VALUES('Selena','Gomez',102,'C');''')

cursor.execute('''INSERT INTO estudiante(name,apellido,codigo,seccion) VALUES(%s,%s,%s,%s); ''',('Diego','Dulanto',103,'B'))
cursor.execute('''INSERT INTO estudiante(name,apellido,codigo,seccion)'''+ '''VALUES (%(name)s,%(apellido)s,%(codigo)s,%(seccion)s)''',{'name':'Sebastian','apellido':'Banda','codigo':104,'seccion':'A'})
cursor.execute('''INSERT INTO estudiante(name,apellido,codigo,seccion)'''+ '''VALUES (%(name)s,%(apellido)s,%(codigo)s,%(seccion)s)''',{'name':'Tamara','apellido':'Paredes','codigo':105,'seccion':'B'})

data = {'name' : 'Francis','apellido':'Baldeza','codigo':106,'seccion':'B'}    
lugar = 'INSERT INTO estudiante(name,apellido,codigo,seccion) VALUES (%(name)s,%(apellido)s,%(codigo)s,%(seccion)s);'
cursor.execute(lugar,data)
data = {'name' : 'Walter','apellido':'Cajavilca','codigo':107,'seccion':'A'}    
lugar = 'INSERT INTO estudiante(name,apellido,codigo,seccion) VALUES (%(name)s,%(apellido)s,%(codigo)s,%(seccion)s);'
cursor.execute(lugar,data)
data = {'name' : 'Pedro','apellido':'Cutipa','codigo':108,'seccion':'C'}    
lugar = 'INSERT INTO estudiante(name,apellido,codigo,seccion) VALUES (%(name)s,%(apellido)s,%(codigo)s,%(seccion)s);'
cursor.execute(lugar,data)
data = {'name' : 'Rafael','apellido':'De la Cruz','codigo':109,'seccion':'A'}    
lugar = 'INSERT INTO estudiante(name,apellido,codigo,seccion) VALUES (%(name)s,%(apellido)s,%(codigo)s,%(seccion)s);'
cursor.execute(lugar,data)




cursor.execute('''INSERT INTO profesor(name,apellido,edad,seccion,curso) VALUES('Mauricio','Soto',65,'A','Historia');''')
cursor.execute('''INSERT INTO profesor(name,apellido,edad,seccion,curso) VALUES('Yuan','Galaga',45,'B','Educacion Fisica');''')
cursor.execute('''INSERT INTO profesor(name,apellido,edad,seccion,curso) VALUES('Judith','Origuella',58,'C','Matematica');''')

cursor.execute('''INSERT INTO profesor(name,apellido,edad,seccion,curso) VALUES(%s,%s,%s,%s,%s); ''',('Diego','Chavarri',53,'D','Taller Deportivo'))
cursor.execute('''INSERT INTO profesor(name,apellido,edad,seccion,curso)'''+ '''VALUES (%(name)s,%(apellido)s,%(edad)s,%(seccion)s,%(curso)s)''',{'name':'Sebastian','apellido':'Meneses','edad':54,'seccion':'E','curso':'Arte'})
cursor.execute('''INSERT INTO profesor(name,apellido,edad,seccion,curso)'''+ '''VALUES (%(name)s,%(apellido)s,%(edad)s,%(seccion)s,%(curso)s)''',{'name':'Tamara','apellido':'Lujan','edad':76,'seccion':'F','curso':'Computacion'})

data = {'name' : 'Franchesco','apellido':'Espinoza','edad':67,'seccion':'G','curso':'Ciencia y Tecnologia'}    
lugar = 'INSERT INTO profesor(name,apellido,edad,seccion,curso) VALUES (%(name)s,%(apellido)s,%(edad)s,%(seccion)s,%(curso)s);'
cursor.execute(lugar,data)
data = {'name' : 'Gustavo','apellido':'Gomez','edad':25,'seccion':'H','curso':'Comunicacion'}    
lugar = 'INSERT INTO profesor(name,apellido,edad,seccion,curso) VALUES (%(name)s,%(apellido)s,%(edad)s,%(seccion)s,%(curso)s);'
cursor.execute(lugar,data)
data = {'name' : 'Rachel','apellido':'Arteta','edad':30,'seccion':'I','curso':'Religion'}    
lugar = 'INSERT INTO profesor(name,apellido,edad,seccion,curso) VALUES (%(name)s,%(apellido)s,%(edad)s,%(seccion)s,%(curso)s);'
cursor.execute(lugar,data)
data = {'name' : 'Rodrigo','apellido':'Rodriguez','edad':45,'seccion':'J','curso':'Razonamiento Matematico'}    
lugar = 'INSERT INTO profesor(name,apellido,edad,seccion,curso) VALUES (%(name)s,%(apellido)s,%(edad)s,%(seccion)s,%(curso)s);'
cursor.execute(lugar,data)







cursor.execute('''INSERT INTO curso(name,duracion,profesor) VALUES('Historia','6 horas','Mauricio');''')
cursor.execute('''INSERT INTO curso(name,duracion,profesor) VALUES('Educacion Fisica','2 horas','Yuan');''')
cursor.execute('''INSERT INTO curso(name,duracion,profesor) VALUES('Matematica','6 horas','Judith');''')

cursor.execute('''INSERT INTO curso(name,duracion,profesor) VALUES(%s,%s,%s); ''',('Taller Deportivo','2 horas','Diego',))
cursor.execute('''INSERT INTO curso(name,duracion,profesor)'''+ '''VALUES (%(name)s,%(duracion)s,%(profesor)s)''',{'name':'Arte','duracion':'2 horas','profesor':'Sebastian'})
cursor.execute('''INSERT INTO curso(name,duracion,profesor)'''+ '''VALUES (%(name)s,%(duracion)s,%(profesor)s)''',{'name':'Computacion','duracion':'2 horas','profesor':'Tamara'})

data = {'name' : 'Ciencia y Tecnologia','duracion':'6 horas','profesor':'Franchesco'}    
lugar = 'INSERT INTO curso(name,duracion,profesor) VALUES (%(name)s,%(duracion)s,%(profesor)s);'
cursor.execute(lugar,data)
data = {'name' : 'Comunicacion','duracion':'6 horas','profesor':'Gustavo'}    
lugar = 'INSERT INTO curso(name,duracion,profesor) VALUES (%(name)s,%(duracion)s,%(profesor)s);'
cursor.execute(lugar,data)
data = {'name' : 'Religion','duracion':'2 horas','profesor':'Rachel'}    
lugar = 'INSERT INTO curso(name,duracion,profesor) VALUES (%(name)s,%(duracion)s,%(profesor)s);'
cursor.execute(lugar,data)
data = {'name' : 'Razonamiento Matematico','duracion':'3 horas','profesor':'Rodrigo'}    
lugar = 'INSERT INTO curso(name,duracion,profesor) VALUES (%(name)s,%(duracion)s,%(profesor)s);'
cursor.execute(lugar,data)




cursor.execute('''INSERT INTO seccion(name,alumno,profesor,curso) VALUES('A','Juan','Mauricio','Historia');''')
cursor.execute('''INSERT INTO seccion(name,alumno,profesor,curso) VALUES('B','Gustavo','Yuan','Educacion Fisica');''')
cursor.execute('''INSERT INTO seccion(name,alumno,profesor,curso) VALUES('C','Selena','Judith','Matematica');''')

cursor.execute('''INSERT INTO seccion(name,alumno,profesor,curso) VALUES(%s,%s,%s,%s); ''',('D','Diego','Diego','Taller Deportivo'))
cursor.execute('''INSERT INTO seccion(name,alumno,profesor,curso)'''+ '''VALUES (%(name)s,%(alumno)s,%(profesor)s,%(curso)s)''',{'name':'E','alumno':'Sebastian','profesor':'Sebastian','curso':'Arte'})
cursor.execute('''INSERT INTO seccion(name,alumno,profesor,curso)'''+ '''VALUES (%(name)s,%(alumno)s,%(profesor)s,%(curso)s)''',{'name':'F','alumno':'Tamara','profesor':'Tamara','curso':'Computacion'})

data = {'name' : 'G','alumno':'Francis','profesor':'Franchesco','curso':'Ciencia y Tecnologia'}    
lugar = 'INSERT INTO seccion(name,alumno,profesor,curso) VALUES (%(name)s,%(alumno)s,%(profesor)s,%(curso)s);'
cursor.execute(lugar,data)
data = {'name' : 'H','alumno':'Walter','profesor':'Gustavo','curso':'Comunicacion'}    
lugar = 'INSERT INTO seccion(name,alumno,profesor,curso) VALUES (%(name)s,%(alumno)s,%(profesor)s,%(curso)s);'
cursor.execute(lugar,data)
data = {'name' : 'I','alumno':'Pedro','profesor':'Rachel','curso':'Religion'}    
lugar = 'INSERT INTO seccion(name,alumno,profesor,curso) VALUES (%(name)s,%(alumno)s,%(profesor)s,%(curso)s);'
cursor.execute(lugar,data)
data = {'name' : 'J','alumno':'Rafael','profesor':'Rodrigo','curso':'Razonamiento Matematico'}    
lugar = 'INSERT INTO seccion(name,alumno,profesor,curso) VALUES (%(name)s,%(alumno)s,%(profesor)s,%(curso)s);'
cursor.execute(lugar,data)   

cursor.execute('select * from estudiante;')
result1 = cursor.fetchall() 
cursor.execute('select * from profesor;')
result2 = cursor.fetchall() 
cursor.execute('select * from curso;')
result3 = cursor.fetchall() 
cursor.execute('select * from seccion;')
result4 = cursor.fetchall() 

print('Estudiantes: ', result1)
print()
print('Profesores: ', result2)
print()
print('Cursos: ', result3)
print()
print('Secciones: ', result4)

connection.commit()
connection.close()
cursor.close()
