# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lbleier/cFS/tools/cFS-GroundSystem/Subsystems/tlmGUI/TelemetrySystemDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TelemetrySystemDialog(object):
    def setupUi(self, TelemetrySystemDialog):
        TelemetrySystemDialog.setObjectName("TelemetrySystemDialog")
        TelemetrySystemDialog.resize(625, 908)
        self.verticalLayout = QtWidgets.QVBoxLayout(TelemetrySystemDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(TelemetrySystemDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(80, 32, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(TelemetrySystemDialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.packetCount = QtWidgets.QSpinBox(TelemetrySystemDialog)
        self.packetCount.setReadOnly(True)
        self.packetCount.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.packetCount.setMaximum(16384)
        self.packetCount.setProperty("value", 0)
        self.packetCount.setObjectName("packetCount")
        self.horizontalLayout_2.addWidget(self.packetCount)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.buttonBox = QtWidgets.QDialogButtonBox(TelemetrySystemDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.label_2 = QtWidgets.QLabel(TelemetrySystemDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tblTlmSys = QtWidgets.QTableWidget(TelemetrySystemDialog)
        self.tblTlmSys.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblTlmSys.setObjectName("tblTlmSys")
        self.tblTlmSys.setColumnCount(4)
        self.tblTlmSys.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblTlmSys.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTlmSys.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTlmSys.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTlmSys.setHorizontalHeaderItem(3, item)
        self.tblTlmSys.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tblTlmSys)

        self.retranslateUi(TelemetrySystemDialog)
        self.buttonBox.clicked['QAbstractButton*'].connect(TelemetrySystemDialog.close)
        QtCore.QMetaObject.connectSlotsByName(TelemetrySystemDialog)

    def retranslateUi(self, TelemetrySystemDialog):
        _translate = QtCore.QCoreApplication.translate
        TelemetrySystemDialog.setWindowTitle(_translate("TelemetrySystemDialog", "Dialog"))
        self.label.setText(_translate("TelemetrySystemDialog", "cFE/CFS Subsystem Telemetry"))
        self.label_6.setText(_translate("TelemetrySystemDialog", "Packets Received"))
        self.label_2.setText(_translate("TelemetrySystemDialog", "Available Pages"))
        item = self.tblTlmSys.horizontalHeaderItem(0)
        item.setText(_translate("TelemetrySystemDialog", "Subsystem/Page"))
        item = self.tblTlmSys.horizontalHeaderItem(1)
        item.setText(_translate("TelemetrySystemDialog", "Packet ID"))
        item = self.tblTlmSys.horizontalHeaderItem(2)
        item.setText(_translate("TelemetrySystemDialog", "Packet Count"))
        item = self.tblTlmSys.horizontalHeaderItem(3)
        item.setText(_translate("TelemetrySystemDialog", " "))

