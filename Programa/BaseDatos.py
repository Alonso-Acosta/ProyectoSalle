import sys
import mysql.connector
from PySide6.QtWidgets import QTableWidgetItem, QFileDialog,QPushButton, QHBoxLayout, QFrame, QAbstractItemView
from PySide6.QtGui import QIcon, QCursor, QPixmap
from PySide6.QtCore import  Qt

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="proyecto")
mycursor = mydb.cursor()
# INSERTAR DATOS EN BASE DE DATOS
sqlinstertUsuarios = "INSERT INTO t_usuarios (user,password,cedula,tipousuario,cod_estud,id_laboratorista) VALUES (%s,%s,%s,%s,%s,%s)"
sqlinstertLaboratorista = "INSERT INTO t_usuarios (id_laboratorista,cedula,nombres,apellidos,tel_fijo,celular,ciudad,fecha_nac,direccion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

sqlinstertPlanM = "INSERT INTO t_planm (laboratorio,codigo_equipo,nombre,vida_util,calibracion,frec_mantenimiento,ultimoM,proximoM,pronostico1,pronostico2,pronostico3,pronostico4,pronostico5,pronostico6,pronostico7,observaciones) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sqlinstertEquipo =  "INSERT INTO t_equipo (id_equipo,nombre,vida_util,frec_mantenimiento,estado_equipo,codigo_equipo,fecha_registro,fabricante,laboratorio,calibracion,valor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sqlinstertReparacion = "INSERT INTO t_reparacion (id_reparacion,fecha_ingreso,fecha_retorno,descripcion,id_laboratorista,id_maquina,id_instrumento) VALUES (%s,%s,%s,%s,%s,%s,%s)"
sqlinstertProveedores = "INSERT INTO t_proveedores (id_proveedor,FechaDiligenciamiento,RazonSocial,Nit,Telefonos,Email,Direccion,Fax,Ciudad,ContactoVentas,ContactoSoporte,PDFProveedor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sqlinstertMantenimientosEnCurso = "INSERT INTO t_mantenimientosencurso (id,fecha_registro,fecha_retorno,observaciones,id_laboratorista,id_equipo,id_proveedor,costo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
sqlinstertMantenimientosRealizado = "INSERT INTO t_mantenimientorealizado (id,fecha_registro,fecha_retorno,observaciones,id_laboratorista,id_equipo,id_proveedor,costo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
sqlinstertNoficaciones = "INSERT INTO t_notificaciones (tipo_noti,codigo_equipo,nombre_equipo) VALUES (%s,%s,%s)"



# CONSULTAR DATOS EN BASE DE DATOS
sqlselectUsuarios = "SELECT * FROM t_usuarios WHERE user = %s"
sqlselectLaboratorista = "SELECT * FROM t_laboratorista WHERE id_laboratorista = %s"

sqlselectNoficaciones = "SELECT * FROM t_notificaciones "
sqlselectNoficacionesCodigoEquipo = "SELECT * FROM t_notificaciones WHERE codigo_equipo = %s"
sqlselectNoficacionesId = "SELECT * FROM tt_notificaciones WHERE id = %s"

sqlselectEquipo = "SELECT * FROM t_equipo "
sqlselectEquipoID = "SELECT * FROM t_equipo WHERE id_equipo = %s"
sqlselectEquipoNombre = "SELECT * FROM t_equipo WHERE nombre = %s"
sqlselectEquipoCodigo = "SELECT * FROM t_equipo WHERE codigo_equipo = %s"

sqlselectPlanM = "SELECT * FROM t_planm "
sqlselectPlanMLaboratorio = "SELECT * FROM t_planm WHERE laboratorio = %s"
sqlselectPlanMNombre = "SELECT * FROM t_planm WHERE nombre = %s"
sqlselectPlanMCodigo = "SELECT * FROM t_planm WHERE codigo_equipo = %s"

sqlselectMantenimientosEnCurso = "SELECT * FROM t_mantenimientosencurso "
sqlselectMantenimientosEnCursoID = "SELECT * FROM t_mantenimientosencurso WHERE id = %s"
sqlselectMantenimientosEnCursoIDProveedor = "SELECT * FROM t_mantenimientosencurso WHERE id_proveedor = %s"
sqlselectMantenimientosEnCursoIDLaboratorista = "SELECT * FROM t_mantenimientosencurso WHERE id_laboratorista = %s"
sqlselectMantenimientosEnCursoIDEquipo = "SELECT * FROM t_mantenimientosencurso WHERE id_equipo = %s"

sqlselectMantenimientosRealizado = "SELECT * FROM t_mantenimientorealizado "
sqlselectMantenimientosRealizadoID = "SELECT * FROM t_mantenimientorealizado WHERE id = %s"
sqlselectMantenimientosRealizadoIDProveedor = "SELECT * FROM t_mantenimientorealizado WHERE id_proveedor = %s"
sqlselectMantenimientosRealizadoIDLaboratorista = "SELECT * FROM t_mantenimientorealizado WHERE id_laboratorista = %s"
sqlselectMantenimientosRealizadoIDEquipo = "SELECT * FROM t_mantenimientorealizado WHERE id_equipo = %s"




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

sqlselectProveedores = "SELECT * FROM t_proveedores"
sqlselectProveedoresID = "SELECT * FROM t_proveedores WHERE id_proveedor = %s"
sqlselectProveedoresRazonSocial = "SELECT * FROM t_proveedores WHERE RazonSocial = %s"
sqlselectProveedoresNit = "SELECT * FROM t_proveedores WHERE Nit = %s"



# MODIFICAR DATOS EN BASE DE DATOS

sqlupdateEquipo = "UPDATE t_equipo SET nombre = %s,	vida_util = %s,frec_mantenimiento = %s,estado_equipo = %s,codigo_equipo = %s,fecha_registro = %s,fabricante = %s,laboratorio = %s,calibracion = %s,valor = %s WHERE id_equipo = %s"
sqlupdatePlanM = "UPDATE t_planm SET laboratorio = %s, nombre = %s,	vida_util = %s,calibracion = %s,frec_mantenimiento = %s,ultimoM = %s, proximoM = %s, pronostico1 = %s,pronostico2 = %s,pronostico3 = %s,pronostico4 = %s,pronostico5 = %s,pronostico6 = %s,pronostico7 = %s, observaciones = %s  WHERE codigo_equipo = %s"
sqlupdateMantenimientosEnCurso = "UPDATE t_mantenimientosencurso SET fecha_registro = %s,	fecha_retorno = %s,observaciones = %s,id_laboratorista = %s,id_equipo = %s, id_proveedor = %s, costo = %s  WHERE id = %s"
sqlupdateMantenimientosRealizado = "UPDATE t_mantenimientorealizado SET fecha_registro = %s,	fecha_retorno = %s,observaciones = %s,id_laboratorista = %s,id_equipo = %s, id_proveedor = %s, costo = %s  WHERE id = %s"
sqlupdateNoficaciones = "UPDATE t_notificaciones SET tipo_noti = %s, codigo_equipo=%s, nombre_equipo=%s WHERE id = %s"


sqlupdateInstrumento = "UPDATE t_instrumento SET nombre = %s,tipo_instr = %s,tipo_practica = %s,estado_instr = %s,cod_seguridad = %s,fecha_registro = %s,fabricante = %s,valor = %s,id_banco = %s WHERE id_instrumento = %s"
sqlupdateMaquina = "UPDATE t_maquina SET nombre = %s, tipo_maq = %s,tipo_practica = %s, fecha_registro = %s, fabricante = %s, valor = %s, estado_maq = %s WHERE id_maquina = %s"
sqlupdateReparacion = "UPDATE t_reparacion SET fecha_ingreso = %s, fecha_retorno = %s,descripcion = %s, id_laboratorista = %s,id_maquina = %s,id_instumento = %s WHERE id_reparacion = %s"
sqlupdateProveedores = "UPDATE t_proveedores SET FechaDiligenciamiento = %s, RazonSocial = %s,Nit = %s, Telefonos = %s,Email = %s,Direccion = %s,Fax = %s,Ciudad = %s,ContactoVentas = %s,ContactoSoporte = %s,PDFProveedor = %s WHERE id_proveedor = %s"




# ELIMINAR DATOS EN BASE DE DATOS
sqlDeleteEquipo = "DELETE FROM t_equipo WHERE id_equipo = %s"
sqlDeletePlanM = "DELETE FROM t_planm WHERE codigo_equipo = %s"
sqlDeleteMantenimientosRealizado = "DELETE FROM t_mantenimientorealizado WHERE id = %s"
sqlDeleteMantenimientosRealizadoIDEquipo = "DELETE FROM t_mantenimientorealizado WHERE id_equipo = %s"
sqlDeleteMantenimientosRealizadoIDProveedores = "DELETE FROM t_mantenimientorealizado WHERE id_proveedor = %s"
sqlDeleteMantenimientosEnCurso = "DELETE FROM t_mantenimientosencurso WHERE id = %s"
sqlDeleteMantenimientosEnCursoIDEquipo = "DELETE FROM t_mantenimientosencurso WHERE id_equipo = %s"
sqlDeleteMantenimientosEnCursoIDProveedores = "DELETE FROM t_mantenimientosencurso WHERE id_proveedor = %s"
sqlDeleteNotificaciones = "DELETE FROM t_notificaciones WHERE id = %s"


sqlDeleteInstrumento = "DELETE FROM t_instrumento WHERE id_instrumento = %s"
sqlDeleteMaquina = "DELETE FROM t_maquina WHERE id_maquina = %s"
sqlDeleteReparacion = "DELETE FROM t_reparacion WHERE id_reparacion = %s"
sqlDeleteProveedor = "DELETE FROM t_proveedores WHERE id_proveedor = %s"


#val = ("45161004","126304","Miguel","Rojas","917508","321225461","Sincelejo","2000/10/15","calle walabi 4 2 sydni",)
#mycursor.execute(sqlinstertLaboratorista,val)
#mydb.commit()
class Notificaciones:
    def agregar(val):
        mycursor.execute(sqlinstertNoficaciones, val)
        mydb.commit()

    def ConsultarTablaNotifiaciones(self):
        mycursor.execute(sqlselectNoficaciones)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaID(adr):
        mycursor.execute(sqlselectNoficacionesId, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaCodigo(adr):
        mycursor.execute(sqlselectNoficacionesCodigoEquipo, adr)
        myresult = mycursor.fetchall()
        return myresult

    def Actualizar(val):
        mycursor.execute(sqlupdateNoficaciones, val)
        mydb.commit()
        print(mycursor.rowcount, "registros afectado/s")

    def Eliminar(val):
        mycursor.execute(sqlDeleteNotificaciones, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")


class Equipo:
    def agregar(val):
        mycursor.execute(sqlinstertEquipo, val)
        mydb.commit()

    def ConsultarTablaEquipo(self):
        mycursor.execute(sqlselectEquipo)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaID(adr):
        mycursor.execute(sqlselectEquipoID, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaNombre(adr):
        mycursor.execute(sqlselectEquipoNombre, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaCodigo(adr):
        mycursor.execute(sqlselectEquipoCodigo, adr)
        myresult = mycursor.fetchall()
        return myresult

    def Actualizar(val):
        mycursor.execute(sqlupdateEquipo, val)
        mydb.commit()
        print(mycursor.rowcount, "registros afectado/s")

    def Eliminar(val):
        mycursor.execute(sqlDeleteEquipo, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")

class PlanM:
    def agregar(val):
        mycursor.execute(sqlinstertPlanM, val)
        mydb.commit()

    def ConsultarTablaPlanM(self):
        mycursor.execute(sqlselectPlanM)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaLaboratorio(adr):
        mycursor.execute(sqlselectPlanMLaboratorio, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaNombre(adr):
        mycursor.execute(sqlselectPlanMNombre, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaCodigo(adr):
        mycursor.execute(sqlselectPlanMCodigo, adr)
        myresult = mycursor.fetchall()
        return myresult

    def Actualizar(val):
        mycursor.execute(sqlupdatePlanM, val)
        mydb.commit()

    def Eliminar(val):
        mycursor.execute(sqlDeletePlanM, val)
        mydb.commit()

class MantenimientosEnCurso:
    def agregar(val):
        mycursor.execute(sqlinstertMantenimientosEnCurso, val)
        mydb.commit()

    def ConsultarTablaMantenimientosEnCurso(self):
        mycursor.execute(sqlselectMantenimientosEnCurso)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaId(adr):
        mycursor.execute(sqlselectMantenimientosEnCursoID, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaIdLaboratorista(adr):
        mycursor.execute(sqlselectMantenimientosEnCursoIDLaboratorista, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaIdProveedor(adr):
        mycursor.execute(sqlselectMantenimientosEnCursoIDProveedor, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaIdEquipo(adr):
        mycursor.execute(sqlselectMantenimientosEnCursoIDEquipo, adr)
        myresult = mycursor.fetchall()
        return myresult

    def Actualizar(val):
        mycursor.execute(sqlupdateMantenimientosEnCurso, val)
        mydb.commit()

    def Eliminar(val):
        mycursor.execute(sqlDeleteMantenimientosEnCurso, val)
        mydb.commit()

    def EliminarEquipos(val,self):
        A = MantenimientosEnCurso.ConsultarTablaMantenimientosEnCurso(self)
        for num in A:
            if num[5] == val[0]:
                mycursor.execute(sqlDeleteMantenimientosEnCursoIDEquipo, val)
                mydb.commit()

    def EliminarProveedores(val,self):
        A = MantenimientosEnCurso.ConsultarTablaMantenimientosEnCurso(self)
        for num in A:
            if num[6] == val[0]:
                mycursor.execute(sqlDeleteMantenimientosEnCursoIDProveedores, val)
                mydb.commit()


class MantenimientosRealizado:
    def agregar(val):
        mycursor.execute(sqlinstertMantenimientosRealizado, val)
        mydb.commit()

    def ConsultarTablaMantenimientosRealizado(self):
        mycursor.execute(sqlselectMantenimientosRealizado)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaId(adr):
        mycursor.execute(sqlselectMantenimientosRealizadoID, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaIdLaboratorista(adr):
        mycursor.execute(sqlselectMantenimientosRealizadoIDLaboratorista, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaIdProveedor(adr):
        mycursor.execute(sqlselectMantenimientosRealizadoIDProveedor, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaIdEquipo(adr):
        mycursor.execute(sqlselectMantenimientosRealizadoIDEquipo, adr)
        myresult = mycursor.fetchall()
        return myresult

    def Actualizar(val):
        mycursor.execute(sqlupdateMantenimientosRealizado, val)
        mydb.commit()

    def Eliminar(val):
        mycursor.execute(sqlDeleteMantenimientosRealizado, val)
        mydb.commit()

    def EliminarEquipos(val,self):
        A = MantenimientosRealizado.ConsultarTablaMantenimientosRealizado(self)
        for num in A:
            if num[5] == val:
                mycursor.execute(sqlDeleteMantenimientosRealizadoIDEquipo, val)
                mydb.commit()

    def EliminarProveedores(val,self):
        A = MantenimientosRealizado.ConsultarTablaMantenimientosRealizado(self)
        for num in A:
            if num[6] == val:
                mycursor.execute(sqlDeleteMantenimientosRealizadoIDEquipo, val)
                mydb.commit()

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

class Proveedores:
    def agregar(val):
        mycursor.execute(sqlinstertProveedores,val)
        mydb.commit()

    def ConsultaID(adr):
        mycursor.execute(sqlselectProveedoresID, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaNit(adr):
        mycursor.execute(sqlselectProveedoresNit, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultaRazonSocial(adr):
        mycursor.execute(sqlselectProveedoresRazonSocial, adr)
        myresult = mycursor.fetchall()
        return myresult

    def ConsultarTablaProvedor(self):
        mycursor.execute(sqlselectProveedores)
        myresult = mycursor.fetchall()
        return myresult

    def Actualizar(val):
        mycursor.execute(sqlupdateProveedores, val)
        print(val)
        mydb.commit()

    def Eliminar(val):
        mycursor.execute(sqlDeleteProveedor, val)
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
        data = Equipo.ConsultarTablaEquipo(self)
        fila = 0
        self.Tequipos.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            fecha = "{}".format(num[6])
            valor = "$ {}".format(num[10])
            self.Tequipos.setItem(fila, 0, QTableWidgetItem(num[0]))
            self.Tequipos.setItem(fila, 1, QTableWidgetItem(num[1]))
            self.Tequipos.setItem(fila, 2, QTableWidgetItem(num[2]))
            self.Tequipos.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.Tequipos.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.Tequipos.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.Tequipos.setItem(fila, 6, QTableWidgetItem(fecha))
            self.Tequipos.setItem(fila, 7, QTableWidgetItem(num[7]))
            self.Tequipos.setItem(fila, 8, QTableWidgetItem(num[8]))
            self.Tequipos.setItem(fila, 9, QTableWidgetItem(num[9]))
            self.Tequipos.setItem(fila, 10, QTableWidgetItem(valor))
            fila += 1
        self.Tequipos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Tequipos.setSelectionMode(QAbstractItemView.SingleSelection)


    def ConsultaDataTabla1(self,val,aux):
        if aux in "ID":
            data = Equipo.ConsultaID(val)
        if aux in "NOMBRE":
            data = Equipo.ConsultaNombre(val)
        if aux in "CODIGO":
            data = Equipo.ConsultaCodigo(val)
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
        self.TConsultaInstrumento.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TConsultaInstrumento.setSelectionMode(QAbstractItemView.SingleSelection)


    def LoadDataTablaNotificaciones(self):
        data = Notificaciones.ConsultarTablaNotifiaciones(self)
        fila = 0
        self.TNotifi.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            Estatus = num[1]
            codigoEquipo = num[2]
            nombre = num[3]
            salida = f"Estatus: {Estatus} Codigo Del Equipo:{codigoEquipo}  Mensaje: Enviar el {nombre} a Mantenimiento Correctivo"
            self.TNotifi.setItem(fila, 0, QTableWidgetItem(salida))
            fila += 1
        self.TNotifi.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TNotifi.setSelectionMode(QAbstractItemView.SingleSelection)


    """def ConsultaDataTabla2(self,val,aux):
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
        self.TConsultaMaquina.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TConsultaMaquina.setSelectionMode(QAbstractItemView.SingleSelection)
"""

    def LoadDataTabla3(self):
        data = MantenimientosEnCurso.ConsultarTablaMantenimientosEnCurso(self)
        fila = 0
        self.TMantenimientosEnCurso.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            aux = "{}".format(num[0])
            fecha1 = "{}".format(num[1])
            fecha2 = "{}".format(num[2])
            self.TMantenimientosEnCurso.setItem(fila, 0, QTableWidgetItem(aux))
            self.TMantenimientosEnCurso.setItem(fila, 1, QTableWidgetItem(fecha1))
            self.TMantenimientosEnCurso.setItem(fila, 2, QTableWidgetItem(fecha2))
            self.TMantenimientosEnCurso.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TMantenimientosEnCurso.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TMantenimientosEnCurso.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TMantenimientosEnCurso.setItem(fila, 6, QTableWidgetItem(num[6]))
            self.TMantenimientosEnCurso.setItem(fila, 7, QTableWidgetItem(num[7]))
            fila += 1
        self.TMantenimientosEnCurso.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TMantenimientosEnCurso.setSelectionMode(QAbstractItemView.SingleSelection)

    def LoadDataTablaMantenimientosRealizados(self):
        data = MantenimientosRealizado.ConsultarTablaMantenimientosRealizado(self)
        fila = 0
        self.TManteniR.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            aux = "{}".format(num[0])
            fecha1 = "{}".format(num[1])
            fecha2 = "{}".format(num[2])
            self.TManteniR.setItem(fila, 0, QTableWidgetItem(aux))
            self.TManteniR.setItem(fila, 1, QTableWidgetItem(fecha1))
            self.TManteniR.setItem(fila, 2, QTableWidgetItem(fecha2))
            self.TManteniR.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TManteniR.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TManteniR.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TManteniR.setItem(fila, 6, QTableWidgetItem(num[6]))
            self.TManteniR.setItem(fila, 7, QTableWidgetItem(num[7]))
            fila += 1
        self.TManteniR.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TManteniR.setSelectionMode(QAbstractItemView.SingleSelection)



    def ConsultaDataTabla3(self,val,aux):
        if aux in "ID":
            data = MantenimientosEnCurso.ConsultaId(val)
        if aux in "LABORATORISTA":
            data = MantenimientosEnCurso.ConsultaIdLaboratorista(val)

        if aux in "EQUIPO":
            data = MantenimientosEnCurso.ConsultaIdEquipo(val)

        if aux in "PROVEEDOR":
            data = MantenimientosEnCurso.ConsultaIdProveedor(val)

        fila = 0
        print(len(data))
        self.TConsultaMantenimientos1.setRowCount(len(data))
        # self.tableWidget.setColumnCount(9)
        for num in data:
            aux = "{}".format(num[0])
            fecha1 = "{}".format(num[1])
            fecha2 = "$ {}".format(num[2])
            self.TConsultaMantenimientos1.setItem(fila, 0, QTableWidgetItem(aux))
            self.TConsultaMantenimientos1.setItem(fila, 1, QTableWidgetItem(fecha1))
            self.TConsultaMantenimientos1.setItem(fila, 2, QTableWidgetItem(fecha2))
            self.TConsultaMantenimientos1.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TConsultaMantenimientos1.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TConsultaMantenimientos1.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TConsultaMantenimientos1.setItem(fila, 6, QTableWidgetItem(num[6]))
            self.TConsultaMantenimientos1.setItem(fila, 7, QTableWidgetItem(num[7]))
            fila += 1
        self.TConsultaMantenimientos1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TConsultaMantenimientos1.setSelectionMode(QAbstractItemView.SingleSelection)


    def LoadDataTablaProveedores(self):
        data = Proveedores.ConsultarTablaProvedor(self)
        fila = 0
        self.TProveedores.setRowCount(len(data))
        for num in data:
            fecha = "{}".format(num[1])
            self.TProveedores.setItem(fila, 0, QTableWidgetItem(num[0]))
            self.TProveedores.setItem(fila, 1, QTableWidgetItem(fecha))
            self.TProveedores.setItem(fila, 2, QTableWidgetItem(num[2]))
            self.TProveedores.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TProveedores.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TProveedores.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TProveedores.setItem(fila, 6, QTableWidgetItem(num[6]))
            self.TProveedores.setItem(fila, 7, QTableWidgetItem(num[7]))
            self.TProveedores.setItem(fila, 8, QTableWidgetItem(num[8]))
            self.TProveedores.setItem(fila, 9, QTableWidgetItem(num[9]))
            self.TProveedores.setItem(fila, 10, QTableWidgetItem(num[10]))
            self.TProveedores.setItem(fila, 11, QTableWidgetItem(num[11]))
            fila += 1
        self.TProveedores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TProveedores.setSelectionMode(QAbstractItemView.SingleSelection)


    def ConsultaDataTablaP(self,val,aux):
        if aux in "ID":
            data = Proveedores.ConsultaID(val)
            print(data)
        if aux in "NOMBRE":
            data = Proveedores.ConsultaRazonSocial(val)
        if aux in "NIT":
            data = Proveedores.ConsultaNit(val)
        fila = 0
        self.TConsultaProveedores.setRowCount(len(data))

        for num in data:
            fecha = "{}".format(num[1])
            self.TConsultaProveedores.setItem(fila, 0, QTableWidgetItem(num[0]))
            self.TConsultaProveedores.setItem(fila, 1, QTableWidgetItem(fecha))
            self.TConsultaProveedores.setItem(fila, 2, QTableWidgetItem(num[2]))
            self.TConsultaProveedores.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TConsultaProveedores.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TConsultaProveedores.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TConsultaProveedores.setItem(fila, 6, QTableWidgetItem(num[6]))
            self.TConsultaProveedores.setItem(fila, 7, QTableWidgetItem(num[7]))
            self.TConsultaProveedores.setItem(fila, 8, QTableWidgetItem(num[8]))
            self.TConsultaProveedores.setItem(fila, 9, QTableWidgetItem(num[9]))
            self.TConsultaProveedores.setItem(fila, 10, QTableWidgetItem(num[10]))
            self.TConsultaProveedores.setItem(fila, 11, QTableWidgetItem(num[11]))
            fila += 1
        self.TConsultaProveedores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TConsultaProveedores.setSelectionMode(QAbstractItemView.SingleSelection)
        self.TConsultaProveedores.selectionModel().selectionChanged.connect(self.seleccionar)




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



