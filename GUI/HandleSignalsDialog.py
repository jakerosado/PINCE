# Form implementation generated from reading ui file 'HandleSignalsDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(363, 523)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_Signals = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget_Signals.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_Signals.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_Signals.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_Signals.setObjectName("tableWidget_Signals")
        self.tableWidget_Signals.setColumnCount(3)
        self.tableWidget_Signals.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Signals.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Signals.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Signals.setHorizontalHeaderItem(2, item)
        self.tableWidget_Signals.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Signals.verticalHeader().setVisible(False)
        self.tableWidget_Signals.verticalHeader().setDefaultSectionSize(16)
        self.tableWidget_Signals.verticalHeader().setMinimumSectionSize(16)
        self.gridLayout.addWidget(self.tableWidget_Signals, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Handle Signals"))
        item = self.tableWidget_Signals.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Signal"))
        item = self.tableWidget_Signals.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Stop & Print"))
        item = self.tableWidget_Signals.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Pass to Program"))
