import os

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from Login import Ui_Form1
from InterfazPrincipal import Ui_MainWindow
from Reparacion import  Ui_Form2
from DateTime import DateTime
import shutil, subprocess

import sys, BaseDatos
DB =BaseDatos
day =DateTime().day()
month = DateTime().Month()
year = DateTime().year()
"""
class ReparacionWindow(QMainWindow,Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_18.clicked.connect(self.Guardar)
        self.pushButton_19.clicked.connect(self.Modificar)
        self.pushButton_6.clicked.connect(self.Buscar)
        self.pushButton_5.clicked.connect(self.Eliminar)
        self.pushButton_22.clicked.connect(self.Actualizar)
        self.pushButton_2.clicked.connect(self.ConsultaIDInstrU)
        self.pushButton.clicked.connect(self.ConsultaIDLaboratorista)
        self.comboBox_2.addItem("ID")
        self.comboBox_2.addItem("ID LABORATORISTA")
        self.comboBox_2.addItem("ID MAQUINA")


    def Actualizar(self):
        DB.metodos.LoadDataTabla3(self)

    def ConsultaIDInstrU(self):
        Consulta = self.lineEdit_6.text()
        val = (Consulta,)
        sal=DB.Instrumento.ConsultaID(val)
        print(sal)
        if Consulta in sal[0]:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Existe")
            dialogo.setText("Instrumento Existente")
            dialogo.exec_()
        else:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Inexistente")
            dialogo.setText("Instrumento Inexistente")
            dialogo.exec_()

    def ConsultaIDLaboratorista(self):
        Consulta = self.lineEdit_3.text()
        val = (Consulta,)
        sal=DB.metodos.ConsultaIDLaboratorista(val)

        print(sal)
        if Consulta in sal[0]:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Existe")
            dialogo.setText("Laboratorista Existente")
            dialogo.exec()
        else:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Inexistente")
            dialogo.setText("Laboratorista Inexistente")
            dialogo.exec()

    def Guardar(self):
        dialogo = QMessageBox.question(self,"Guardar","Seguro Desea Guardar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit.text()
            FechaIngreso = self.dateEdit.text()
            FechaRetorno = self.dateEdit_3.text()
            Descripcion = "{}".format(self.textEdit.toPlainText())
            IDLaboratorista = self.lineEdit_3.text()
            IDInstrumento = self.lineEdit_6.text()
            print(Descripcion)
            val = (ID, FechaIngreso, FechaRetorno, Descripcion, IDLaboratorista, " ", IDInstrumento)
            DB.Reparacion.agregar(val)



    def Modificar(self):
        dialogo = QMessageBox.question(self, "Modificar", "Seguro Desea Modificar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit.text()
            FechaIngreso = self.dateEdit.text()
            FechaRetorno = self.dateEdit_3.text()
            Descripcion = self.textEdit.toPlainText()
            IDLaboratorista = self.lineEdit_3.text()
            IDInstrumento = self.lineEdit_6.text()
            val = (FechaIngreso, FechaRetorno, Descripcion, IDLaboratorista, " ", IDInstrumento, ID)
            DB.Reparacion.Actualizar(val)


    def Buscar(self):
        Consulta = self.lineEdit_5.text()
        aux = self.comboBox_2.currentText()
        val=(Consulta,)
        print(Consulta)
        DB.metodos.ConsultaDataTabla3(self,val,aux)

    def Eliminar(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_5.text()
            val = (Consulta,)
            DB.Reparacion.Eliminar(val)
"""
"""
class RegistroWindow(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_11.clicked.connect(self.Guardar1)
        self.pushButton_10.clicked.connect(self.Modificar1)
        self.pushButton_2.clicked.connect(self.Buscar1)
        self.pushButton.clicked.connect(self.Eliminar1)
        self.pushButton_14.clicked.connect(self.Guardar2)
        self.pushButton_15.clicked.connect(self.Modificar2)
        self.pushButton_4.clicked.connect(self.Buscar2)
        self.pushButton_3.clicked.connect(self.Eliminar2)
        self.pushButton_18.clicked.connect(self.Actualizar)
        self.pushButton_19.clicked.connect(self.Actualizar2)

        self.comboBox.addItem("BUENO")
        self.comboBox.addItem("REGULAR")
        self.comboBox.addItem("MALO")
        self.comboBox.addItem("PARA REPARACION")

        self.comboBox_3.addItem("BUENO")
        self.comboBox_3.addItem("REGULAR")
        self.comboBox_3.addItem("MALO")
        self.comboBox_3.addItem("PARA REPARACION")

        self.comboBox_2.addItem("ID")
        self.comboBox_2.addItem("NOMBRE")
        self.comboBox_2.addItem("TIPO")

        self.comboBox_4.addItem("ID")
        self.comboBox_4.addItem("NOMBRE")
        self.comboBox_4.addItem("TIPO")

    def Actualizar(self):
        DB.metodos.LoadDataTabla1(self)

    def Actualizar2(self):
        DB.metodos.LoadDataTabla2(self)

    def Guardar1(self):
        dialogo = QMessageBox.question(self, "Guardar", "Seguro Desea Guardar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit.text()
            Nombre = self.lineEdit_2.text()
            Codigo = self.lineEdit_3.text()
            Tipo_instr = self.lineEdit_4.text()
            Estado = self.comboBox.currentText()
            Fabricante = self.lineEdit_6.text()
            Tipo_Pract = self.lineEdit_8.text()
            Valor = self.lineEdit_7.text()
            Fecha_Re = self.dateEdit.text()
            val = (ID, Nombre, Tipo_instr, Tipo_Pract, Estado, Codigo, Fecha_Re, Fabricante, Valor, "0")
            DB.Instrumento.agregar(val)


    def Guardar2(self):
        dialogo = QMessageBox.question(self, "Guardar", "Seguro Desea Guardar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_9.text()
            Nombre = self.lineEdit_10.text()
            Tipo_Maq = self.lineEdit_13.text()
            Estado = self.comboBox_3.currentText()
            Fabricante = self.lineEdit_12.text()
            Tipo_Pract = self.lineEdit_14.text()
            Valor = self.lineEdit_15.text()
            Fecha_Re = self.dateEdit_2.text()
            val = (ID, Nombre, Tipo_Maq, Tipo_Pract, Fecha_Re, Fabricante, Valor, Estado)
            DB.Maquina.agregar(val)


    def Modificar1(self):
        dialogo = QMessageBox.question(self, "Modificar", "Seguro Desea Modificar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit.text()
            Nombre = self.lineEdit_2.text()
            Codigo = self.lineEdit_3.text()
            Tipo_instr = self.lineEdit_4.text()
            Estado = self.comboBox.currentText()
            Fabricante = self.lineEdit_6.text()
            Tipo_Pract = self.lineEdit_8.text()
            Valor = self.lineEdit_7.text()
            Fecha_Re = self.dateEdit.text()
            val = (Nombre, Tipo_instr, Tipo_Pract, Estado, Codigo, Fecha_Re, Fabricante, Valor, "0", ID)
            DB.Instrumento.Actualizar(val)


    def Modificar2(self):
        dialogo = QMessageBox.question(self, "Modificar", "Seguro Desea Modificar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_9.text()
            Nombre = self.lineEdit_10.text()
            Tipo_Maq = self.lineEdit_13.text()
            Estado = self.comboBox_3.currentText()
            Fabricante = self.lineEdit_12.text()
            Tipo_Pract = self.lineEdit_14.text()
            Valor = self.lineEdit_15.text()
            Fecha_Re = self.dateEdit_2.text()
            val = (Nombre, Tipo_Maq, Tipo_Pract, Fecha_Re, Fabricante, Valor, Estado, ID)
            DB.Maquina.Actualizar(val)


    def Buscar1(self):

        Consulta = self.lineEdit_5.text()
        aux = self.comboBox_2.currentText()
        val=(Consulta,)
        print(Consulta)
        DB.metodos.ConsultaDataTabla1(self,val,aux)


    def Buscar2(self):
        Consulta = self.lineEdit_11.text()
        aux = self.comboBox_4.currentText()
        val=(Consulta,)
        DB.metodos.ConsultaDataTabla2(self,val,aux)



    def Eliminar1(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_5.text()
            val = (Consulta,)
            DB.Instrumento.Eliminar(val)


    def Eliminar2(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_11.text()
            val = (Consulta,)
            DB.Maquina.Eliminar(val)
"""

