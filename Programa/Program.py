from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from notifypy import Notify
from Login import Ui_Form1
from InterfazPrincipal import Ui_MainWindow
from DateTime import DateTime
import shutil, subprocess
import sys, BaseDatos
DB =BaseDatos
Noti = Notify()
FechaH = QDate(2022,10,13)
#FechaH = QDate(DateTime().year(),DateTime().month(),DateTime().day())
class MainWindow2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_10.clicked.connect(self.Notificaciones)

        self.pushButton_2.clicked.connect(self.MostrarRegistro)
        self.pushButton_3.clicked.connect(self.MostrarMantenimientos)
        self.pushButton_5.clicked.connect(self.MostrarProveedore)
        self.pushButton_7.clicked.connect(self.MostrarPlan)
        self.pushButton_71.clicked.connect(self.GenerarPlanM)
        self.pushButton.clicked.connect(self.Inicio)
        self.Wregistrar.setGeometry(0, 0, 1250,0)
        self.Wreparacion.setGeometry(0, 0, 1250, 0)
        self.Wproveedores.setGeometry(0, 0, 1250, 0)
        self.dateEdit_5.setDate(FechaH)
        self.dateEdit_6.setDate(FechaH)
        self.dateEdit_9.setDate(FechaH)
        self.FDiligenciamiento_2.setDate(FechaH)
        DB.metodos.LoadDataTablaNotificaciones(self)
        #"Inicializacion de registro"
        DB.metodos.LoadDataTabla1(self)
        #DB.metodos.LoadDataTabla2(self)

        self.pushButton_21.clicked.connect(self.Guardar1)
        self.pushButton_20.clicked.connect(self.Modificar1)
        self.pushButton_54.clicked.connect(self.Buscar1)
        self.pushButton_53.clicked.connect(self.Eliminar1)

        """self.pushButton_28.clicked.connect(self.Guardar2)
        self.pushButton_29.clicked.connect(self.Modificar2)
        self.pushButton_33.clicked.connect(self.Buscar2)
        self.pushButton_32.clicked.connect(self.Eliminar2)
        """
        self.comboBoxEstadoEquipo.addItem("BUENO")
        self.comboBoxEstadoEquipo.addItem("REGULAR")
        self.comboBoxEstadoEquipo.addItem("MALO")
        self.comboBoxEstadoEquipo.addItem("PARA REPARACION")

        self.comboBoxLaboratorio.addItem(" ")
        self.comboBoxLaboratorio.addItem("BIOTECNOLOGÍA")
        self.comboBoxLaboratorio.addItem("CIROC-SUELOS")
        self.comboBoxLaboratorio.addItem("CDT")
        self.comboBoxLaboratorio.addItem("HIDRÁULICA")
        self.comboBoxLaboratorio.addItem("TOPOGRAFÍA")
        self.comboBoxLaboratorio.addItem("PPA'S")
        self.comboBoxLaboratorio.addItem("CTAS")

        self.comboBoxCalibracion.addItem(" ")
        self.comboBoxCalibracion.addItem("SI")
        self.comboBoxCalibracion.addItem("NO")

        self.comboBoxMantenimientoEquipo.addItem("Frecuencia de mantenimiento")
        self.comboBoxMantenimientoEquipo.addItem("SEMESTRAL")
        self.comboBoxMantenimientoEquipo.addItem("ANUAL")
        self.comboBoxMantenimientoEquipo.addItem("2 AÑOS")
        self.comboBoxMantenimientoEquipo.addItem("3 AÑOS")

        self.comboBoxBuscarEquipo.addItem("ID")
        self.comboBoxBuscarEquipo.addItem("NOMBRE")
        self.comboBoxBuscarEquipo.addItem("CODIGO")
        """
        self.comboBoxBuscarMaquina.addItem("ID")
        self.comboBoxBuscarMaquina.addItem("NOMBRE")
        self.comboBoxBuscarMaquina.addItem("TIPO")
        """
        #"Inicializacion de Mantenimientos"
        DB.metodos.LoadDataTabla3(self)
        DB.metodos.LoadDataTablaMantenimientosRealizados(self)
        self.pushButton_36.clicked.connect(self.Guardar)
        self.pushButton_37.clicked.connect(self.Modificar)
        self.pushButton_42.clicked.connect(self.Buscar)
        self.pushButton_41.clicked.connect(self.Eliminar)
        self.pushButton_35.clicked.connect(self.ConsultaIDEquipo)
        self.pushButton_34.clicked.connect(self.ConsultaIDLaboratorista)
        self.pushButton_55.clicked.connect(self.ConsultaIDProveedor)
        self.comboBoxBuscarInstrumentoReparacion.addItem("ID")
        self.comboBoxBuscarInstrumentoReparacion.addItem("ID LABORATORISTA")
        self.comboBoxBuscarInstrumentoReparacion.addItem("ID EQUIPO")
        self.comboBoxBuscarInstrumentoReparacion.addItem("ID PROVEEDOR")

        self.comboBox_10.addItem("ID")
        self.comboBox_10.addItem("ID LABORATORISTA")
        self.comboBox_10.addItem("ID EQUIPO")
        self.comboBox_10.addItem("ID PROVEEDOR")

        #"Inicializacion de Proveedores"
        DB.metodos.LoadDataTablaProveedores(self)
        self.pushButton_62.clicked.connect(self.GuardarP)
        self.pushButton_61.clicked.connect(self.ModificarP)
        self.pushButton_66.clicked.connect(self.BuscarP)
        self.pushButton_65.clicked.connect(self.EliminarP)
        self.pushButton_23.clicked.connect(self.SeleccionarArchivo)
        self.comboBoxBProveedores.addItem("ID")
        self.comboBoxBProveedores.addItem("NOMBRE")
        self.comboBoxBProveedores.addItem("NIT")
        #"Medotodos de las Tablas"
        self.TProveedores.selectionModel().selectionChanged.connect(self.seleccionarProveedores)
        self.Tequipos.selectionModel().selectionChanged.connect(self.seleccionarEquipos)
        self.TManteniR.selectionModel().selectionChanged.connect(self.seleccionarMantenimientoRealizados)
        self.TMantenimientosEnCurso.selectionModel().selectionChanged.connect(self.seleccionarMantenimientoEnCurso)

        #self.TConsultaInstrumento.selectionModel().selectionChanged.connect(self.seleccionarEquipos)
    def seleccionarEquipos(self, seleccion):
        if seleccion.indexes():
            self.fila = seleccion.indexes()[0].row()
            self.columna = seleccion.indexes()[0].column()
            ID =  self.Tequipos.item(self.fila,0).text()
            Nombre =  self.Tequipos.item(self.fila,1).text()
            vida_util =  self.Tequipos.item(self.fila,2).text()
            Mantenimientos =  self.Tequipos.item(self.fila,3).text()
            Estado =  self.Tequipos.item(self.fila,4).text()
            Codigo =  self.Tequipos.item(self.fila,5).text()
            Fecha_R =  self.Tequipos.item(self.fila,6).text()
            Fabricante =  self.Tequipos.item(self.fila,7).text()
            Laboratorio =  self.Tequipos.item(self.fila,8).text()
            calibracion =  self.Tequipos.item(self.fila,9).text()
            valor =  self.Tequipos.item(self.fila,10).text()
            self.lineEdit_39.setText(ID)
            self.lineEdit_40.setText(Nombre)
            self.lineEdit_43.setText(vida_util)
            #self.lineEdit_61.setText(Mantenimientos)
            #self.lineEdit_57.setText(Estado)
            self.lineEdit_41.setText(Codigo)
            #self.lineEdit_62.setText(Fecha_R)
            self.lineEdit_42.setText(Fabricante)
            #self.lineEdit_59.setText(Laboratorio)
            #self.lineEdit_64.setText(calibracion)
            self.lineEdit_44.setText(valor)
    def seleccionarProveedores(self, seleccion):
        if seleccion.indexes():
            self.fila = seleccion.indexes()[0].row()
            self.columna = seleccion.indexes()[0].column()
            ID =  self.TProveedores.item(self.fila,0).text()
            FechaDi =  self.TProveedores.item(self.fila,1).text()
            Nombre =  self.TProveedores.item(self.fila,2).text()
            NIT =  self.TProveedores.item(self.fila,3).text()
            Telefono =  self.TProveedores.item(self.fila,4).text()
            Email =  self.TProveedores.item(self.fila,5).text()
            Direccion =  self.TProveedores.item(self.fila,6).text()
            Fax =  self.TProveedores.item(self.fila,7).text()
            Ciudad =  self.TProveedores.item(self.fila,8).text()
            ContactoVentas =  self.TProveedores.item(self.fila,9).text()
            ContactoSoporte =  self.TProveedores.item(self.fila,10).text()
            PDFProveedor = self.TProveedores.item(self.fila,11).text()
            self.lineEdit_67.setText(ID)
            self.lineEdit_60.setText(Nombre)
            self.lineEdit_68.setText(NIT)
            self.lineEdit_61.setText(Telefono)
            self.lineEdit_57.setText(Email)
            self.lineEdit_63.setText(Direccion)
            self.lineEdit_62.setText(Fax)
            self.lineEdit_58.setText(Ciudad)
            self.lineEdit_59.setText(ContactoVentas)
            self.lineEdit_64.setText(ContactoSoporte)
            self.lineEdit_65.setText(PDFProveedor)
            if self.columna == 11:
                dialogo2 = QMessageBox.question(self, "PDF", "Desae abrir el PDF de este proveedor?")
                if dialogo2 == QMessageBox.Yes:
                    subprocess.Popen([rf"C:\Users\Orale\Documents\ProyectoT\Memoria\PDFProveedores\{PDFProveedor}"], shell=True)

    def seleccionarMantenimientoRealizados(self, seleccion):
        if seleccion.indexes():
            self.fila = seleccion.indexes()[0].row()
            self.columna = seleccion.indexes()[0].column()
            Observaciones =  self.TManteniR.item(self.fila,3).text()
            self.textEdit_2.setText(Observaciones)

    def seleccionarMantenimientoEnCurso(self, seleccion):
        if seleccion.indexes():
            self.fila = seleccion.indexes()[0].row()
            self.columna = seleccion.indexes()[0].column()
            ID = self.TMantenimientosEnCurso.item(self.fila,0).text()
            Fecha_ingreso = self.TMantenimientosEnCurso.item(self.fila,1).text()
            Fecha1 = QDate(int(Fecha_ingreso.split("-")[0]),int(Fecha_ingreso.split("-")[1]),int(Fecha_ingreso.split("-")[2]))
            Fecha_Retorno = self.TMantenimientosEnCurso.item(self.fila,2).text()
            Fecha2 = QDate(int(Fecha_Retorno.split("-")[0]), int(Fecha_Retorno.split("-")[1]),int(Fecha_Retorno.split("-")[2]))
            Observaciones =  self.TMantenimientosEnCurso.item(self.fila,3).text()
            ID_Laboratorista = self.TMantenimientosEnCurso.item(self.fila,4).text()
            ID_Equipo = self.TMantenimientosEnCurso.item(self.fila,5).text()
            ID_Proveedor = self.TMantenimientosEnCurso.item(self.fila,6).text()
            Costo = self.TMantenimientosEnCurso.item(self.fila,7).text()
            self.lineEdit_31.setText(ID)
            self.textEdit.setText(Observaciones)
            self.dateEdit_5.setDate(Fecha1)
            self.dateEdit_6.setDate(Fecha2)
            self.lineEdit_33.setText(ID_Laboratorista)
            self.lineEdit_32.setText(ID_Equipo)
            self.lineEdit_45.setText(ID_Proveedor)
            self.lineEdit_47.setText(Costo)
    #"Funcion Inicio"
    def Inicio(self):
        newHeight = 0
        self.Wregistrar.setGeometry(250, 0, 1250, newHeight)
        self.Wreparacion.setGeometry(250, 0, 1250, newHeight)
        self.Wproveedores.setGeometry(0, 0, 1250, newHeight)
        self.PlanM.setGeometry(0, 0, 1250, newHeight)

    #"Funciones Registro"
    def MostrarRegistro(self):
        height = self.Wregistrar.height()
        auxHeight = self.Wreparacion.height()
        auxHeight2 = self.Wproveedores.height()
        auxHeight3 = self.PlanM.height()
        if height == 0:
            newHeight = 750
            if auxHeight != 0:
                auxHeight = 0
                self.Wreparacion.setGeometry(0, 0, 1250, auxHeight)
            if auxHeight2 != 0:
                auxHeight2 = 0
                self.Wproveedores.setGeometry(0, 0, 1250, auxHeight2)
            if auxHeight3 != 0:
                auxHeight3 = 0
                self.PlanM.setGeometry(0, 0, 1250, auxHeight3)
        else:
            newHeight = 0
        self.Wregistrar.setGeometry(0, 0, 1250, newHeight)
    def Guardar1(self):
        dialogo = QMessageBox.question(self, "Guardar", "Seguro Desea Guardar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_39.text()
            Nombre = self.lineEdit_40.text()
            Codigo = self.lineEdit_41.text()
            Vida_util = self.lineEdit_43.text()
            Estado = self.comboBoxEstadoEquipo.currentText()
            Fabricante = self.lineEdit_42.text()
            Mantenimiento = self.comboBoxMantenimientoEquipo.currentText()
            Valor = self.lineEdit_44.text()
            Fecha_Re = self.dateEdit_9.text()
            Laboratorio = self.comboBoxLaboratorio.currentText()
            Calibracion = self.comboBoxCalibracion.currentText()
            val = (ID, Nombre, Vida_util, Mantenimiento, Estado, Codigo, Fecha_Re, Fabricante, Laboratorio, Calibracion, Valor)
            DB.Equipo.agregar(val)
            DB.metodos.LoadDataTabla1(self)

    """ def Guardar2(self):
        dialogo = QMessageBox.question(self, "Guardar", "Seguro Desea Guardar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_25.text()
            Nombre = self.lineEdit_24.text()
            Tipo_Maq = self.lineEdit_26.text()
            Estado = self.comboBoxEstadoMaquina.currentText()
            Fabricante = self.lineEdit_27.text()
            Tipo_Pract = self.lineEdit_28.text()
            Valor = self.lineEdit_29.text()
            Fecha_Re = self.dateEdit_4.text()
            val = (ID, Nombre, Tipo_Maq, Tipo_Pract, Fecha_Re, Fabricante, Valor, Estado)
            DB.Maquina.agregar(val)
            DB.metodos.LoadDataTabla2(self)
        """
    def Modificar1(self):
        dialogo = QMessageBox.question(self, "Modificar", "Seguro Desea Modificar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_39.text()
            Nombre = self.lineEdit_40.text()
            Codigo = self.lineEdit_41.text()
            Vida_util = self.lineEdit_43.text()
            Estado = self.comboBoxEstadoEquipo.currentText()
            Fabricante = self.lineEdit_42.text()
            Mantenimiento = self.comboBoxMantenimientoEquipo.currentText()
            Valor = self.lineEdit_44.text()
            Fecha_Re = self.dateEdit_9.text()
            Laboratorio = self.comboBoxLaboratorio.currentText()
            Calibracion = self.comboBoxCalibracion.currentText()
            val = (Nombre, Vida_util, Mantenimiento, Estado, Codigo, Fecha_Re, Fabricante, Laboratorio, Calibracion, Valor,ID)
            DB.Equipo.Actualizar(val)
            DB.metodos.LoadDataTabla1(self)
    """def Modificar2(self):
        dialogo = QMessageBox.question(self, "Modificar", "Seguro Desea Modificar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_25.text()
            Nombre = self.lineEdit_24.text()
            Tipo_Maq = self.lineEdit_26.text()
            Estado = self.comboBoxEstadoMaquina.currentText()
            Fabricante = self.lineEdit_27.text()
            Tipo_Pract = self.lineEdit_28.text()
            Valor = self.lineEdit_29.text()
            Fecha_Re = self.dateEdit_4.text()
            val = (Nombre, Tipo_Maq, Tipo_Pract, Fecha_Re, Fabricante, Valor, Estado, ID)
            DB.Maquina.Actualizar(val)
            DB.metodos.LoadDataTabla2(self)
            """
    def Buscar1(self):
        Consulta = self.lineEdit_46.text()
        aux = self.comboBoxBuscarEquipo.currentText()
        val=(Consulta,)
        DB.metodos.ConsultaDataTabla1(self,val,aux)

    """def Buscar2(self):
        Consulta = self.lineEdit_30.text()
        aux = self.comboBoxBuscarMaquina.currentText()
        val=(Consulta,)
        DB.metodos.ConsultaDataTabla2(self,val,aux)
        """
    def Eliminar1(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_46.text()
            val = (Consulta,)
            DB.Equipo.Eliminar(val)
            DB.metodos.LoadDataTabla1(self)

    """def Eliminar2(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_30.text()
            val = (Consulta,)
            DB.Maquina.Eliminar(val)
            DB.metodos.LoadDataTabla2(self)
            """

    #"Funciones de Mantenimientos:"
    def MostrarMantenimientos(self):
        height = self.Wreparacion.height()
        auxHeight = self.Wregistrar.height()
        auxHeight2 = self.Wproveedores.height()
        auxHeight3 = self.PlanM.height()
        if height == 0:
            newHeight = 750
            if auxHeight != 0:
                auxHeight = 0
                self.Wregistrar.setGeometry(0, 0, 1250, auxHeight)
            if auxHeight2 != 0:
                auxHeight2 = 0
                self.Wproveedores.setGeometry(0, 0, 1250, auxHeight2)
            if auxHeight3 != 0:
                auxHeight3 = 0
                self.PlanM.setGeometry(0, 0, 1250, auxHeight3)
        else:
            newHeight = 0
        self.Wreparacion.setGeometry(0, 0, 1250, newHeight)
    def ConsultaIDEquipo(self):
        Consulta = self.lineEdit_32.text()
        val = (Consulta,)
        sal=DB.Equipo.ConsultaID(val)
        print(sal)
        if Consulta == "":
            self.consul = False
        else:
            if Consulta in sal[0]:
                dialogo = QMessageBox(self)
                dialogo.setWindowTitle("Existe")
                dialogo.setText("Instrumento Existente")
                dialogo.exec()
                self.consul = True
            else:
                dialogo = QMessageBox(self)
                dialogo.setWindowTitle("Inexistente")
                dialogo.setText("Instrumento Inexistente")
                dialogo.exec()
                self.consul = False
    def ConsultaIDLaboratorista(self):
        Consulta = self.lineEdit_33.text()
        val = (Consulta,)
        sal=DB.metodos.ConsultaIDLaboratorista(val)
        print(sal)
        if Consulta == "":
            self.consul = False
        else:
            if Consulta in sal[0]:
                dialogo = QMessageBox(self)
                dialogo.setWindowTitle("Existe")
                dialogo.setText("Laboratorista Existente")
                dialogo.exec()
                self.consul1 = True
            else:
                dialogo = QMessageBox(self)
                dialogo.setWindowTitle("Inexistente")
                dialogo.setText("Laboratorista Inexistente")
                dialogo.exec()
                self.consul1 = False
    def ConsultaIDProveedor(self):
        Consulta = self.lineEdit_45.text()
        val = (Consulta,)
        sal=DB.Proveedores.ConsultaID(val)
        print(sal)
        if Consulta == "":
            self.consul = False
        else:
            if Consulta in sal[0]:
                dialogo = QMessageBox(self)
                dialogo.setWindowTitle("Existe")
                dialogo.setText("Proveedor Existente")
                dialogo.exec()

            else:
                dialogo = QMessageBox(self)
                dialogo.setWindowTitle("Inexistente")
                dialogo.setText("Proveedor Inexistente")
                dialogo.exec()

    def Guardar(self):
        self.ConsultaIDEquipo()
        self.ConsultaIDLaboratorista()
        print(self.consul)
        print(self.consul1)
        if self.consul and self.consul1:
            dialogo = QMessageBox.question(self, "Guardar", "Seguro Desea Guardar?")
            if dialogo == QMessageBox.Yes:
                ID = self.lineEdit_31.text()
                FechaIngreso = self.dateEdit_5.text()
                FechaRetorno = self.dateEdit_6.text()
                Observaciones = "{}".format(self.textEdit.toPlainText())
                IDLaboratorista = self.lineEdit_33.text()
                IDEquipo = self.lineEdit_32.text()
                IDProveedor = self.lineEdit_45.text()
                Costo = self.lineEdit_47.text()
                val = (ID, FechaIngreso, FechaRetorno,Observaciones,IDLaboratorista,IDEquipo, IDProveedor,Costo)
                dialogo2 = QMessageBox.question(self, "Guardar", "El mantenimiento ya fue realizado? (Dar NO si el Mantenimiento se encuentra en curso)")
                if dialogo2 == QMessageBox.Yes:
                    DB.MantenimientosRealizado.agregar(val)
                else:
                    DB.MantenimientosEnCurso.agregar(val)
                DB.metodos.LoadDataTabla3(self)
                DB.metodos.LoadDataTablaMantenimientosRealizados(self)
        else:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Error")
            dialogo.setText("No se logro Guardar, El Campo de ID Laboratorista o ID Equipo estan vacios o no existen")
            dialogo.exec()

    def Modificar(self):
        self.ConsultaIDEquipo()
        self.ConsultaIDLaboratorista()
        if self.consul and self.consul1:
            dialogo = QMessageBox.question(self, "Modificar", "Seguro Desea Modificar?")
            if dialogo == QMessageBox.Yes:
                ID = self.lineEdit_31.text()
                FechaIngreso = self.dateEdit_5.text()
                FechaRetorno = self.dateEdit_6.text()
                Observaciones = "{}".format(self.textEdit.toPlainText())
                IDLaboratorista = self.lineEdit_33.text()
                IDEquipo = self.lineEdit_32.text()
                IDProveedor = self.lineEdit_45.text()
                Costo = self.lineEdit_47.text()
                val = (FechaIngreso, FechaRetorno, Observaciones, IDLaboratorista, IDEquipo, IDProveedor, Costo,ID)
                DB.MantenimientosEnCurso.Actualizar(val)
                DB.metodos.LoadDataTabla3(self)
        else:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Error")
            dialogo.setText("No se logro Modificar, El Campo de ID Laboratorista o ID Equipo estan vacios o no existen")
            dialogo.exec()
    def Buscar(self):
        Consulta = self.lineEdit_34.text()
        aux = self.comboBoxBuscarInstrumentoReparacion.currentText().split(" ")[-1]
        val=(Consulta,)
        DB.metodos.ConsultaDataTabla3(self,val,aux)
    def Eliminar(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_34.text()
            aux = self.comboBoxBuscarInstrumentoReparacion.currentText().split(" ")[-1]
            val = (Consulta,)
            if aux in "ID":
                DB.MantenimientosEnCurso.Eliminar(val)
            if aux in "LABORATORISTA":
                dialogo = QMessageBox.question(self, "Eliminar", "No se puede borrar por laboratorista")
            if aux in "EQUIPO":
                dialogo2 = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar todos los mantenimientos de este equipo?")
                if dialogo2 == QMessageBox.Yes:
                    DB.MantenimientosEnCurso.EliminarEquipos(val,self)
            if aux in "PROVEEDOR":
                dialogo2 = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar todos los mantenimientos realizados por este proveedor?")
                if dialogo2 == QMessageBox.Yes:
                    DB.MantenimientosEnCurso.EliminarProveedores(val)
            DB.metodos.LoadDataTabla3(self)

    "Funciones de Proveedores"
    def MostrarProveedore(self):
        height = self.Wproveedores.height()
        auxHeight = self.Wregistrar.height()
        auxHeight2 = self.Wreparacion.height()
        auxHeight3 = self.PlanM.height()
        if height == 0:
            newHeight = 750
            if auxHeight != 0:
                auxHeight = 0
                self.Wregistrar.setGeometry(0, 0, 1250, auxHeight)
            if auxHeight2 != 0:
                auxHeight2 = 0
                self.Wreparacion.setGeometry(0, 0, 1250, auxHeight2)
            if auxHeight3 != 0:
                auxHeight3 = 0
                self.PlanM.setGeometry(0, 0, 1250, auxHeight3)
        else:
            newHeight = 0
        self.Wproveedores.setGeometry(0, 0, 1250, newHeight)

    def GuardarP(self):
        dialogo = QMessageBox.question(self, "Guardar", "Seguro Desea Guardar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_67.text()
            FechaDi = self.FDiligenciamiento_2.text()
            Nombre = self.lineEdit_60.text()
            NIT = self.lineEdit_68.text()
            Telefono = self.lineEdit_61.text()
            Email = self.lineEdit_57.text()
            Direccion = self.lineEdit_63.text()
            Fax = self.lineEdit_62.text()
            Ciudad = self.lineEdit_58.text()
            ContactoVentas = self.lineEdit_59.text()
            ContactoSoporte = self.lineEdit_64.text()
            PDFProveedor = self.ArchivoS
            val = (ID, FechaDi, Nombre, NIT, Telefono,Email, Direccion,Fax,Ciudad,ContactoVentas,ContactoSoporte,PDFProveedor )
            DB.Proveedores.agregar(val)
            self.GuardarArchivoProveedores()
            DB.metodos.LoadDataTablaProveedores(self)

    def ModificarP(self):
        dialogo = QMessageBox.question(self, "Modificar", "Seguro Desea Modificar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_67.text()
            FechaDi = self.FDiligenciamiento_2.text()
            Nombre = self.lineEdit_60.text()
            NIT = self.lineEdit_68.text()
            Telefono = self.lineEdit_61.text()
            Email = self.lineEdit_57.text()
            Direccion = self.lineEdit_63.text()
            Fax = self.lineEdit_62.text()
            Ciudad = self.lineEdit_58.text()
            ContactoVentas = self.lineEdit_59.text()
            ContactoSoporte = self.lineEdit_64.text()
            PDFProveedor = self.lineEdit_65.text()
            val = (FechaDi, Nombre, NIT, Telefono, Email, Direccion, Fax, Ciudad, ContactoVentas, ContactoSoporte,PDFProveedor,ID)
            DB.Proveedores.Actualizar(val)
            dialogo2 = QMessageBox.question(self, "Modificar", "Desea Modificar el Archivo PDF tambien?")
            if dialogo2 == QMessageBox.Yes:
                self.GuardarArchivoProveedores()
            DB.metodos.LoadDataTablaProveedores(self)

    def BuscarP(self):
        Consulta = self.lineEdit_66.text()
        aux = self.comboBoxBProveedores.currentText()
        val=(Consulta,)
        DB.metodos.ConsultaDataTablaP(self,val,aux)

    def EliminarP(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_66.text()
            val = (Consulta,)
            DB.Proveedores.Eliminar(val)
            DB.metodos.LoadDataTablaProveedores(self)

    def SeleccionarArchivo(self):
        self.ArchivoE = QFileDialog.getOpenFileName()[0]
        print(self.ArchivoE)
        ArchivoName = self.ArchivoE.split("/")[-1]
        self.ArchivoS = f"{ArchivoName}"
        self.lineEdit_65.setText(ArchivoName)
        subprocess.Popen([rf"C:\Users\Orale\Documents\ProyectoT\Memoria\PDFProveedores\{ArchivoName}"], shell=True)


    def GuardarArchivoProveedores(self):
        shutil.copy(self.ArchivoE, r'C:\Users\Orale\Documents\ProyectoT\Memoria\PDFProveedores')


# Funciones del Plan de mantenimientos
    def MostrarPlan(self):
        height = self.PlanM.height()
        auxHeight = self.Wregistrar.height()
        auxHeight2 = self.Wreparacion.height()
        auxHeight3 = self.Wproveedores.height()
        if height == 0:
            newHeight = 750
            if auxHeight != 0:
                auxHeight = 0
                self.Wregistrar.setGeometry(0, 0, 1250, auxHeight)
            if auxHeight2 != 0:
                auxHeight2 = 0
                self.Wreparacion.setGeometry(0, 0, 1250, auxHeight2)
            if auxHeight3 != 0:
                auxHeight3 = 0
                self.Wproveedores.setGeometry(0, 0, 1250, auxHeight3)
        else:
            newHeight = 0
        self.PlanM.setGeometry(0, 0, 1250, newHeight)

    def GenerarPlanM(self):
        DatosE = DB.Equipo.ConsultarTablaEquipo(self)
        DatosPlanM = DB.PlanM.ConsultarTablaPlanM(self)
        fila = 0
        pronostico1 = "      "
        pronostico2 = "      "
        pronostico3 = "      "
        pronostico4 = "      "
        pronostico5 = "      "
        pronostico6 = "      "
        pronostico7 = "      "
        observaciones = ""

        self.TPlan.setRowCount(len(DatosE))
        for num in DatosPlanM:
            """fecha = "{}".format(num[6])
            proximoM = "{}".format(num[6])
            pronostico1 = "{}".format(num[6])
            pronostico2 = "{}".format(num[6])
            pronostico3 = "{}".format(num[6])
            pronostico4 = "{}".format(num[6])
            pronostico5 = "{}".format(num[6])
            pronostico6 = "{}".format(num[6])
            pronostico7 = "{}".format(num[6])"""
            self.TPlan.setItem(fila, 0, QTableWidgetItem(num[0]))
            self.TPlan.setItem(fila, 1, QTableWidgetItem(num[1]))
            self.TPlan.setItem(fila, 2, QTableWidgetItem(num[2]))
            self.TPlan.setItem(fila, 3, QTableWidgetItem(num[3]))
            self.TPlan.setItem(fila, 4, QTableWidgetItem(num[4]))
            self.TPlan.setItem(fila, 5, QTableWidgetItem(num[5]))
            self.TPlan.setItem(fila, 6, QTableWidgetItem(num[6]))
            self.TPlan.setItem(fila, 7, QTableWidgetItem(num[7]))
            self.TPlan.setItem(fila, 8, QTableWidgetItem(num[8]))
            self.TPlan.setItem(fila, 9, QTableWidgetItem(num[9]))
            self.TPlan.setItem(fila, 10, QTableWidgetItem(num[10]))
            self.TPlan.setItem(fila, 11, QTableWidgetItem(num[11]))
            self.TPlan.setItem(fila, 12, QTableWidgetItem(num[12]))
            self.TPlan.setItem(fila, 13, QTableWidgetItem(num[13]))
            self.TPlan.setItem(fila, 14, QTableWidgetItem(num[14]))
            self.TPlan.setItem(fila, 15, QTableWidgetItem(num[15]))
            fila += 1
        if DatosE > DatosPlanM:
            aux = len(DatosE) - len(DatosPlanM)
            if aux == 1:
                num = DatosE[-1]
                print(num)
            elif aux > 1:
                aux2 = len(DatosE) - aux
                for i in range(aux2,len(DatosE),1):
                    num = DatosE[i]
                    fecha = "{}".format(num[6])
                    if num[3] == "SEMESTRAL":
                        for aux in range(1,8):
                            anoU = fecha.split("-")[0]
                            mesU = fecha.split("-")[1]
                            mesP = int(mesU) + 6
                            AnoP = int(anoU)+aux
                            if mesP > 12:
                                mesP = mesP-12
                            for i in range(8, 15):
                                Nheader = self.TPlan.horizontalHeaderItem(i).text().split(" ")[1]
                                if str(AnoP) == Nheader:
                                    fechaP = str(AnoP) + "-" + str(mesP) + "-" + fecha.split("-")[2] + " - " + str(AnoP) + "-" + fecha.split("-")[1] + "-" + fecha.split("-")[2]
                                    self.TPlan.setItem(fila, i, QTableWidgetItem(fechaP))
                            if aux == 1:
                                self.TPlan.setItem(fila, 7, QTableWidgetItem(fechaP))
                                proximoM = fechaP
                                pronostico1 = fechaP
                            if aux == 2:
                                pronostico2 = fechaP
                            if aux == 3:
                                pronostico3 = fechaP
                            if aux == 4:
                                pronostico4 = fechaP
                            if aux == 5:
                                pronostico5 = fechaP
                            if aux == 6:
                                pronostico6 = fechaP
                            if aux == 7:
                                pronostico7 = fechaP
                    if num[3] == "ANUAL":
                        for aux in range(1,8):
                            anoU = fecha.split("-")[0]
                            AnoP = int(anoU) + aux
                            for i in range(8, 15):
                                Nheader = self.TPlan.horizontalHeaderItem(i).text().split(" ")[1]
                                if str(AnoP) == Nheader:
                                    fechaP = str(AnoP) + "-" + fecha.split("-")[1] + "-" + fecha.split("-")[2]
                                    self.TPlan.setItem(fila, i, QTableWidgetItem(fechaP))
                            if aux == 1:
                                self.TPlan.setItem(fila, 7, QTableWidgetItem(fechaP))
                                proximoM=fechaP
                                pronostico1 = fechaP
                            if aux == 2:
                                pronostico2 = fechaP
                            if aux == 3:
                                pronostico3 = fechaP
                            if aux == 4:
                                pronostico4 = fechaP
                            if aux == 5:
                                pronostico5 = fechaP
                            if aux == 6:
                                pronostico6 = fechaP
                            if aux == 7:
                                pronostico7 = fechaP

                    if num[3] == "2 AÑOS":
                        for aux in range(2,10,2):
                            anoU = fecha.split("-")[0]
                            AnoP = int(anoU) + aux
                            for i in range(8,15):
                                Nheader = self.TPlan.horizontalHeaderItem(i).text().split(" ")[1]
                                if str(AnoP) == Nheader:
                                    fechaP = str(AnoP) + "-" + fecha.split("-")[1] + "-" + fecha.split("-")[2]
                                    self.TPlan.setItem(fila, i, QTableWidgetItem(fechaP))
                            if aux == 2:
                                self.TPlan.setItem(fila, 7, QTableWidgetItem(fechaP))
                                proximoM = fechaP
                                pronostico2 = fechaP
                            if aux == 4:
                                pronostico4 = fechaP
                            if aux == 6:
                                pronostico6 = fechaP

                    if num[3] == "3 AÑOS":
                        for aux in range(3, 10, 3):
                            anoU = fecha.split("-")[0]
                            AnoP = int(anoU) + aux
                            for i in range(8, 15):
                                Nheader = self.TPlan.horizontalHeaderItem(i).text().split(" ")[1]
                                if str(AnoP) == Nheader:
                                    fechaP = str(AnoP) + "-" + fecha.split("-")[1] + "-" + fecha.split("-")[2]
                                    self.TPlan.setItem(fila, i, QTableWidgetItem(fechaP))
                            if aux == 3:
                                self.TPlan.setItem(fila, 7, QTableWidgetItem(fechaP))
                                proximoM = fechaP
                            if aux == 6:
                                pronostico3 = fechaP
                            if aux == 9:
                                pronostico6 = fechaP
                    self.TPlan.setItem(fila, 0, QTableWidgetItem(num[8]))
                    self.TPlan.setItem(fila, 1, QTableWidgetItem(num[5]))
                    self.TPlan.setItem(fila, 2, QTableWidgetItem(num[1]))
                    self.TPlan.setItem(fila, 3, QTableWidgetItem(num[2]))
                    self.TPlan.setItem(fila, 4, QTableWidgetItem(num[9]))
                    self.TPlan.setItem(fila, 5, QTableWidgetItem(num[3]))
                    self.TPlan.setItem(fila, 6, QTableWidgetItem(fecha))
                    fila += 1
                    laboratorio = num[8]
                    codigo = num[5]
                    nombre = num[1]
                    vida_util = num[2]
                    calibracion = num[9]
                    frecuenciaM =num[3]
                    val = (laboratorio, codigo, nombre, vida_util, calibracion, frecuenciaM, fecha, proximoM, pronostico1, pronostico2, pronostico3, pronostico4, pronostico5, pronostico6, pronostico7,observaciones)
                    DB.PlanM.agregar(val)
    def Notificaciones(self):
        DatosPlan = DB.PlanM.ConsultarTablaPlanM(self)
        DatosNoti =DB.Notificaciones.ConsultarTablaNotifiaciones(self)
        for num in DatosPlan:
            auxAno= num[7].split("-")[0]
            auxMes = num[7].split("-")[1]
            auxDia = num[7].split("-")[2]
            FechaAux = FechaH
            if int(auxAno) == int(FechaAux.year()):
                if int(FechaAux.month()) >= 1:
                    aux1 = int(auxMes)-1
                else:
                    aux1 = 12
                if int(auxMes) == int(FechaAux.month()):
                    if int(FechaAux.day()) < int(auxDia):
                        codigo_equipo = num[1]
                        nombre_equipo = num[2]
                        aux3 = "No"
                        for num1 in DatosNoti:
                            if str(num1[2]) == str(codigo_equipo):
                                aux3 = "Si"
                        if aux3 == "No":
                            val = ("Pendientes", codigo_equipo, nombre_equipo)
                            DB.Notificaciones.agregar(val)
                    if int(FechaAux.day()) > int(auxDia):
                        codigo_equipo = num[1]
                        nombre_equipo = num[2]
                        aux3 = "No"
                        for num1 in DatosNoti:
                            if str(num1[2]) == str(codigo_equipo):
                                aux3 = "Si"
                        if aux3 == "No":
                            val = ("Urgente", codigo_equipo, nombre_equipo)
                            DB.Notificaciones.agregar(val)
                if int(FechaAux.month()) == int(aux1):
                    if int(FechaAux.day()) > int(auxDia):
                        codigo_equipo = num[1]
                        nombre_equipo = num[2]
                        aux3 = "No"
                        for num1 in DatosNoti:
                            if str(num1[2])== str(codigo_equipo):
                                aux3= "Si"
                        if aux3 == "No":
                            val=("Pendientes",codigo_equipo,nombre_equipo)
                            DB.Notificaciones.agregar(val)

        Noti = Notify()
        Noti.title = "Notificacion SalleApp"
        Noti.message = "Enviar a mantenimiento correctivo el equipo: "
        #Noti.send()




class MainWindow(QMainWindow, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.IniciarSesion)
        self.InterfazPrincipal = MainWindow2()

    def IniciarSesion(self):
        val = self.lineEdit_3.text()
        val2=self.lineEdit_4.text()
        sal=DB.IniciarSesion.Verificar(val,val2)
        print(sal)
        if sal:
            self.InterfazPrincipal.show()
            self.close()
        else:
            dialogo= QMessageBox(self)
            dialogo.setWindowTitle("Error")
            dialogo.setText("Usuario o Contraseña Equivocada")
            dialogo.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow2()
    Window.show()
    sys.exit(app.exec())
