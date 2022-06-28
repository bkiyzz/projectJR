import pyodbc

server = 'localhost'
bd = 'BDProyect'

user = 'Richpoo'
passw = 'richmsr'

cnn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='
        +server+';DATABASE='+bd+';UID='+user+';PWD='+passw)


class registerpac():

    def __init__(self, id, name, height, weight, age, tipblood, enfermedad, fecha, presion, IMS, medid):
        self.cnn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='
        +server+';DATABASE='+bd+';UID='+user+';PWD='+passw)
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.tipblood = tipblood
        self.enfermedad = enfermedad
        self.fecha = fecha
        self.presion = presion
        self.IMS = IMS
        #self.enftoreport = '''INSERT INTO reportes SELECT'''
        self.medid = medid

    @staticmethod
    def consultPac():
        cnn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='
        +server+';DATABASE='+bd+';UID='+user+';PWD='+passw)
        cur = cnn.cursor()
        all = cur.execute("SELECT * FROM pacientes").fetchall()
        pacientes = []
        for p in all:
            persona = registerpac(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7],p[8],p[9],p[10])
            pacientes.append(persona)
        cur.close()
        return pacientes

    def registerpaciente(self):
        cur = cnn.cursor()
        sql = '''INSERT INTO pacientes (id_paciente, nombre_pac, altura, peso, edad, tipblood, enfermedad, fecha, presion, IMS, med_id)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}','{}')'''.format(self.id, self.name, self.height, self.weight, self.age, self.tipblood, self.enfermedad, self.fecha, self.presion, self.IMS, self.medid)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def makeReports(self, id, medid, pacid, enf):
        cur = cnn.cursor()
        sql = '''INSERT INTO reportes (id_report, med_id, paciente_id, enf)
        VALUES('{}', '{}', '{}','{}')'''.format(id, medid, pacid, enf)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def updatedPac(self):
        cur = self.cnn.cursor()
        sql = '''UPDATE pacientes SET nombre_pac = {}, altura = {}, peso = {}, edad = {}, tipblood = {}, enfermedad = {}, fecha = {}, presion = {}, IMS = {}, med_id = {} WHERE id_paciente = {}'''.format(self.name, self.height, self.weight, self.age, self.tipblood, self.enfermedad, self.fecha, self.presion, self.IMS, self.medid, self.id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit
        cur.close

    def deletePac(self):
        if self.id != 0:
            cur = self.cnn.cursor()
            sql = '''DELETE FROM pacientes WHERE id_paciente = {}'''.format(self.id)
            cur.execute(sql)
            n = cur.rowcount
            self.cnn.commit()
            cur.close()
        return n

    def __str__(self):
        return '{}: Nombre: {}, altura: {}, Peso: {}, Edad: {}, Tipo Sangre: {}, Enfermedad: {} ,Medico Asignado: {}'.format(self.id, self.name, self.height, self.weight, self.age, self.tipblood, self.enfermedad, self.medid)