class MainWindow2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.MostrarRegistro)
        self.pushButton_3.clicked.connect(self.MostrarReparacion)
        self.pushButton_5.clicked.connect(self.MostrarProveedore)
        self.pushButton.clicked.connect(self.Inicio)
        self.Wregistrar.setGeometry(0, 0, 1250,0)
        self.Wreparacion.setGeometry(0, 0, 1250, 0)
        self.Wproveedores.setGeometry(0, 0, 1250, 0)
        "Inicializacion de registro"
        DB.metodos.LoadDataTabla1(self)
        DB.metodos.LoadDataTabla2(self)

        self.pushButton_19.clicked.connect(self.Guardar1)
        self.pushButton_18.clicked.connect(self.Modificar1)
        self.pushButton_27.clicked.connect(self.Buscar1)
        self.pushButton_26.clicked.connect(self.Eliminar1)

        self.pushButton_28.clicked.connect(self.Guardar2)
        self.pushButton_29.clicked.connect(self.Modificar2)
        self.pushButton_33.clicked.connect(self.Buscar2)
        self.pushButton_32.clicked.connect(self.Eliminar2)

        self.comboBoxEstadoInstrumento.addItem("BUENO")
        self.comboBoxEstadoInstrumento.addItem("REGULAR")
        self.comboBoxEstadoInstrumento.addItem("MALO")
        self.comboBoxEstadoInstrumento.addItem("PARA REPARACION")

        self.comboBoxEstadoMaquina.addItem("BUENO")
        self.comboBoxEstadoMaquina.addItem("REGULAR")
        self.comboBoxEstadoMaquina.addItem("MALO")
        self.comboBoxEstadoMaquina.addItem("PARA REPARACION")

        self.comboBoxBuscarInstrumento.addItem("ID")
        self.comboBoxBuscarInstrumento.addItem("NOMBRE")
        self.comboBoxBuscarInstrumento.addItem("TIPO")

        self.comboBoxBuscarMaquina.addItem("ID")
        self.comboBoxBuscarMaquina.addItem("NOMBRE")
        self.comboBoxBuscarMaquina.addItem("TIPO")
        "Inicializacion de reparacion"
        DB.metodos.LoadDataTabla3(self)
        self.pushButton_36.clicked.connect(self.Guardar)
        self.pushButton_37.clicked.connect(self.Modificar)
        self.pushButton_42.clicked.connect(self.Buscar)
        self.pushButton_41.clicked.connect(self.Eliminar)
        self.pushButton_35.clicked.connect(self.ConsultaIDInstrU)
        self.pushButton_34.clicked.connect(self.ConsultaIDLaboratorista)
        self.comboBoxBuscarInstrumentoReparacion.addItem("ID")
        self.comboBoxBuscarInstrumentoReparacion.addItem("ID LABORATORISTA")
        self.comboBoxBuscarInstrumentoReparacion.addItem("ID INSTRUMENTO")

        "Inicializacion de Proveedores"
        DB.metodos.LoadDataTablaProveedores(self)
        self.pushButton_62.clicked.connect(self.GuardarP)
        self.pushButton_61.clicked.connect(self.ModificarP)
        self.pushButton_66.clicked.connect(self.BuscarP)
        self.pushButton_65.clicked.connect(self.EliminarP)
        self.pushButton_23.clicked.connect(self.SeleccionarArchivo)
        self.comboBoxBProveedores.addItem("ID")
        self.comboBoxBProveedores.addItem("NOMBRE")
        self.comboBoxBProveedores.addItem("NIT")
        "Medotodos de las Tablas"
        self.TProveedores.selectionModel().selectionChanged.connect(self.seleccionar)

    def seleccionar(self, seleccion):
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
        "Funcion Inicio"
    def Inicio(self):
        newHeight = 0
        self.Wregistrar.setGeometry(250, 0, 1250, newHeight)
        self.Wreparacion.setGeometry(250, 0, 1250, newHeight)
        self.Wproveedores.setGeometry(0, 0, 1250, newHeight)

        "Funciones Registro"
        "Funcion Registro"
    def MostrarRegistro(self):
        height = self.Wregistrar.height()
        auxHeight = self.Wreparacion.height()
        auxHeight2 = self.Wproveedores.height()
        if height == 0:
            newHeight = 750
            if auxHeight != 0:
                auxHeight = 0
                self.Wreparacion.setGeometry(0, 0, 1250, auxHeight)
            if auxHeight2 != 0:
                auxHeight2 = 0
                self.Wproveedores.setGeometry(0, 0, 1250, auxHeight2)
        else:
            newHeight = 0
        self.Wregistrar.setGeometry(0, 0, 1250, newHeight)
    def Guardar1(self):
        dialogo = QMessageBox.question(self, "Guardar", "Seguro Desea Guardar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_16.text()
            Nombre = self.lineEdit_17.text()
            Codigo = self.lineEdit_18.text()
            Tipo_instr = self.lineEdit_20.text()
            Estado = self.comboBoxEstadoInstrumento.currentText()
            Fabricante = self.lineEdit_19.text()
            Tipo_Pract = self.lineEdit_21.text()
            Valor = self.lineEdit_22.text()
            Fecha_Re = self.dateEdit_3.text()
            val = (ID, Nombre, Tipo_instr, Tipo_Pract, Estado, Codigo, Fecha_Re, Fabricante, Valor, "0")
            DB.Instrumento.agregar(val)
            DB.metodos.LoadDataTabla1(self)
    def Guardar2(self):
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
    def Modificar1(self):
        dialogo = QMessageBox.question(self, "Modificar", "Seguro Desea Modificar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_16.text()
            Nombre = self.lineEdit_17.text()
            Codigo = self.lineEdit_18.text()
            Tipo_instr = self.lineEdit_20.text()
            Estado = self.comboBoxEstadoInstrumento.currentText()
            Fabricante = self.lineEdit_19.text()
            Tipo_Pract = self.lineEdit_21.text()
            Valor = self.lineEdit_22.text()
            Fecha_Re = self.dateEdit_3.text()
            val = (Nombre, Tipo_instr, Tipo_Pract, Estado, Codigo, Fecha_Re, Fabricante, Valor, "0", ID)
            DB.Instrumento.Actualizar(val)
            DB.metodos.LoadDataTabla1(self)
    def Modificar2(self):
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
    def Buscar1(self):

        Consulta = self.lineEdit_23.text()
        aux = self.comboBoxBuscarInstrumento.currentText()
        val=(Consulta,)
        DB.metodos.ConsultaDataTabla1(self,val,aux)
    def Buscar2(self):
        Consulta = self.lineEdit_30.text()
        aux = self.comboBoxBuscarMaquina.currentText()
        val=(Consulta,)
        DB.metodos.ConsultaDataTabla2(self,val,aux)
    def Eliminar1(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_23.text()
            val = (Consulta,)
            DB.Instrumento.Eliminar(val)
            DB.metodos.LoadDataTabla1(self)
    def Eliminar2(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_30.text()
            val = (Consulta,)
            DB.Maquina.Eliminar(val)
            DB.metodos.LoadDataTabla2(self)

    "Funciones de Reparacion:"
    def MostrarReparacion(self):
        height = self.Wreparacion.height()
        auxHeight = self.Wregistrar.height()
        auxHeight2 = self.Wproveedores.height()
        if height == 0:
            newHeight = 750
            if auxHeight != 0:
                auxHeight = 0
                self.Wregistrar.setGeometry(0, 0, 1250, auxHeight)
            if auxHeight2 != 0:
                auxHeight2 = 0
                self.Wproveedores.setGeometry(0, 0, 1250, auxHeight2)
        else:
            newHeight = 0
        self.Wreparacion.setGeometry(0, 0, 1250, newHeight)
    def ConsultaIDInstrU(self):
        Consulta = self.lineEdit_32.text()
        val = (Consulta,)
        sal=DB.Instrumento.ConsultaID(val)
        print(sal)
        if Consulta in sal[0]:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Existe")
            dialogo.setText("Instrumento Existente")
            dialogo.exec()
        else:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Inexistente")
            dialogo.setText("Instrumento Inexistente")
            dialogo.exec()
    def ConsultaIDLaboratorista(self):
        Consulta = self.lineEdit_33.text()
        val = (Consulta,)
        sal=DB.metodos.ConsultaIDLaboratorista(val)

        print(sal)
        if Consulta in sal[0]:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Existe")
            dialogo.setText("Laboratorista Existente")
            dialogo.exec()
        else:
            dialogo = QMessageBox(self)
            dialogo.setWindowTitle("Inexistente")
            dialogo.setText("Laboratorista Inexistente")
            dialogo.exec()
    def Guardar(self):
        dialogo = QMessageBox.question(self,"Guardar","Seguro Desea Guardar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_31.text()
            FechaIngreso = self.dateEdit_5.text()
            FechaRetorno = self.dateEdit_6.text()
            Descripcion = "{}".format(self.textEdit.toPlainText())
            IDLaboratorista = self.lineEdit_33.text()
            IDInstrumento = self.lineEdit_32.text()
            val = (ID, FechaIngreso, FechaRetorno, Descripcion, IDLaboratorista, " ", IDInstrumento)
            DB.Reparacion.agregar(val)
            DB.metodos.LoadDataTabla3(self)
    def Modificar(self):
        dialogo = QMessageBox.question(self, "Modificar", "Seguro Desea Modificar?")
        if dialogo == QMessageBox.Yes:
            ID = self.lineEdit_31.text()
            FechaIngreso = self.dateEdit_5.text()
            FechaRetorno = self.dateEdit_6.text()
            Descripcion = "{}".format(self.textEdit.toPlainText())
            IDLaboratorista = self.lineEdit_33.text()
            IDInstrumento = self.lineEdit_32.text()
            val = (FechaIngreso, FechaRetorno, Descripcion, IDLaboratorista, " ", IDInstrumento, ID)
            DB.Reparacion.Actualizar(val)
            DB.metodos.LoadDataTabla3(self)
    def Buscar(self):
        Consulta = self.lineEdit_34.text()
        aux = self.comboBoxBuscarInstrumentoReparacion.currentText()
        val=(Consulta,)
        DB.metodos.ConsultaDataTabla3(self,val,aux)
    def Eliminar(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_34.text()
            val = (Consulta,)
            DB.Reparacion.Eliminar(val)
            DB.metodos.LoadDataTabla3(self)

    "Funciones de Proveedores"
    def MostrarProveedore(self):
        height = self.Wproveedores.height()
        auxHeight = self.Wregistrar.height()
        auxHeight2 = self.Wreparacion.height()
        if height == 0:
            newHeight = 750
            if auxHeight != 0:
                auxHeight = 0
                self.Wregistrar.setGeometry(0, 0, 1250, auxHeight)
            if auxHeight2 != 0:
                auxHeight2 = 0
                self.Wreparacion.setGeometry(0, 0, 1250, auxHeight2)
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
            self.GuardarArchivo()
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
                self.GuardarArchivo()
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


    def GuardarArchivo(self):
        shutil.copy(self.ArchivoE, r'C:\Users\Orale\Documents\ProyectoT\Memoria\PDFProveedores')



#class MetodosAux:



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
