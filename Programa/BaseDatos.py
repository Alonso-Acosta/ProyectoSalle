import sys
import mysql.connector
from PySide6.QtWidgets import QTableWidgetItem

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="proyecto")
mycursor = mydb.cursor()
# INSERTAR DATOS EN BASE DE DATOS
sqlinstertUsuarios = "INSERT INTO t_usuarios (user,password,cedula,tipousuario,cod_estud,id_laboratorista) VALUES (%s,%s,%s,%s,%s,%s)"
sqlinstertLaboratorista = "INSERT INTO t_usuarios (id_laboratorista,cedula,nombres,apellidos,tel_fijo,celular,ciudad,fecha_nac,direccion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"


sqlinstertInstrumento = "INSERT INTO t_instrumento (id_instrumento,nombre,tipo_instr,tipo_practica,estado_instr,cod_seguridad,fecha_registro,fabricante,valor,id_banco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sqlinstertMaquina = "INSERT INTO t_maquina (id_maquina,nombre,tipo_maq,tipo_practica,fecha_registro,fabricante,valor,estado_maq) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
sqlinstertReparacion = "INSERT INTO t_reparacion (id_reparacion,fecha_ingreso,fecha_retorno,descripcion,id_laboratorista,id_maquina,id_instrumento) VALUES (%s,%s,%s,%s,%s,%s,%s)"

# CONSULTAR DATOS EN BASE DE DATOS
sqlselectUsuarios = "SELECT * FROM t_usuarios WHERE user = %s"
sqlselectLaboratorista = "SELECT * FROM t_laboratorista WHERE id_laboratorista = %s"

sqlselectInstrumento = "SELECT * FROM t_instrumento "
sqlselectInstrumentoID = "SELECT * FROM t_instrumento WHERE id_instrumento = %s"
sqlselectInstrumentoNombre = "SELECT * FROM t_instrumento WHERE nombre = %s"
sqlselectInstrumentoTipo = "SELECT * FROM t_instrumento WHERE tipo_instr = %s"

sqlselectMaquina = "SELECT * FROM t_maquina "
sqlselectMaquinaID = "SELECT * FROM t_maquina WHERE id_maquina = %s"
sqlselectMaquinaNombre = "SELECT * FROM t_maquina WHERE nombre = %s"
sqlselectMaquinaTipo = "SELECT * FROM t_maquina WHERE tipo_maq = %s"

sqlselectReparacion = "SELECT * FROM t_reparacion"
sqlselectReparacionID = "SELECT * FROM t_reparacion WHERE id_reparacion = %s"
sqlselectReparacionIDInstru = "SELECT * FROM t_reparacion WHERE id_instrumento = %s"
sqlselectReparacionIDMaq = "SELECT * FROM t_reparacion WHERE id_maquina = %s"

# MODIFICAR DATOS EN BASE DE DATOS
sqlupdateInstrumento = "UPDATE t_instrumento SET nombre = %s,tipo_instr = %s,tipo_practica = %s,estado_instr = %s,cod_seguridad = %s,fecha_registro = %s,fabricante = %s,valor = %s,id_banco = %s WHERE id_instrumento = %s"
sqlupdateMaquina = "UPDATE t_maquina SET nombre = %s, tipo_maq = %s,tipo_practica = %s, fecha_registro = %s, fabricante = %s, valor = %s, estado_maq = %s WHERE id_maquina = %s"
sqlupdateReparacion = "UPDATE t_reparacion SET fecha_ingreso = %s, fecha_retorno = %s,descripcion = %s, id_laboratorista = %s,id_maquina = %s,id_instumento = %s WHERE id_reparacion = %s"

# ELIMINAR DATOS EN BASE DE DATOS
sqlDeleteInstrumento = "DELETE FROM t_instrumento WHERE id_instrumento = %s"
sqlDeleteMaquina = "DELETE FROM t_maquina WHERE id_maquina = %s"
sqlDeleteReparacion = "DELETE FROM t_reparacion WHERE id_reparacion = %s"

#val = ("45161004","126304","Miguel","Rojas","917508","321225461","Sincelejo","2000/10/15","calle walabi 4 2 sydni",)
#mycursor.execute(sqlinstertLaboratorista,val)
#mydb.commit()

