# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mastergui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MasterGUI(object):
    def setupUi(self, MasterGUI):
        MasterGUI.setObjectName("MasterGUI")
        MasterGUI.resize(784, 743)
        self.centralWidget = QtWidgets.QWidget(MasterGUI)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.overallTabs = QtWidgets.QTabWidget(self.centralWidget)
        self.overallTabs.setAutoFillBackground(True)
        self.overallTabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.overallTabs.setUsesScrollButtons(True)
        self.overallTabs.setMovable(True)
        self.overallTabs.setTabBarAutoHide(True)
        self.overallTabs.setObjectName("overallTabs")
        self.tab_User = QtWidgets.QWidget()
        self.tab_User.setObjectName("tab_User")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_User)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableView_User = QtWidgets.QTableView(self.tab_User)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_User.sizePolicy().hasHeightForWidth())
        self.tableView_User.setSizePolicy(sizePolicy)
        self.tableView_User.setObjectName("tableView_User")
        self.gridLayout_3.addWidget(self.tableView_User, 1, 1, 1, 1)
        self.gridLayout_User = QtWidgets.QGridLayout()
        self.gridLayout_User.setSpacing(6)
        self.gridLayout_User.setObjectName("gridLayout_User")
        self.pb_DBserver = QtWidgets.QPushButton(self.tab_User)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_DBserver.sizePolicy().hasHeightForWidth())
        self.pb_DBserver.setSizePolicy(sizePolicy)
        self.pb_DBserver.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.pb_DBserver.setFont(font)
        self.pb_DBserver.setAutoDefault(False)
        self.pb_DBserver.setDefault(False)
        self.pb_DBserver.setFlat(False)
        self.pb_DBserver.setObjectName("pb_DBserver")
        self.gridLayout_User.addWidget(self.pb_DBserver, 0, 0, 3, 2)
        self.pb_searchUser = QtWidgets.QPushButton(self.tab_User)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.pb_searchUser.setFont(font)
        self.pb_searchUser.setObjectName("pb_searchUser")
        self.gridLayout_User.addWidget(self.pb_searchUser, 1, 3, 2, 1)
        self.lineEdit_User = QtWidgets.QLineEdit(self.tab_User)
        self.lineEdit_User.setObjectName("lineEdit_User")
        self.gridLayout_User.addWidget(self.lineEdit_User, 1, 2, 2, 1)
        self.label_User = QtWidgets.QLabel(self.tab_User)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.label_User.setFont(font)
        self.label_User.setAlignment(QtCore.Qt.AlignCenter)
        self.label_User.setObjectName("label_User")
        self.gridLayout_User.addWidget(self.label_User, 0, 2, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_User, 0, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_fakePercetangeFixed = QtWidgets.QLabel(self.tab_User)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_fakePercetangeFixed.setFont(font)
        self.label_fakePercetangeFixed.setTextFormat(QtCore.Qt.RichText)
        self.label_fakePercetangeFixed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fakePercetangeFixed.setObjectName("label_fakePercetangeFixed")
        self.gridLayout_4.addWidget(self.label_fakePercetangeFixed, 0, 1, 1, 1)
        self.label_fakePercentageVar = QtWidgets.QLabel(self.tab_User)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_fakePercentageVar.setFont(font)
        self.label_fakePercentageVar.setText("")
        self.label_fakePercentageVar.setObjectName("label_fakePercentageVar")
        self.gridLayout_4.addWidget(self.label_fakePercentageVar, 1, 1, 1, 1)
        self.tableView_UserAllReviews = QtWidgets.QTableView(self.tab_User)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_UserAllReviews.sizePolicy().hasHeightForWidth())
        self.tableView_UserAllReviews.setSizePolicy(sizePolicy)
        self.tableView_UserAllReviews.setObjectName("tableView_UserAllReviews")
        self.gridLayout_4.addWidget(self.tableView_UserAllReviews, 0, 0, 2, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.overallTabs.addTab(self.tab_User, "")
        self.tab_Business = QtWidgets.QWidget()
        self.tab_Business.setObjectName("tab_Business")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_Business)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_Business = QtWidgets.QGridLayout()
        self.gridLayout_Business.setSpacing(6)
        self.gridLayout_Business.setObjectName("gridLayout_Business")
        self.label = QtWidgets.QLabel(self.tab_Business)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_Business.addWidget(self.label, 1, 0, 1, 1)
        self.label_BusinessPercentage = QtWidgets.QLabel(self.tab_Business)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_BusinessPercentage.setFont(font)
        self.label_BusinessPercentage.setText("")
        self.label_BusinessPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_BusinessPercentage.setObjectName("label_BusinessPercentage")
        self.gridLayout_Business.addWidget(self.label_BusinessPercentage, 1, 1, 1, 1)
        self.pb_searchBusiness = QtWidgets.QPushButton(self.tab_Business)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.pb_searchBusiness.setFont(font)
        self.pb_searchBusiness.setObjectName("pb_searchBusiness")
        self.gridLayout_Business.addWidget(self.pb_searchBusiness, 0, 1, 1, 1)
        self.tableView_Business = QtWidgets.QTableView(self.tab_Business)
        self.tableView_Business.setObjectName("tableView_Business")
        self.gridLayout_Business.addWidget(self.tableView_Business, 2, 0, 1, 2)
        self.lineEdit_businessInput = QtWidgets.QLineEdit(self.tab_Business)
        self.lineEdit_businessInput.setObjectName("lineEdit_businessInput")
        self.gridLayout_Business.addWidget(self.lineEdit_businessInput, 0, 0, 1, 1)
        self.listView_test = QtWidgets.QListView(self.tab_Business)
        self.listView_test.setObjectName("listView_test")
        self.gridLayout_Business.addWidget(self.listView_test, 3, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_Business, 0, 0, 1, 1)
        self.overallTabs.addTab(self.tab_Business, "")
        self.tab_Recommendation = QtWidgets.QWidget()
        self.tab_Recommendation.setObjectName("tab_Recommendation")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_Recommendation)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_Recomm = QtWidgets.QGridLayout()
        self.gridLayout_Recomm.setSpacing(6)
        self.gridLayout_Recomm.setObjectName("gridLayout_Recomm")
        self.lineEdit_UserForRecom = QtWidgets.QLineEdit(self.tab_Recommendation)
        self.lineEdit_UserForRecom.setObjectName("lineEdit_UserForRecom")
        self.gridLayout_Recomm.addWidget(self.lineEdit_UserForRecom, 0, 1, 1, 1)
        self.pb_SearchForRecom = QtWidgets.QPushButton(self.tab_Recommendation)
        self.pb_SearchForRecom.setObjectName("pb_SearchForRecom")
        self.gridLayout_Recomm.addWidget(self.pb_SearchForRecom, 0, 2, 1, 1)
        self.label_UserIDForRecommendation = QtWidgets.QLabel(self.tab_Recommendation)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_UserIDForRecommendation.setFont(font)
        self.label_UserIDForRecommendation.setTextFormat(QtCore.Qt.RichText)
        self.label_UserIDForRecommendation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_UserIDForRecommendation.setObjectName("label_UserIDForRecommendation")
        self.gridLayout_Recomm.addWidget(self.label_UserIDForRecommendation, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_Recomm, 0, 0, 1, 1)
        self.tableView_Recomm = QtWidgets.QTableView(self.tab_Recommendation)
        self.tableView_Recomm.setObjectName("tableView_Recomm")
        self.gridLayout_6.addWidget(self.tableView_Recomm, 1, 0, 1, 1)
        self.overallTabs.addTab(self.tab_Recommendation, "")
        self.gridLayout_2.addWidget(self.overallTabs, 0, 0, 1, 1)
        MasterGUI.setCentralWidget(self.centralWidget)

        self.retranslateUi(MasterGUI)
        self.overallTabs.setCurrentIndex(1)
        self.pb_DBserver.clicked.connect(MasterGUI.close)
        QtCore.QMetaObject.connectSlotsByName(MasterGUI)

    def retranslateUi(self, MasterGUI):
        _translate = QtCore.QCoreApplication.translate
        MasterGUI.setWindowTitle(_translate("MasterGUI", "MasterGUI"))
        self.pb_DBserver.setText(_translate("MasterGUI", "DB Server Usr/PW"))
        self.pb_searchUser.setText(_translate("MasterGUI", "Search"))
        self.label_User.setText(_translate("MasterGUI", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">User Search</span></p></body></html>"))
        self.label_fakePercetangeFixed.setText(_translate("MasterGUI", "%Fake Review"))
        self.overallTabs.setTabText(self.overallTabs.indexOf(self.tab_User), _translate("MasterGUI", "User"))
        self.label.setText(_translate("MasterGUI", "% Fake Review"))
        self.pb_searchBusiness.setText(_translate("MasterGUI", "             Search           "))
        self.overallTabs.setTabText(self.overallTabs.indexOf(self.tab_Business), _translate("MasterGUI", "Business"))
        self.pb_SearchForRecom.setText(_translate("MasterGUI", "Search For Recommendation"))
        self.label_UserIDForRecommendation.setText(_translate("MasterGUI", " Enter User ID "))
        self.overallTabs.setTabText(self.overallTabs.indexOf(self.tab_Recommendation), _translate("MasterGUI", "Recommendation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MasterGUI = QtWidgets.QMainWindow()
    ui = Ui_MasterGUI()
    ui.setupUi(MasterGUI)
    MasterGUI.show()
    sys.exit(app.exec_())

