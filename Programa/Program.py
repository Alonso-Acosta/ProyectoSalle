import ast
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Login import Ui_Form1
from InterfazPrincipal import Ui_MainWindow
from Reparacion import  Ui_Form2

from Regitro import Ui_Form
import sys, BaseDatos
DB =BaseDatos


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
        self.ReparacionWindow = ReparacionWindow()
        self.pushButton.clicked.connect(self.Inicio)
        self.Wregistrar.setGeometry(0, 0, 1250,0)
        self.Wreparacion.setGeometry(0, 0, 1250, 0)
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

        "Funcion Inicio"
    def Inicio(self):
        newHeight = 0
        self.Wregistrar.setGeometry(250, 0, 1250, newHeight)
        self.Wreparacion.setGeometry(250, 0, 1250, newHeight)

        "Funciones Registro"
    def MostrarRegistro(self):
        height = self.Wregistrar.height()
        if height == 0:
            newHeight = 750
            auxHeight =0
        else:
            newHeight = 0
        self.Wreparacion.setGeometry(0, 0, 1250, auxHeight)
        self.Wregistrar.setGeometry(0, 0, 1250, newHeight)

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
            DB.metodos.LoadDataTabla1(self)


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
            DB.metodos.LoadDataTabla2(self)



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
            DB.metodos.LoadDataTabla1(self)


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
            DB.metodos.LoadDataTabla2(self)


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
            DB.metodos.LoadDataTabla1(self)


    def Eliminar2(self):
        dialogo = QMessageBox.question(self, "Eliminar", "Seguro Desea Eliminar?")
        if dialogo == QMessageBox.Yes:
            Consulta = self.lineEdit_11.text()
            val = (Consulta,)
            DB.Maquina.Eliminar(val)
            DB.metodos.LoadDataTabla2(self)

    "Funciones de Reparacion:"
    def MostrarReparacion(self):
        height = self.Wreparacion.height()
        auxHeight = self.Wregistrar.height()
        if height == 0:
            newHeight = 750
            if auxHeight != 0:
                auxHeight = 0
                self.Wregistrar.setGeometry(0, 0, 1250, auxHeight)
        else:
            newHeight = 0
        self.Wreparacion.setGeometry(0, 0, 1250, newHeight)


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
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec())