import pyodbc

server = 'localhost'
bd = 'BDProyect'

user = 'Richpoo'
passw = 'richmsr'

class registermeds():
    
    def __init__(self, id, name, height, weight, age, tipblood):
        self.cnn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='
        +server+';DATABASE='+bd+';UID='+user+';PWD='+passw)
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.tipblood = tipblood

    def consultMeds(self):
        cur = self.cnn.cursor()
        all = cur.execute("SELECT * FROM medicos").fetchall()
        personas = []
        for p in all:
            persona = registermeds(p[0],p[1],p[2], p[3], p[4], p[5])
            personas.append(persona)
        cur.close()
        return personas

    def registerMedico(self):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO medicos (id_med, nombre, altura, peso, edad, tipblood)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(self.id, self.name, self.height, self.weight, self.age, self.tipblood)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def deleteMed(self,id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM medicos WHERE id_med = {}'''.format(id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def __str__(self):
        return '{}: Nombre: {}, altura: {}, Peso: {}, Edad: {}, Tipo Sangre: {}'.format(self.id, self.name, self.height, self.weight, self.age, self.tipblood)