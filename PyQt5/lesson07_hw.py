import sys

from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlRelationalTableModel, QSqlRelation, QSqlTableModel, \
    QSqlRelationalDelegate
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import mainform


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainform.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.db_path = r'db/db_test.sqlite3'
        self.ui.lbl_full_path_db.setText(self.db_path)
        self.ui.btn_db_open.clicked.connect(self.db_file_open)
        self.ui.btn_add.clicked.connect(self.db_add)
        self.ui.btn_add.setEnabled(False)
        self.ui.btn_del.clicked.connect(self.db_del)
        self.ui.btn_del.setEnabled(False)
        self.ui.save_changes.clicked.connect(self.save_change_db)
        self.ui.save_changes.setEnabled(False)
        self.ui.mnu_exit.triggered.connect(self.close)
        self.ui.tablelist.setEnabled(False)
        self.db = None
        self.db_model = None
        self.open_db()
        self.ui.tablelist.currentIndexChanged.connect(self.show_table)

    def open_db(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.db_path)
        self.db.open()
        self.get_tables_name()
        # self.show_table()

    def get_tables_name(self):
        self.ui.tablelist.clear()
        for table_name in self.db.tables():
            self.ui.tablelist.addItem(table_name)

    def db_file_open(self):
        self.db_path = QFileDialog.getOpenFileName(self, "Open file")[0]
        self.ui.lbl_full_path_db.setText(self.db_path)
        self.db.close()
        self.open_db()
        self.ui.tablelist.setEnabled(True)
        self.ui.btn_add.setEnabled(True)
        self.ui.btn_del.setEnabled(True)
        self.ui.save_changes.setEnabled(True)
        self.ui.btn_db_open.setEnabled(False)

    def show_table(self):
        self.table_model = QSqlRelationalTableModel()
        table = self.ui.tablelist.currentText()
        if table == 'goods':
            self.create_goods_table_model()
        elif table == 'employees':
            self.create_employees_table_model()
        elif table == 'units':
            self.create_units_table_model()
        elif table == 'vendors':
            self.create_vendors_table_model()
        elif table == 'positions':
            self.create_positions_table_model()
        elif table == 'categories':
            self.create_categories_table_model()
        else:
            self.table_model.setTable(table)
            self.table_model.select()
        self.table_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        view = self.ui.tableView
        view.setModel(self.table_model)
        view.hideColumn(0)
        view.setItemDelegate(QSqlRelationalDelegate(view))

    def db_add(self):
        self.table_model.insertRows(self.table_model.rowCount(), 1)

    def db_del(self):
        rs = list(map(lambda x: x.row(), self.ui.tableView.selectedIndexes()))
        print(rs)
        for i in rs:
            self.table_model.removeRows(i, 1)

    def create_goods_table_model(self):
        self.table_model.setTable('goods')
        self.table_model.setRelation(2, QSqlRelation('units', 'unit_id', 'unit_name'))
        self.table_model.setRelation(3, QSqlRelation('categories', 'category_id', 'category_name'))
        self.table_model.setRelation(4, QSqlRelation('vendors', 'vendor_id', 'vendor_name'))
        self.table_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Название продукта')
        self.table_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Единица измерения')
        self.table_model.setHeaderData(3, QtCore.Qt.Horizontal, 'Категория продукта')
        self.table_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Поставщик')
        self.table_model.select()

    def create_units_table_model(self):
        self.table_model.setTable('units')
        self.table_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Единица измерения')
        self.table_model.select()

    def create_employees_table_model(self):
        self.table_model.setTable('employees')
        self.table_model.setRelation(2, QSqlRelation('positions', 'position_id', 'position_name'))
        self.table_model.setHeaderData(1, QtCore.Qt.Horizontal, 'ФИО сотрудника')
        self.table_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Должность')
        self.table_model.select()

    def create_positions_table_model(self):
        self.table_model.setTable('positions')
        self.table_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Должность')
        self.table_model.select()

    def create_vendors_table_model(self):
        self.table_model.setTable('vendors')
        self.table_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Наименование')
        self.table_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Форма собственности')
        self.table_model.setHeaderData(3, QtCore.Qt.Horizontal, 'Адрес')
        self.table_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Телефон')
        self.table_model.setHeaderData(5, QtCore.Qt.Horizontal, 'Электронная почта')
        self.table_model.select()

    def create_categories_table_model(self):
        self.table_model.setTable('categories')
        self.table_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Название категории')
        self.table_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Описание категории')
        self.table_model.select()

    def save_change_db(self):
        if self.table_model.submitAll():
            self.ui.statusbar.showMessage('Изменения сохранены')
        else:
            self.ui.statusbar.showMessage(f'{self.table_model.lastError().text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
