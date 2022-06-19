import pyodbc

server = 'localhost'
bd = 'BDProyect'

user = 'Richpoo'
passw = 'richmsr'

class registers():
    
    def __init__(self):
        self.cnn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='
        +server+';DATABASE='+bd+';UID='+user+';PWD='+passw)

    def __str__(self):
        datos = self.consultProys()
        aux =""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consultProys(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM proys")
        datos = cur.fetchall()
        cur.close()
        return datos

    def registerBoss(self, name, id, direc, phone):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO boss (boss_name, boss_id, boss_direc, boss_phone)
        VALUES('{}', '{}', '{}', '{}')'''.format(name, id, direc, phone)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def registerArqs(self, name, id, direc, phone):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO arqs (arq_name, arq_id, arq_direc, arq_phone)
        VALUES('{}', '{}', '{}', '{}')'''.format(name, id, direc, phone)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def registerPlanos(self, id, date, arqs):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO plans (pln_id, pln_date, id_arqs)
        VALUES('{}', '{}', '{}')'''.format(id, date, arqs)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def registerProys(self, id, name, status, boss, arqs, pln):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO proys (proy_id, proy_name, proy_status, id_boss, id_arq, id_pln)
        VALUES('{}', '{}', '{}', '{}','{}', '{}')'''.format(id, name, status, boss, arqs, pln)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def updateStatusproy(self, id, status):
        cur = self.cnn.cursor()
        sql = '''UPDATE proys SET proy_status = {} WHERE proy_id = {}'''.format(status,id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def deleteProy(self,id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM proys WHERE proy_id = {}'''.format(id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n