class Instrumento:
    def agregar(val):
        mycursor.execute(sqlinstertInstrumento, val)
        mydb.commit()

    def ConsultarTablaInstrumento(self):
        mycursor.execute(sqlselectInstrumento)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaID(adr):
        mycursor.execute(sqlselectInstrumentoID, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaNombre(adr):
        mycursor.execute(sqlselectInstrumentoNombre, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaTIpo(adr):
        mycursor.execute(sqlselectInstrumentoTipo, adr)
        myresult = mycursor.fetchall()
        return myresult

    def Actualizar(val):
        mycursor.execute(sqlupdateInstrumento, val)
        mydb.commit()
        print(mycursor.rowcount, "registros afectado/s")

    def Eliminar(val):
        mycursor.execute(sqlDeleteInstrumento, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")


class Maquina:
    def agregar(val):
        mycursor.execute(sqlinstertMaquina, val)
        mydb.commit()

    def ConsultaID(adr):
        mycursor.execute(sqlselectMaquinaID, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaNombre(adr):
        mycursor.execute(sqlselectMaquinaNombre, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaTipo(adr):
        mycursor.execute(sqlselectMaquinaTipo, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultarTablaMaquina(self):
        mycursor.execute(sqlselectMaquina)
        myresult = mycursor.fetchall()
        return myresult

    def Actualizar(val):
        mycursor.execute(sqlupdateMaquina, val)
        mydb.commit()
        print(mycursor.rowcount, "registros afectado/s")

    def Eliminar(val):
        mycursor.execute(sqlDeleteMaquina, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")


class Reparacion:
    def agregar(val):
        mycursor.execute(sqlinstertReparacion,val)
        mydb.commit()

    def ConsultaID(adr):
        mycursor.execute(sqlselectReparacionID, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaIDInstrumento(adr):
        mycursor.execute(sqlselectReparacionIDInstru, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaIDMaquina(adr):
        mycursor.execute(sqlselectReparacionIDMaq, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultarTablaReparacion(self):
        mycursor.execute(sqlselectReparacion)
        myresult = mycursor.fetchall()
        return myresult

    def Actualizar(val):
        mycursor.execute(sqlupdateReparacion, val)
        mydb.commit()

    def Eliminar(val):
        mycursor.execute(sqlDeleteReparacion, val)
        mydb.commit()


class metodos:
    def convertTuple(tup):
        str = ''.join(tup)
        return str

    def ConsultaIDLaboratorista(adr):
        mycursor.execute(sqlselectLaboratorista, adr)
        myresult = mycursor.fetchall()
        return myresult

    def LoadDataTabla1(self):
        data = Instrumento.ConsultarTablaInstrumento(self)
        fila = 0
        self.TInstrumento.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            fecha = "{}".format(num[6])
            valor = "$ {}".format(num[8])
            self.TInstrumento.setItem(fila, 0, QTableWidgetItem(num[0]))
            self.TInstrumento.setItem(fila, 1, QTableWidgetItem(num[1]))
            self.TInstrumento.setItem(fila, 2, QTableWidgetItem(num[2]))
            self.TInstrumento.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TInstrumento.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TInstrumento.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TInstrumento.setItem(fila, 6, QTableWidgetItem(fecha))
            self.TInstrumento.setItem(fila, 7, QTableWidgetItem(num[7]))
            self.TInstrumento.setItem(fila, 8, QTableWidgetItem(valor))
            fila += 1

    def ConsultaDataTabla1(self,val,aux):
        if aux in "ID":
            data = Instrumento.ConsultaID(val)
        if aux in "NOMBRE":
            data = Instrumento.ConsultaNombre(val)
        if aux in "TIPO":
            data = Instrumento.ConsultaTIpo(val)
        fila = 0
        self.TConsultaInstrumento.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            fecha = "{}".format(num[6])
            valor = "$ {}".format(num[8])
            self.TConsultaInstrumento.setItem(fila, 0, QTableWidgetItem(num[0]))
            self.TConsultaInstrumento.setItem(fila, 1, QTableWidgetItem(num[1]))
            self.TConsultaInstrumento.setItem(fila, 2, QTableWidgetItem(num[2]))
            self.TConsultaInstrumento.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TConsultaInstrumento.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TConsultaInstrumento.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TConsultaInstrumento.setItem(fila, 6, QTableWidgetItem(fecha))
            self.TConsultaInstrumento.setItem(fila, 7, QTableWidgetItem(num[7]))
            self.TConsultaInstrumento.setItem(fila, 8, QTableWidgetItem(valor))
            fila += 1
    def LoadDataTabla2(self):
        data = Maquina.ConsultarTablaMaquina(self)
        fila = 0
        self.TMaquina.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            fecha = "{}".format(num[4])
            valor = "$ {}".format(num[6])
            self.TMaquina.setItem(fila, 0, QTableWidgetItem(num[0]))
            self.TMaquina.setItem(fila, 1, QTableWidgetItem(num[1]))
            self.TMaquina.setItem(fila, 2, QTableWidgetItem(num[2]))
            self.TMaquina.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TMaquina.setItem(fila, 4, QTableWidgetItem(fecha))
            self.TMaquina.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TMaquina.setItem(fila, 6, QTableWidgetItem(valor))
            self.TMaquina.setItem(fila, 7, QTableWidgetItem(num[7]))
            fila += 1
    def ConsultaDataTabla2(self,val,aux):
        if aux in "ID":
            data = Maquina.ConsultaID(val)
        if aux in "NOMBRE":
            data = Maquina.ConsultaNombre(val)
        if aux in "TIPO":
            data = Maquina.ConsultaTipo(val)
        print(data)
        fila = 0
        self.TConsultaMaquina.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            fecha = "{}".format(num[4])
            valor = "$ {}".format(num[6])
            self.TConsultaMaquina.setItem(fila, 0, QTableWidgetItem(num[0]))
            self.TConsultaMaquina.setItem(fila, 1, QTableWidgetItem(num[1]))
            self.TConsultaMaquina.setItem(fila, 2, QTableWidgetItem(num[2]))
            self.TConsultaMaquina.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TConsultaMaquina.setItem(fila, 4, QTableWidgetItem(fecha))
            self.TConsultaMaquina.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TConsultaMaquina.setItem(fila, 6, QTableWidgetItem(valor))
            self.TConsultaMaquina.setItem(fila, 7, QTableWidgetItem(num[7]))
            fila += 1
    def LoadDataTabla3(self):
        data = Reparacion.ConsultarTablaReparacion(self)
        fila = 0
        self.TInstrumentoReparacion.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            aux = "{}".format(num[0])
            fecha1 = "{}".format(num[1])
            fecha2 = "$ {}".format(num[2])
            self.TInstrumentoReparacion.setItem(fila, 0, QTableWidgetItem(aux))
            self.TInstrumentoReparacion.setItem(fila, 1, QTableWidgetItem(fecha1))
            self.TInstrumentoReparacion.setItem(fila, 2, QTableWidgetItem(fecha2))
            self.TInstrumentoReparacion.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TInstrumentoReparacion.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TInstrumentoReparacion.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TInstrumentoReparacion.setItem(fila, 6, QTableWidgetItem(num[6]))
            fila += 1
    def ConsultaDataTabla3(self,val,aux):
        if aux in "ID":
            data = Reparacion.ConsultaID(val)
        if aux in "ID LABORATORISTA":
            data = Reparacion.ConsultaIDInstrumento(val)
        if aux in "ID MAQUINA":
            data = Reparacion.ConsultaIDMaquina(val)
        fila = 0
        self.TConsultaInstrumentoReparacion.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            aux = "{}".format(num[0])
            fecha1 = "{}".format(num[1])
            fecha2 = "$ {}".format(num[2])
            self.TConsultaInstrumentoReparacion.setItem(fila, 0, QTableWidgetItem(aux))
            self.TConsultaInstrumentoReparacion.setItem(fila, 1, QTableWidgetItem(fecha1))
            self.TConsultaInstrumentoReparacion.setItem(fila, 2, QTableWidgetItem(fecha2))
            self.TConsultaInstrumentoReparacion.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TConsultaInstrumentoReparacion.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TConsultaInstrumentoReparacion.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TConsultaInstrumentoReparacion.setItem(fila, 6, QTableWidgetItem(num[6]))
            fila += 1


class IniciarSesion:
    def Verificar(usua, contra):
        mycursor.execute(sqlselectUsuarios, (usua,))
        myresult = mycursor.fetchall()
        usuaa = metodos.convertTuple(usua)
        contraa = metodos.convertTuple(contra)
        usuaB = " "
        contraB = " "
        for row in myresult:
            usuaB = row[0]
            contraB = row[1]
        if usuaa in usuaB:
            if contraB in contraa:
                return True
            else:
                print("contra F")
                return False
        else:
            print("F usua")
        return False



